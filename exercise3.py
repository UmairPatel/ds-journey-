# Exercise 3 

initial_balance = 10000
transactions = [200, -500, 300, -1000, 400, -200, 150, -50] 

def finBal(initial_balance, transactions):
    return initial_balance + sum(transactions)

def count_withdrawels(transactions):
    withdrawels = 0
    for amount in transactions:
        if amount < 0:
            withdrawels += 1
    return withdrawels        

print(f"The total balance is: ${finBal (initial_balance, transactions):,.1f}")
print(f"The amount of withdrawels is: {count_withdrawels (transactions)}")