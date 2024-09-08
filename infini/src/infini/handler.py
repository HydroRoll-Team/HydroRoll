from infini.injector import Injector
from infini.input import Input
from infini.output import Output
from infini.typing import List, Any, RouterType, Callable, Generator, Union
from infini.queue import EventQueue


class Handler:
    handlers: List[RouterType]

    def input(self, input: Input):
        injector = Injector()
        parameters = {
            "input": input,
            "plain_text": input.get_plain_text(),
            "user_id": input.get_user_id(),
        }
        if (queue := self.match(injector, **parameters)).is_empty():
            yield Output.empty()
            return
        while not queue.is_empty():
            if isinstance(
                stream := injector.output(queue.pop(), parameters=parameters), Generator
            ):
                for output in stream:
                    yield output
                    if output.block:
                        return
            else:
                yield stream
                if stream.block:
                    return

    def match(
        self, injector: Injector, **parameters
    ) -> EventQueue[Callable[..., Union[Output, Generator[Output, Any, None]]]]:
        queue = EventQueue()

        for handler in self.handlers:
            if injector.output(handler["router"].match, parameters=parameters):
                queue.push(handler["priority"], handler["handler"])

        return queue
