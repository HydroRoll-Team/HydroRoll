from rich.logging import RichHandler
from rich.console import Console

import logging

console = Console()


logging.basicConfig(
    level="INFO",
    format="%(message)s",
    handlers=[
        RichHandler(
            console=console,
            show_time=False,
            show_path=False,
            show_level=True,
            markup=True,
        )
    ],
)

logger = logging.getLogger("rich")
