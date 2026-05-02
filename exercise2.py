# Exercise 2: Lists and Loops
#  You have  a list of 8 transactions. Write a program that prints each transaction one by one, prints the total balance at the end and prints how many transactions were withdrawals. 

initial_balance = 10000
transactions = [200, -500, 300, -1000, 400, -200, 150, -50] 
withdrawels = 0

for amount in transactions:
    if amount <0:
        print(f"Withdrawel: ${(amount):,.2f}")
        withdrawels += 1

total_balance = initial_balance + sum(transactions)
print(f"Total balance: ${total_balance:,.1f}")
print(f"Total withdrawels: {withdrawels}")