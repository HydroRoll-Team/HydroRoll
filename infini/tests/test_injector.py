from typing import Dict, List, Optional
from unittest.mock import Base
from infini.handler import Handler
from infini.injector import Injector
from infini.input import Input
from infini.loader import Loader
from infini.output import Output
from infini.router import Startswith


def test_injector():
    def name(nickname: str, c: int = 0):
        return nickname, c

    def add(a: int, b: int = 0):
        return a + b

    injector = Injector()
    injector.parameters = {"a": 12, "b": 20, "c": 10, "nickname": "苏向夜"}
    assert injector.inject(add)() == 32
    assert injector.output(add) == 32
    assert injector.output(name) == ("苏向夜", 10)


def test_handler_injector():
    input = Input("test_message")

    def absolute(input: Input[str], plain_text: str) -> Output:
        return input.output(
            "text",
            "absolute",
            block=False,
            variables={
                "text": plain_text,
            },
        )

    def absolute_2(input: Input[str], plain_text: Optional[str]) -> Output:
        return input.output(
            "text",
            "absolute",
            block=False,
            variables={
                "text": plain_text,
            },
        )

    handler = Handler()
    handler.handlers = [
        {
            "priority": 2,
            "router": Startswith(""),
            "handler": absolute,
        },
        {
            "priority": 2,
            "router": Startswith(""),
            "handler": absolute_2,
        },
    ]

    core = Loader().into_core()
    core.handler = handler
    core.generator.events = {
        "absolute": "{{ text }}",
    }

    for output in core.input(input):
        assert output == "test_message"


def test_instance_injector():
    class BaseClass: ...

    class Class(BaseClass):
        value = 10

    def test(
        a: int,
        base: BaseClass,
        b: int = 0,
        cls: Optional[BaseClass] = None,
    ):
        assert isinstance(base, Class)
        assert isinstance(cls, Class)
        assert cls.value == 10
        return a + b

    injector = Injector()
    injector.parameters = {"a": 12, "b": 20, "c": 0, "cls": Class(), "base": Class()}

    assert injector.output(test) == 32


def test_complex_injector():
    def test(data: Dict[str, Dict[str, List[str]]]):
        assert isinstance(data, dict)
        return data["value"]

    injector = Injector()
    injector.parameters = {"data": {"value": 32}}

    assert injector.output(test) == 32
