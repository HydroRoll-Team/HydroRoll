from .lexer import Token


__all__ = ["Interpreter"]


class Interpreter:
    """
    A class representing an interpreter for Psi code.

    Args:
        ast: The abstract syntax tree (AST) of the code to be interpreted.

    Returns:
        None

    Example:
        ```python
        interpreter = Interpreter(ast)
        interpreter.interpret()
        ```
    """

    def __init__(self, ast):
        """
        Initializes an Interpreter object.

        Args:
            ast: The abstract syntax tree (AST) of the code to be interpreted.

        Returns:
            None
        """
        self.ast = ast

    def interpret(self):
        """
        Interprets the code represented by the AST.

        Returns:
            The result of the interpretation.
        """
        return self.interpret_expr(self.ast)

    def interpret_expr(self, node):
        """
        Interprets an expression node in the AST.

        Args:
            node: The expression node to be interpreted.

        Returns:
            The result of the interpretation.
        """
        if isinstance(node, Token):
            return node.value
        elif isinstance(node, list):
            for expr in node:
                result = self.interpret_expr(expr)
                if result is not None:
                    return result

    def interpret_condition(self, node):
        """
        Interprets a condition node in the AST.

        Args:
            node: The condition node to be interpreted.

        Returns:
            The result of the interpretation.
        """
        variable = self.interpret_expr(node[0])
        value = self.interpret_expr(node[2])

        return variable == value
