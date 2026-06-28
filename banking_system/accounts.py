from abc import ABC, abstractmethod
from exceptions import InvalidAmountError, InsufficientFundsError, AccountHolderNameError
from decorators import transaction_logger

class Account(ABC):
    """Abstract base class for all bank accounts."""
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        if balance < 0:
            raise InvalidAmountError("Initial balance cannot be negative.")
        self.balance = balance

    @property
    def account_holder(self):
        return self.__account_holder

    @account_holder.setter
    def account_holder(self, value):
        value = value.strip()
        if not value:
            raise AccountHolderNameError("Account holder name cannot be empty.")
        if len(value) < 3:
            raise AccountHolderNameError("Account holder name must contain at least 3 characters.")
        self.__account_holder = value.title()

    @abstractmethod
    def deposit(self, amount): 
        pass

    @abstractmethod
    def withdraw(self, amount): 
        pass

    @abstractmethod
    def show_balance(self):
        pass


class SavingsAccount(Account):
    @transaction_logger
    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be greater than zero.")
        self.balance += amount
        print(f"Successfully deposited Rs.{amount} into Savings Account.")
        return amount, self.balance

    @transaction_logger
    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient balance.")
        self.balance -= amount
        print(f"Successfully withdrawn Rs.{amount} from Savings Account.")
        return amount, self.balance

    def show_balance(self):
        print("\n------ Account Details ------")
        print(f"Account Holder : {self.account_holder}")
        print("Account Type   : Savings")
        print(f"Balance        : Rs.{self.balance}")
        print("-----------------------------")


class CurrentAccount(Account):
    @transaction_logger
    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be greater than zero.")
        self.balance += amount
        print(f"Successfully deposited Rs.{amount} into Current Account.")
        return amount, self.balance

    @transaction_logger
    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient balance.")
        self.balance -= amount
        print(f"Successfully withdrawn Rs.{amount} from Current Account.")
        return amount, self.balance

    def show_balance(self):
        print("\n------ Account Details ------")
        print(f"Account Holder : {self.account_holder}")
        print("Account Type   : Current")
        print(f"Balance        : Rs.{self.balance}")
        print("-----------------------------")
