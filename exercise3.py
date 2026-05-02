# Exercise 3 

initial_balance = 10000
transactions = [200, -500, 300, -1000, 400, -200, 150, -50] 

def final_balance(initial_balance, transactions):
    return initial_balance + sum(transactions)

def count_withdrawals(transactions):
    withdrawals = 0
    for amount in transactions:
        if amount < 0:
            withdrawals += 1
    return withdrawals        

print(f"The total balance is: ${final_balance(initial_balance, transactions):,.2f}")
print(f"The amount of withdrawals is: {count_withdrawals(transactions)}")