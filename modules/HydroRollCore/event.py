from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Generic, Optional, Union
from typing_extensions import Self

from pydantic import BaseModel, ConfigDict
from .typing import RuleT


class Event(ABC, BaseModel, Generic[RuleT]):
    model_config = ConfigDict(extra="allow")

    if TYPE_CHECKING:
        rule: RuleT
    else:
        rule: Any
    type: Optional[str]
    __handled__: bool = False

    def __str__(self) -> str:
        return f"Event<{self.type}>"

    def __repr__(self) -> str:
        return self.__str__()


class MessageEvent(Event[RuleT], Generic[RuleT]):
    """Base class for general message event classes."""

    @abstractmethod
    def get_plain_text(self) -> str:
        """Get the plain text content of the message.

        Returns:
            The plain text content of the message.
        """

    @abstractmethod
    async def reply(self, message: str) -> Any:
        """Reply message.

        Args:
            message: The content of the reply message.

        Returns:
            The response to the reply message action.
        """

    @abstractmethod
    async def is_same_sender(self, other: Self) -> bool:
        """Determine whether itself and another event are the same sender.

        Args:
            other: another event.

        Returns:
            Is it the same sender?
        """

    async def get(
        self,
        *,
        max_try_times: Optional[int] = None,
        timeout: Optional[Union[int, float]] = None,
    ) -> Self:
        """Get the user's reply message.

        Equivalent to `get()` of ``Bot``, the condition is that the adapter, event type and sender are the same.

        Args:
            max_try_times: Maximum number of events.
            timeout: timeout period.

        Returns:
            Message event that the user replies to.

        Raises:
            GetEventTimeout: Maximum number of events exceeded or timeout.
        """

        return await self.rule.get(
            self.is_same_sender,
            event_type=type(self),
            max_try_times=max_try_times,
            timeout=timeout,
        )

    async def ask(
        self,
        message: str,
        max_try_times: Optional[int] = None,
        timeout: Optional[Union[int, float]] = None,
    ) -> Self:
        """Ask for news.

        Indicates getting the user's reply after replying to a message.
        Equivalent to executing ``get()`` after ``reply()``.

        Args:
            message: The content of the reply message.
            max_try_times: Maximum number of events.
            timeout: timeout period.

        Returns:
            Message event that the user replies to.
        """

        await self.reply(message)
        return await self.get(max_try_times=max_try_times, timeout=timeout)
