from savings_account import create_savings_account
from cd_account import create_cd_account

def main():
    savings_balance = float(input("Enter the savings account balance: "))
    savings_interest = float(input("Enter the savings account interest rate: "))
    cd_balance = float(input("Enter the CD account balance: "))
    cd_interest = float(input("Enter the CD account interest rate: "))

    savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest)
    cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest)

    print(f"Savings Account: Updated Balance = {savings_balance}, Interest Earned = {savings_interest_earned}")
    print(f"CD Account: Updated Balance = {cd_balance}, Interest Earned = {cd_interest_earned}")

if __name__ == "__main__":
    main()
