from infini.typing import Literal, Optional
from infini.typing import Dict, Any, Generic, T, Optional
from infini.output import Output


class Input(Generic[T]):
    plain_data: T
    variables: Dict[str, Any]

    def __init__(
        self, plain_data: T, variables: Optional[Dict[str, Any]] = None
    ) -> None:
        self.plain_data = plain_data
        self.variables = variables or {}

    def get_user_id(self) -> str:
        return self.variables.get("user_id", "0")

    def get_session_id(self) -> str:
        return (
            self.variables.get("group_id")
            or self.variables.get("session_id")
            or self.variables.get("user_id")
            or "0"
        )

    def is_tome(self) -> bool:
        return bool(self.variables.get("is_tome"))

    def get_plain_text(self) -> str:
        return str(self.plain_data)

    def output(
        self,
        type: Literal["text", "workflow"],
        name: str,
        *,
        block: bool = False,
        variables: Dict[str, Any] = {},
    ):
        vars = self.variables.copy()
        vars.update(variables)
        return Output(type, name, block=block, variables=vars)
