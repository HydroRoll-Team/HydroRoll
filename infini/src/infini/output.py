from infini.typing import Union, Literal, Dict, Any


class Output:
    type: Union[Literal["null", "text", "workflow"], str]
    name: str
    status: int
    block: bool

    variables: Dict[str, Any]

    def __init__(
        self,
        type: Union[Literal["null", "text", "workflow"], str],
        name: str,
        *,
        block: bool = False,
        variables: Dict[str, Any] = {},
    ) -> None:
        self.type = type
        self.name = name
        self.status = 1
        self.block = block
        self.variables = variables

    @classmethod
    def empty(cls) -> "Output":
        return cls("null", "null", block=True)

    def is_empty(self) -> bool:
        return self.type == "null"
