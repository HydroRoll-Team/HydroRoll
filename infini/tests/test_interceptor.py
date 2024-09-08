from infini.input import Input
from infini.interceptor import Interceptor
from infini.output import Output
from infini.router import Contains


def test_interceptor():
    input = Input("这个人叫简律纯.")
    valid_input = Input("这个叫苏向夜.")

    def intercept(_: Input) -> Input | Output:
        return Output("text", "block.jianlvchun", block=True)

    interceptor = Interceptor()
    interceptor.interceptors = [
        {
            "priority": 1,
            "router": Contains("简律纯"),
            "handler": intercept,
        }
    ]
    for output in interceptor.input(input):
        assert isinstance(output, Output)
        assert output.name == "block.jianlvchun"

    for valid_output in interceptor.input(valid_input):
        assert isinstance(valid_output, Input)
        assert valid_output.get_plain_text() == "这个叫苏向夜."

    for output in interceptor.output(Output("text", "none", block=True), "简律纯"):
        assert isinstance(output, Output)
        assert output.name == "block.jianlvchun"

    for output in interceptor.output(
        Output("text", "none", block=True), "这个叫苏向夜."
    ):
        assert isinstance(output, str)
        assert output == "这个叫苏向夜."
