from infini.output import Output
from infini.typing import Dict, Callable, Union, Optional
from infini.exceptions import UnknownEvent, UnknownEventType
from infini.injector import Injector
from jinja2 import Template

import abc


class BaseGenerator(metaclass=abc.ABCMeta):
    type: str
    events: Dict[str, str]
    global_variables: Dict[str, Union[str, Callable]]

    @abc.abstractmethod
    def output(self, output: Output, injector: Injector) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def match(self, output: Output) -> Template:
        raise NotImplementedError


class TextGenerator(BaseGenerator):
    type = "text"

    def __init__(self) -> None:
        self.events = {}
        self.global_variables = {}

    def output(self, output: Output, injector: Injector) -> str:
        assert (
            output.type == self.type
        ), f"文本生成器应当传入类型为 '{self.type}' 的 Output 实例"
        variables = self.global_variables.copy()
        variables.update(output.variables)
        for name, variable in variables.items():
            if callable(variable):
                variables[name] = injector.output(variable, variables)
        return self.match(output).render(variables)

    def match(self, output: Output) -> Template:
        if context := self.events.get(output.name):
            return Template(context)
        raise UnknownEvent(f"事件不存在: {output.name}")


class Generator:
    generators: Dict[str, BaseGenerator]
    events: Dict[str, str]
    global_variables: Dict[str, Union[str, Callable]]

    def __init__(self) -> None:
        self.generators = {"text": TextGenerator()}

    def output(self, output: Output, injector: Injector) -> str:
        assert (
            output.type != "workflow"
        ), "生成器应当传入类型为非 'workflow' 的 Output 实例"
        if not (generator := self.match(output)):
            raise UnknownEventType(f"没有为事件类型 '{output.type}' 注册生成器")

        generator.events = self.events
        generator.global_variables = self.global_variables
        return generator.output(output, injector)

    def match(self, output: Output) -> Optional[BaseGenerator]:
        return self.generators.get(output.type)
