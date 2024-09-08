from infini.core import Core
from infini.generator import Generator
from infini.handler import Handler
from infini.injector import Injector
from infini.input import Input
from infini.interceptor import Interceptor
from infini.output import Output
from infini.register import Register


def test_register():
    blocked_god_input = Input("这是苏向夜的杰作.")
    snh_input = Input("撅少年狐!")

    register = Register()

    @register.pre_interceptor("苏向夜", priority=0)
    def test_pre_interceptor(_: Input):
        return Output("text", "block.sxy", block=True)

    @register.handler("撅少年狐")
    def test_handler(_: Input):
        return Output("text", "block.snh", block=True)

    register.register_textevent("block.sxy", "不可直呼{{ sxy_id }}的ID")
    register.register_textevent("block.snh", "不许撅{{ get_snh_id }}")

    register.register_variable("sxy_id", "苏向夜")

    @register.dynamic_variable()
    def get_snh_id():
        return "少年狐"

    @register.interceptor("苏向夜", priority=0)
    def test_interceptor(_: Input):
        return Output("text", "block.sxy", block=True)

    pre_interceptor = Interceptor()
    pre_interceptor.interceptors = register.pre_interceptors
    handler = Handler()
    handler.handlers = register.handlers
    generator = Generator()
    generator.events = register.events
    generator.global_variables = register.global_variables
    interceptor = Interceptor()
    interceptor.interceptors = register.interceptors

    core = Core()
    core.pre_interceptor = pre_interceptor
    core.handler = handler
    core.generator = generator
    core.interceptor = interceptor
    core.injector = Injector()

    for output in core.input(blocked_god_input):
        assert output == "不可直呼苏向夜的ID"

    for output in core.input(snh_input):
        assert output == "不许撅少年狐"
