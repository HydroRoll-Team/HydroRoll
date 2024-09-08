from infini.handler import Handler
from infini.input import Input
from infini.output import Output
from infini.router import Startswith


def test_handler():
    input = Input(".add 1 2")

    def add(input: Input) -> Output:
        return Output(
            "text",
            str(sum(list(map(int, input.get_plain_text().lstrip(".add").split())))),
            block=False,
        )

    def cmd(_: Input) -> Output:
        return Output("text", "cmd", block=False)

    handler = Handler()
    handler.handlers = [
        {
            "priority": 2,
            "router": Startswith(".add"),
            "handler": add,
        },
        {
            "priority": 1,
            "router": Startswith("."),
            "handler": cmd,
        },
    ]

    names = []
    for output in handler.input(input):
        names.append(output.name)
    assert names == ["cmd", "3"]


def test_handler_block():
    input = Input(".add 1 2")

    def add(input: Input) -> Output:
        return Output(
            "text",
            str(sum(list(map(int, input.get_plain_text().lstrip(".add").split())))),
            block=False,
        )

    def cmd(_: Input) -> Output:
        return Output("text", "cmd", block=True)

    handler = Handler()
    handler.handlers = [
        {
            "priority": 2,
            "router": Startswith(".add"),
            "handler": add,
        },
        {
            "priority": 1,
            "router": Startswith("."),
            "handler": cmd,
        },
    ]

    names = []
    for output in handler.input(input):
        names.append(output.name)
    assert names == ["cmd"]


def test_handler_interator():
    input = Input(".add 1 2")

    def add(input: Input):
        yield Output(
            "text",
            str(sum(list(map(int, input.get_plain_text().lstrip(".add").split())))),
            block=False,
        )
        yield Output("text", "ok", block=False)

    handler = Handler()
    handler.handlers = [
        {
            "priority": 1,
            "router": Startswith(".add"),
            "handler": add,
        },
    ]

    names = []
    for output in handler.input(input):
        names.append(output.name)
    assert names == ["3", "ok"]
