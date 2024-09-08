from infini.generator import Generator, TextGenerator
from infini.injector import Injector
from infini.output import Output


def test_generator():
    generator = TextGenerator()
    generator.events = {
        "test.event1": "Event1 文本",
    }
    generator.match(Output("text", "test.event1"))
    assert generator.output(Output("text", "test.event1"), Injector()) == "Event1 文本"


def test_generator_with_var():
    generator = TextGenerator()
    generator.events = {
        "test.event1": "Event1 文本: {{ var }}",
    }

    assert (
        generator.output(
            Output("text", "test.event1", variables={"var": "变量测试"}), Injector()
        )
        == "Event1 文本: 变量测试"
    )


def test_generator_injector():
    def name(nickname: str = "苏向夜"):
        return nickname

    injector = Injector()
    injector.parameters = {"a": 12, "b": 20, "c": 0}

    generator = TextGenerator()
    generator.events = {
        "test.event1": "[{{ card_name }}]Event1 文本: {{ var }}",
    }
    generator.global_variables = {"card_name": name}
    assert (
        generator.output(
            Output("text", "test.event1", variables={"var": "变量测试"}), injector
        )
        == "[苏向夜]Event1 文本: 变量测试"
    )

def test_register_generator():
    def name(nickname: str = "苏向夜"):
        return nickname

    custom = TextGenerator()
    custom.type = "custom_text"

    generator = Generator()
    generator.events = {
        "test.event1": "[{{ card_name }}]Event1 文本: {{ var }}",
    }
    generator.generators.update({"custom_text": custom})

    generator.global_variables = {"card_name": name}
    assert (
        generator.output(
            Output("custom_text", "test.event1", variables={"var": "变量测试"}),
            Injector(),
        )
        == "[苏向夜]Event1 文本: 变量测试"
    )
