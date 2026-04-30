# Exercise 1: Variables and Types
# Write a program that stores the following information about a fictional bank customer and then prints a sentence describing them. 
# The customer name, age, account balance and whether they are a premium customer or not. 

customer = "Umair"
age = 20
accBal = 900000

premium = input("Are you a premium customer? (Y/N): ")

if premium.lower() == "y":
    print(f"{customer}, {age}, has an account balance of ${accBal:,.2f} and is a premium customer")
elif premium.lower() == "n":
    print(f"{customer}, {age}, has an account balance of ${accBal:,.2f} and is not a premium customer")
else:
    print("Invalid Option, Please try again")