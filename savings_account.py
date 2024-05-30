from Accounts import Account

def create_savings_account(balance, interest):
    savings_account = Account(balance, interest)
    interest_earned = savings_account.calculate_interest()
    savings_account.update_balance(interest_earned)
    return savings_account.balance, interest_earned
