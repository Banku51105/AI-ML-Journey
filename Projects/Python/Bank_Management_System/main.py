from bank_account import BankAccount
from customer import Customer
from savings_account import SavingsAccount
from current_account import CurrentAccount
from bank import Bank

customer1 = Customer("Banku", 21)
customer2 = Customer("Gunjan", 20)
account1 = SavingsAccount(10000001, customer1, 5)
account2 = CurrentAccount(10000002, customer2, 1000)
print(account1)
print(account2)
print(f"Total Accounts: {BankAccount.show_total_accounts()}")

try:
    bad = SavingsAccount(1234, customer1, 5)
except ValueError as e:
    print(e)
print(f"Total Accounts: {BankAccount.show_total_accounts()}")

account1.deposit(5000)
print(account1.balance)

try:
    account1.deposit(0)
except ValueError as e:
    print(e)
try:
    account1.deposit(-500)
except ValueError as e:
    print(e)

account1.withdraw(2000)
print(account1.balance)

try:
    account1.withdraw(5000)
except ValueError as e:
    print(e)
print(account1.balance)

account1.transfer(account2, 1000)
print(account1.balance)
print(account2.balance)

account1.add_interest()
print(account1.balance)

account2.withdraw(1500)
print(account2.balance)

try:
    account2.withdraw(1000)
except ValueError as e:
    print(e)
print(account2.balance)

bank = Bank()
bank.add_account(account1)
bank.add_account(account2)
bank.show_accounts()

bank.add_account(account1)

found = bank.find_account(10000001)
print(found)

bank.remove_account(10000002)
bank.show_accounts()

bank.remove_account(10000002)

account1.show_history()
account2.show_history()

accounts = [account1, account2]
for account in accounts:
    print(account)