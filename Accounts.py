class Account:
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    def calculate_interest(self):
        return self.balance * self.interest

    def update_balance(self, interest_earned):
        self.balance += interest_earned
