class PsiException(Exception):
    """
    An exception class for Psi-specific exceptions.

    This class inherits from the built-in `Exception` class.

    Example:
        ```python
        raise PsiException("An error occurred in the Psi code.")
        ```
    """


class ValueError(PsiException):
    """
    An exception class for value-related errors in Psi code.

    This class inherits from the `PsiException` class.

    Example:
        ```python
        raise ValueError("Invalid value encountered in the Psi code.")
        ```
    """


class GrammarError(PsiException):
    """
    An exception class for grammar-related errors in Psi code.

    This class inherits from the `PsiException` class.

    Example:
        ```python
        raise GrammarError("Invalid grammar encountered in the Psi code.")
        ```
    """
