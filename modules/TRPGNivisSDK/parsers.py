from .lexer import Lexer, Token


__all__ = ["Parser"]


class Parser:
    """
    A class representing a parser for Psi code.

    Args:
        input: The input code to be parsed.

    Returns:
        None

    Example:
        ```python
        parser = Parser(input)
        parser.parse()
        ```
    """

    def __init__(self, input):
        """
        Initializes a Parser object.

        Args:
            input: The input code to be parsed.

        Returns:
            None
        """
        self.lexer = Lexer(input)
        self.tokens = iter(self.lexer)
        self.current_token = next(self.tokens)

    def parse(self):
        """
        Parses the input code.

        Returns:
            The result of the parsing.
        """
        return self.parse_expr()

    def parse_expr(self):
        """
        Parses an expression in the input code.

        Returns:
            The result of the parsing.
        """
        token = self.current_token
        if token.value == "?":
            self.eat("?")

            condition = self.parse_condition()

            self.eat(":")

            if condition:
                result = self.parse_reply()
            else:
                result = None

            return result

    def parse_condition(self):
        """
        Parses a condition in the input code.

        Returns:
            The result of the parsing.
        """
        variable = self.parse_variable()
        self.eat("==")
        value = self.parse_value()

        return variable == value

    def parse_variable(self):
        """
        Parses a variable in the input code.

        Returns:
            The result of the parsing.
        """
        token = self.current_token
        self.eat("IDENTIFIER")
        return token.value

    def parse_value(self):
        """
        Parses a value in the input code.

        Returns:
            The result of the parsing.

        Raises:
            Exception: Raised when an invalid value is encountered.
        """
        token = self.current_token
        if token.type == "INTEGER":
            self.eat("INTEGER")
            return token.value
        else:
            raise Exception(f"Invalid value: {token.value}")

    def parse_reply(self):
        """
        Parses a reply in the input code.

        Returns:
            The result of the parsing.

        Raises:
            Exception: Raised when an invalid reply is encountered.
        """
        self.eat("reply")
        self.eat(":")

        token = self.current_token
        if token.type != "SEPARATOR":
            raise Exception(f"Invalid reply: {token.value}")

        return token.value

    def eat(self, expected_type):
        """
        Consumes the current token if it matches the expected type.

        Args:
            expected_type: The expected type of the token.

        Returns:
            None

        Raises:
            Exception: Raised when an unexpected token is encountered.
        """
        if self.current_token.type == expected_type:
            self.current_token = next(self.tokens)
        else:
            raise Exception(f"Unexpected token: {self.current_token.value}")
