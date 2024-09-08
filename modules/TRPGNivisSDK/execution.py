from .parsers import Parser
from .interpreter import Interpreter

__all__ = ["Execution"]


class Execution:
    """
    A class representing the execution of Psi code.

    Args:
        input: The input code to be executed.

    Returns:
        None

    Example:
        ```python
        execution = Execution("print('Hello, World!')")
        execution.execute()
        ```
    """

    def __init__(self, input):
        """
        Initializes an Execution object.

        Args:
            input: The input code to be executed.

        Returns:
            None
        """
        self.input = input

    def execute(self):
        """
        Executes the input code.

        Returns:
            The result of the execution.
        """
        parser = Parser(self.input)
        ast = parser.parse()

        interpreter = Interpreter(ast)
        return interpreter.interpret()
