from savings_account import create_savings_account

# Test the function with sample values
balance = 1000.0
interest_rate = 5.0
months = 12

updated_balance, interest_earned = create_savings_account(balance, interest_rate, months)
print(f"Updated Balance: {updated_balance}")
print(f"Interest Earned: {interest_earned}")
