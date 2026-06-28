class InvalidAmountError(Exception):
    """Raised when deposit or withdrawal amount is less than or equal to zero."""
    pass

class InsufficientFundsError(Exception):
    """Raised when withdrawal amount exceeds available balance."""
    pass

class FileOperationError(Exception):
    """Raised when an error occurs during file operations."""
    pass

class AccountHolderNameError(Exception):
    """Raised when the account holder name is invalid."""
    pass

class InvalidChoiceError(Exception):
    """Raised when the user enters an invalid menu choice."""
    pass
