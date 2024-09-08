from infini.doc import Doc
from infini.input import Input
from infini.interceptor import Interceptor
from infini.generator import Generator
from infini.handler import Handler
from infini.injector import Injector
from infini.output import Output
from infini.typing import Any, Generator as GeneratorT, Union
from infini.exceptions import ValueError


class Core:
    pre_interceptor: Interceptor
    handler: Handler
    generator: Generator
    interceptor: Interceptor
    injector: Injector
    doc: Doc

    def input(self, input: Input) -> GeneratorT[Union[str, Output], Any, None]:
        for pre_intercepted_stream in self.pre_intercept(input):
            if isinstance(pre_intercepted_stream, Output):
                if not isinstance(pre_intercepted_stream, Output):
                    raise ValueError(
                        "Interceptor functions should return or yield a `Output` object."
                    )
                if pre_intercepted_stream.is_empty():
                    return
                if pre_intercepted_stream.type == "workflow":
                    yield pre_intercepted_stream
                    if pre_intercepted_stream.block:
                        while pre_intercepted_stream.status != 0:
                            pass
                    continue
                else:
                    yield self.generate(pre_intercepted_stream)  # TODO 拦截拦截器文本

                if pre_intercepted_stream.block:
                    return
            else:
                input = pre_intercepted_stream

        for handled_stream in self.handle(input):
            if not isinstance(handled_stream, Output):
                raise ValueError(
                    "Handler functions should return or yield a `Output` object."
                )
            if handled_stream.is_empty():
                return
            if handled_stream.type == "workflow":
                yield handled_stream
                if handled_stream.block:
                    while handled_stream.status != 0:
                        pass
                continue
            else:
                outcome = self.generate(handled_stream)
            for stream in self.intercept(handled_stream, outcome):
                if isinstance(stream, Output):
                    if stream.is_empty():
                        return
                    if stream.type == "workflow":
                        yield stream
                        if stream.block:
                            while stream.status != 0:
                                pass
                    else:
                        yield self.generate(stream)
                        if stream.block:
                            return
                    continue
                outcome = stream
            yield outcome
            if handled_stream.block:
                return

    def pre_intercept(
        self, input: Input
    ) -> GeneratorT[Union[Input, Output], Any, None]:
        return self.pre_interceptor.input(input)

    def handle(self, input: Input) -> GeneratorT[Output, Any, None]:
        iterator = self.handler.input(input)
        for output in iterator:
            yield output

    def generate(self, output: Output) -> str:
        return self.generator.output(output, self.injector)

    def intercept(
        self, output: Output, output_text: str
    ) -> GeneratorT[Union[str, Output], Any, None]:
        return self.interceptor.output(output, output_text)
