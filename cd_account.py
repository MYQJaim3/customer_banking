from Accounts import Account

def create_cd_account(balance, interest):
    cd_account = Account(balance, interest)
    interest_earned = cd_account.calculate_interest()
    cd_account.update_balance(interest_earned)
    return cd_account.balance, interest_earned
