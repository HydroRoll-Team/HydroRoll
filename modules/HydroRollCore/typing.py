# ruff: noqa: TCH001
from typing import TYPE_CHECKING, Awaitable, Callable, Optional, TypeVar

if TYPE_CHECKING:
    from typing import Any

    from .core import Core
    from .config import ConfigModel
    from .event import Event
    from .rule import Rule


StateT = TypeVar("StateT")
EventT = TypeVar("EventT", bound="Event[Any]")
RuleT = TypeVar("RuleT", bound="Rule[Any, Any, Any]")
ConfigT = TypeVar("ConfigT", bound=Optional["ConfigModel"])

CoreHook = Callable[["Core"], Awaitable[None]]
RuleHook = Callable[["Rule"], Awaitable[None]]
EventHook = Callable[["Event[Any]"], Awaitable[None]]
