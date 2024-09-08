from infini.injector import Injector
from infini.input import Input
from infini.output import Output
from infini.typing import List, Any, RouterType, Callable, Generator, Union
from infini.queue import EventQueue


class Interceptor:
    interceptors: List[RouterType]

    def input(self, input: Input) -> Generator[Union[Output, Input], Any, None]:
        injector = Injector()
        parameters = {
            "input": input,
            "plain_text": input.get_plain_text(),
            "user_id": input.get_user_id(),
        }
        queue = self.match(injector, **parameters)
        while not queue.is_empty():
            if isinstance(
                stream := injector.output(queue.pop(), parameters=parameters),
                Generator,
            ):
                for outcome in stream:
                    if isinstance(outcome, Input):
                        input = outcome
                        break
                    yield outcome
                    if outcome.block:
                        return
            else:
                if stream is None:
                    yield Output.empty()
                    return
                if isinstance(stream, Output):
                    yield stream
                    if stream.block:
                        return
                    continue
                input = stream
        yield input

    def output(
        self, output: Output, output_text: str
    ) -> Generator[Union[Output, str], Any, None]:
        input = Input(output_text, variables=output.variables)
        injector = Injector()
        parameters = {
            "input": input,
            "output": output,
            "plain_text": output_text,
            "user_id": input.get_user_id(),
        }
        queue = self.match(injector, **parameters)
        while not queue.is_empty():
            if isinstance(
                stream := injector.output(queue.pop(), parameters=parameters), Generator
            ):
                for outcome in stream:
                    if isinstance(outcome, Input):
                        input = outcome
                        break
                    yield outcome
                    if outcome.block:
                        return
            else:
                if stream is None:
                    yield Output.empty()
                    return
                if isinstance(stream, Output):
                    yield stream
                    if stream.block:
                        return
                    continue
                input = stream
        yield input.get_plain_text()

    def match(
        self, injector: Injector, **parameters
    ) -> EventQueue[
        Callable[..., Union[Input, Output, Generator[Union[Input, Output], Any, None]]]
    ]:
        queue = EventQueue()

        for interceptor in self.interceptors:
            if injector.output(interceptor["router"].match, parameters=parameters):
                queue.push(interceptor["priority"], interceptor["handler"])

        return queue
