class Bank:
    def __init__(self):
        self.accounts = []
    def add_account(self, account):
        for acc in self.accounts:
            if account.account_number == acc.account_number: #i had to look for how to access account number inside self.accounts
                print("Account already exists")
                return
        self.accounts.append(account)
    def find_account(self, account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
        return None
    def remove_account(self, account_number):
        account = self.find_account(account_number)
        if account:
            self.accounts.remove(account)
        else:
            print("Account not found")
    def show_accounts(self):
        for account in self.accounts:
            print(account)