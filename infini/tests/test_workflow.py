from infini.core import Core
from infini.generator import Generator
from infini.handler import Handler
from infini.injector import Injector
from infini.input import Input
from infini.interceptor import Interceptor
from infini.output import Output
from infini.router import Startswith


def test_workflow():
    def func_workflow(input: Input):
        yield input.output("workflow", "test.workflow", block=True)

    input = Input("testmsg")

    handler = Handler()
    handler.handlers = [
        {
            "priority": 0,
            "router": Startswith(""),
            "handler": func_workflow,
        }
    ]

    interceptor = Interceptor()
    interceptor.interceptors = []

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

    for output in core.input(input):
        assert isinstance(output, Output)
        assert output.type == "workflow"
        output.status = 0
