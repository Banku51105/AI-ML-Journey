from bank_account import BankAccount
from decorators import transaction_logger

class SavingsAccount(BankAccount):
    def __init__(self, account_number, customer, interest_rate):
        super().__init__(account_number, customer)
        self.interest_rate = interest_rate
    @transaction_logger
    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.deposit(interest, record_history=False)
        self.transaction_history.append(f"Interest Added ₹{interest}")