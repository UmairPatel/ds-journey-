# Exercise 4 

customer_list = [
    {"name": "Umair", "age": 20, "balance": 25000, "account_type": "Cheque", "is_active": True}, 
    {"name": "Sahil", "age": 21, "balance": 20000, "account_type": "Savings", "is_active": False},
    {"name": "Mike", "age": 25, "balance": 29000, "account_type": "Savings", "is_active": False}
]

def customer_summary(customer_list):
    for summary in customer_list:
        print(f"{summary['name']} is {summary['age']} has a {summary['account_type']} account with the balance of ${summary['balance']:,.2f} and is their account active? {summary['is_active']}")

customer_summary(customer_list)
    