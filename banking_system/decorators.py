from datetime import datetime
from python_projects.banking_system.exceptions import FileOperationError

def transaction_logger(func):
    """Decorator to log successful transactions into transaction_history.txt."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        account = args[0] 
        amount, balance = result
        try:
            with open("transaction_history.txt", "a") as file:
                file.write(
                    f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n"
                    f"Account Holder: {account.account_holder}\n"
                    f"Transaction: {func.__name__.capitalize()} Rs.{amount}\n"
                    f"Balance: Rs.{balance}\n"
                    f"{'-'*40}\n"
                )
        except Exception:
            raise FileOperationError("Unable to write transaction history.")

        return result

    return wrapper
