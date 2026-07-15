from abc import ABC, abstractmethod
class Account(ABC):
    def __init__(self, account_number, customer):
        self.account_number = account_number
        self.customer = customer
    @abstractmethod
    def deposit(self, amount):
        pass
    @abstractmethod
    def withdraw(self, amount):
        pass