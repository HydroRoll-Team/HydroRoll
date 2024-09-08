from typing import (
    TYPE_CHECKING,
    Dict as Dict,
    List as List,
    Any as Any,
    Tuple as Tuple,
    Type as Type,
    Optional as Optional,
    Generic as Generic,
    Callable as Callable,
    Literal as Literal,
    Sequence as Sequence,
    Generator as Generator,
    overload as overload,
    TypeVar,
    TypedDict,
    Union,
)
from types import ModuleType as ModuleType, GeneratorType as GeneratorType

if TYPE_CHECKING:
    from infini.router import Router
    from infini.input import Input
    from infini.output import Output

T = TypeVar("T")
Stream = Union["Input[Any]", "Output"]
OutputGenerator = Generator["Output", Any, None]


class RouterType(TypedDict):
    priority: int
    router: "Router"
    handler: Callable[..., Union[Stream, OutputGenerator]]
