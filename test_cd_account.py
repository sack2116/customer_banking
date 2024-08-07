from cd_account import create_cd_account

# Test the function with sample values
balance = 1000.0
interest_rate = 5.0
months = 12

updated_balance, interest_earned = create_cd_account(balance, interest_rate, months)
print(f"Updated Balance: {updated_balance:.2f}")
print(f"Interest Earned: {interest_earned:.2f}")
