# Example: Private Members
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

# Creating an instance of BankAccount
account = BankAccount("12345", 1000)

# Accessing public methods to interact with private attributes
account.deposit(500)  # Output: Deposited 500. New balance: 1500
print(account.get_balance())  # Output: 1500

# Trying to directly access private attributes (will result in an error)
# print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'

# Accessing private attributes using name mangling (not recommended)
print(account._BankAccount__balance)  # Output: 1500