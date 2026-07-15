from account import Account
from decorators import transaction_logger

class BankAccount(Account):
    total_accounts = 0
    @staticmethod
    def validate_account_number(account_number):
        acc_str = str(account_number)
        if not acc_str.isdigit() or len(acc_str) != 8:
            raise ValueError("Invalid Account Number")
    def __init__(self, account_number, customer):
        super().__init__(account_number, customer)
        self._balance = 0
        self.transaction_history = []
        BankAccount.validate_account_number(account_number)
        BankAccount.total_accounts += 1
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance Cannot Be Negative")
        self._balance = value
    @transaction_logger
    def deposit(self, amount, record_history=True):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0")
        self.balance += amount
        if record_history:
            self.transaction_history.append(f"Deposited: ₹{amount}")
    @transaction_logger
    def withdraw(self, amount, record_history=True):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0")
        elif amount > self.balance:
            raise ValueError("Insufficient Balance")
        self.balance -= amount
        if record_history:
            self.transaction_history.append(f"Withdrawn: ₹{amount}")
    @transaction_logger
    def transfer(self, other_account, amount):
        self.withdraw(amount, record_history=False)
        other_account.deposit(amount, record_history=False)
        self.transaction_history.append(f"Transferred ₹{amount} to Account {other_account.account_number}")
        other_account.transaction_history.append(f"Received ₹{amount} from Account {self.account_number}")
    def show_history(self):
        print("-----Transaction History-----")
        count = 0
        for i in self.transaction_history:
            count +=1
            print(f"{count}. {i}")
        print("-----------------------------")
    @classmethod
    def show_total_accounts(cls):
        return cls.total_accounts
    def __str__(self):
        return f"{'Account Type':<12}: {self.__class__.__name__}\n{'Account No':<12}: {self.account_number}\n{'Owner':<12}: {self.customer.name}\n{'Balance':<12}: ₹{self._balance}"
