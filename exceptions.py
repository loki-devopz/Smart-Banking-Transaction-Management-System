
"""
Custom Exception Module
Defines banking-related exceptions.
"""


class InsufficientBalanceError(Exception):
    """Raised when withdrawal exceeds available balance."""

    pass


class InvalidAmountError(Exception):
    """Raised when an invalid transaction amount is entered."""

    pass


class AccountNotFoundError(Exception):
    """Raised when a requested account does not exist."""

    pass
