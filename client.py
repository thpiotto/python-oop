from utils import *

class Client:

    def __init__(self, first_name, last_name, default=False) -> None:
        
        self.__first_name = first_name
        self.__last_name = last_name
        self.__full_name = f"{first_name} {last_name}"
        self.__default = default
        print(f"New client created: [Client]: {self.__full_name}\n")

    @property
    def first_name(self):
        
        return self.__first_name

    @property
    def last_name(self):
        
        return self.__last_name

    @property
    def full_name(self):
        
        return self.__full_name

    @property
    def default(self):

        return self.__default

    def general_info(self):

        print(f"[First Name]: {self.first_name}")
        print(f"[Last Name]: {self.last_name}")
        print(f"[Full Name]: {self.full_name}")
        print(f"[Default]: {self.default}")

        return 1

    def change_default_status(self):

        self.__default = not self.__default
        print(f":: DEFAULT STATUS CHANGED ::")
        print(f"[Client]: {self.__full_name}\n[Default]: {self.default}\n")

        return 1
