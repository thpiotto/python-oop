from utils import *

class Account:
    
    def __init__(self, number, client, balance, credit_limit=300) -> None:
        
        self.__number = number
        self.__holder = client.full_name
        self.__balance = balance
        self.__credit_limit = credit_limit
        print(f"New account created: [Acc Number]: {self.__number}\n")

    @property
    def balance(self):

        return self.__balance

    @property
    def credit_limit(self):

        return self.__credit_limit

    @credit_limit.setter
    def credit_limit(self, value):
        
        self.__credit_limit = value
        print(f":: CREDIT LIMIT CHANGED ::")
        print(f"[Acc Number]: {self.__number}\n[Credit Limit]: ${money_output(self.credit_limit)}\n")

        return 1

    def general_info(self):

        print(f":: GENERAL INFO - STATEMENT ::")
        print(f"[Acc Number]: {self.__number}")
        print(f"[Holder]: {self.__holder}")
        print(f"[Balance]: ${money_output(self.balance)}")
        print(f"[Credit Limit]: ${money_output(self.credit_limit)}\n")
        
        return 1
    
    def deposit(self, incoming_value):

        print(f":: NEW DEPOSIT to ::\n[Holder]: {self.__holder}")

        if incoming_value >= 0:

            self.__balance += incoming_value
            self.__balance = float_treatment(self.__balance)
            print(f"[VALUE DEPOSITED]: ${money_output(incoming_value)}\n")
            
            return incoming_value
       
        print(f":: WRONG DEPOSIT::\n[ERR]: Negative value! {money_output(incoming_value)}\n")

        return 0

    def withdraw(self, value):

        print(f":: NEW WITHDRAW from ::\n[Holder]: {self.__holder}")

        if value >= 0:

            if self.balance + self.credit_limit > value:

                if value > self.balance:

                    diff = (self.balance - value) * -1
                    self.__balance = 0
                    self.__balance = float_treatment(self.balance)
                    print(f"[VALUE WITHDRAWN]: ${money_output(value)} (Credit Limit remaining: ${self.credit_limit - 1})")
                    print(f"[WARNING]: A difference of ${money_output(diff)} will be withdrawn from your account credit limit.")
                    print(f"[WARNING]: Some taxes and fees will probably be deduct from the account balance next month!\n")
                    self.credit_limit = self.credit_limit - 1
                else:

                    self.__balance -= value
                    self.__balance = float_treatment(self.__balance)
                    print(f"[VALUE WITHDRAWN]: ${money_output(value)}\n")

                return value

            print(f":: WRONG WITHDRAW ::\n[ERR]: Limit exceeded! {money_output(value)} > {money_output(self.balance + self.credit_limit)}\n")

            return 0
        
        print(f":: WRONG WITHDRAW ::\n[ERR]: Negative value! {money_output(value)}\n")

        return 0

    def transfer(self, value, destination_account):

        print(f":: NEW TRANSFER::")

        self.withdraw(value)
        destination_account.deposit(value)

        return 1
