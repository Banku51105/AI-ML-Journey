from bank_account import BankAccount
from decorators import transaction_logger

class CurrentAccount(BankAccount):
    def __init__(self, account_number, customer, overdraft_limit):
        super().__init__(account_number, customer)
        self.overdraft_limit = overdraft_limit
    @property
    def balance(self):
        return super().balance
    @balance.setter
    def balance(self, value):
        if value < -self.overdraft_limit:
            raise ValueError("Balance cannot exceed the Overdraft Limit")
        self._balance = value
    @transaction_logger
    def withdraw(self, amount, record_history=True):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0")
        elif amount > self.balance + self.overdraft_limit:
            raise ValueError("Insufficient Balance")
        self.balance -= amount
        if record_history:
            self.transaction_history.append(f"Withdrawn: ₹{amount}")