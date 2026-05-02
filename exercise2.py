# Exercise 2: Lists and Loops
#  You have  a list of 8 transactions. Write a program that prints each transaction one by one, prints the total balance at the end and prints how many transactions were withdrawals. 

initial_balance = 10000
transactions = [200, -500, 300, -1000, 400, -200, 150, -50] 
withdrawals = 0

for amount in transactions:
    if amount <0:
        print(f"Withdrawal: ${abs(amount):,.2f}")
        withdrawals += 1
    elif amount == 0:
        print("Invalid Amount")
    else:
        print(f"Deposit: ${(amount):,.2f}")

total_balance = initial_balance + sum(transactions)
print(f"Total balance: ${total_balance:,.2f}")
print(f"Total withdrawals: {withdrawals}")