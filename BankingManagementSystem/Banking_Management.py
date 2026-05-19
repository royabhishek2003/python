from pathlib import Path
import os
import math
import random
import string
import json

class Bank:
    
    database= 'data.json'
    data= []
    try:
        if os.path.exists(database):
            with open(database, 'r') as fs:
                data= json.load(fs)
        else:
            print("Database does not exist")    
    except Exception as err:
        print(f"An error occured: {err}")
        
    
    @staticmethod
    def validate_email(email):
        if '@' in email and '.' in email:
            return True
        else:
            return False
    @staticmethod
    def generate_account_number():
        return ''.join(random.choices(string.digits, k=10))
    @staticmethod
    def update_database(data):
        try:
            with open(Bank.database, 'w') as fs:
                json.dump(data, fs)
        except Exception as err:
            print(f"An error occured: {err}") 
    
    def create_account(self):
        data ={
            "name": input("Enter your name: "),
            "age": int(input("Enter your age: ")),
            "email": input("Enter your email: "),
            "pin": int(input("Enter your pin: ")),
            "account_number": Bank.generate_account_number(),
            "balance": 0
        }
        
        if data['age'] < 18 or len(str(data['pin'])) !=4 or not Bank.validate_email(data['email']):
            print("You are not eligible to create an account")
            return
        for i in Bank.data:
            if i['email'] == data['email']:
                print("Email already exists")
                return
        print(f"Account created successfully with account number: {data['account_number']}")
        print(f"Your account details are: {data}")

        Bank.data.append(data)
        Bank.update_database(Bank.data)
    
    def deposit(self):
        account_number = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))
        for i in Bank.data:
            if i['account_number'] == account_number and i['pin'] == pin:
                amount = int(input("Enter the amount to deposit: "))
                i['balance'] += amount
                print(f"Amount deposited successfully. Your new balance is: {i['balance']}")
                Bank.update_database(Bank.data)
                return
            else:
                print("Invalid account number or pin")
    
    def withdraw(self):
        account_number = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))
        for i in Bank.data:
            if i['account_number'] == account_number and i['pin'] == pin:
                amount = int(input("Enter the amount to withdraw: "))
                if amount > i['balance']:
                    print("Insufficient balance")
                    return
                i['balance'] -= amount
                print(f"Amount withdrawn successfully. Your new balance is: {i['balance']}")
                Bank.update_database(Bank.data)
                return
            else:
                print("Invalid account number or pin")
    def check_details(self):
        account_number = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))
        for i in Bank.data:
            if i['account_number'] == account_number and i['pin'] == pin:
                print(f"Your account details are: {i}")
                return
            else:
                print("Invalid account number or pin")
    
    def edit_details(self):
        account_number = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))
        for i in Bank.data:
            if i['account_number'] == account_number and i['pin'] == pin:
                print("Enter the details you want to edit: ")
                print("1. Name")
                print("2. Age")
                print("3. Email")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    i['name'] = input("Enter your new name: ")
                elif choice == 2:
                    i['age'] = int(input("Enter your new age: "))
                elif choice == 3:
                    i['email'] = input("Enter your new email: ")
                else:
                    print("Invalid choice")
                    return
                print(f"Details updated successfully. Your new details are: {i}")
                Bank.update_database(Bank.data)
                return
            else:
                print("Invalid account number or pin")
    
    def delete_account(self):
        account_number = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))
        for i in Bank.data:
            if i['account_number'] == account_number and i['pin'] == pin:
                Bank.data.remove(i)
                print("Account deleted successfully")
                Bank.update_database(Bank.data)
                return
            else:
                print("Invalid account number or pin")
        
    
        

user = Bank()
print("Enter 1 for creating the account")
print("Enter 2 for depositing the money")
print("Enter 3 for withdrawing the money")
print("Enter 4 for check the details of the account")
print('Enter 5 for editing the details of the account')
print("Enter 6 for deleting the account")

check= int(input("Enter your choice: "))

if check ==1:
    user.create_account()
if check ==2:
    user.deposit()
if check ==3:
    user.withdraw()
if check ==4:
    user.check_details()
if check ==5:
    user.edit_details()
if check ==6:
    user.delete_account()
    

    
