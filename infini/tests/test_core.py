from infini.core import Core
from infini.generator import Generator
from infini.handler import Handler
from infini.injector import Injector
from infini.input import Input
from infini.interceptor import Interceptor
from infini.output import Output
from infini.router import Contains, Startswith


def test_core():
    command_input = Input(".add 1 2")
    intercepted_input = Input("这个人叫简律纯.")
    valid_input = Input("这个叫苏向夜.")
    command_and_valid_input = Input(".echo 苏向夜打爆了简某人的狗头")

    def intercept_jianlvchun(_: Input) -> Input | Output:
        return Output("text", "block.jianlvchun", block=True)  # TODO 拦截器阻塞标识

    interceptor = Interceptor()
    interceptor.interceptors = [
        {
            "priority": 1,
            "router": Contains("简律纯"),
            "handler": intercept_jianlvchun,
        }
    ]

    def add(input: Input) -> Output:
        result = str(sum(list(map(int, input.get_plain_text().lstrip(".add").split()))))
        return Output("text", "test.add", block=False, variables={"result": result})

    def cmd(_: Input) -> Output:
        return Output("text", "test.cmd", block=False)

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

    generator = Generator()
    generator.events = {
        "test.cmd": "cmd",
        "test.add": "{{ result }}",
        "block.jianlvchun": "检测到违禁词",
    }
    generator.global_variables = {}

    core = Core()
    core.handler = handler
    core.interceptor = interceptor
    core.pre_interceptor = interceptor
    core.generator = generator
    core.injector = Injector()

    outputs = set()
    for output in core.input(command_input):
        outputs.add(output)
    assert outputs == {"cmd", "3"}

    count = 0
    for _ in core.input(valid_input):
        count += 1
    assert count == 0

    for output in core.input(intercepted_input):
        assert output == "检测到违禁词"

    outputs = set()
    for output in core.input(command_and_valid_input):
        outputs.add(output)
    assert outputs == {"cmd"}
