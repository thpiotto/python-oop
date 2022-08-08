from utils import *

class Account:
    
    def __init__(self, number, holder, balance) -> None:
        
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        print(f"New account created: [Acc Number]: {self.__number}\n")

    def statement(self):

        print(f":: STATEMENT ::\n[Holder]: {self.__holder}\n[Balance]: ${money_output(self.__balance)}\n")
        
        return self.__balance
    
    def deposit(self, incoming_value):
        
        if incoming_value >= 0:

            self.__balance += incoming_value
            self.__balance = float_treatment(self.__balance)
            print(f":: NEW DEPOSIT ::\n[VALUE DEPOSITED]: ${money_output(incoming_value)}\n")
            
            return incoming_value
       
        print(f":: WRONG DEPOSIT ::\n[ERR]: Negative value! {money_output(incoming_value)}\n")

        return 0

    def withdraw(self, value):
        if value >= 0:

            if self.__balance > value:
                
                self.__balance -= value
                self.__balance = float_treatment(self.__balance)
                print(f":: NEW WITHDRAW ::\n[VALUE WITHDRAWN]: ${money_output(value)}\n")

                return value

            print(f":: WRONG WITHDRAW ::\n[ERR]: Limit exceeded! {money_output(value)} > {money_output(self.__balance)}\n")

            return 0
        
        print(f":: WRONG WITHDRAW ::\n[ERR]: Negative value! {money_output(value)}\n")

        return 0
