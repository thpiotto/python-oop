from account import Account
from client import Client


## Inicialization for tests

client1 = Client("Thales Heron", "Piotto de Lira")
client2 = Client("Maria Vitória", "Reiter Grandi")
client3 = Client("Cássia Regina", "Piotto de Lira")

acc1 = Account(1, client1, 0)
acc2 = Account(2, client2, 0)
acc3 = Account(3, client3, 0)

#acc1.general_info()
#acc2.general_info()
#acc3.general_info()

acc1.deposit(500)
#acc2.deposit(600)
#acc3.deposit(-100)

acc1.withdraw(501)
acc1.general_info()
#acc2.withdraw(466.1)

#acc1.transfer(200, acc2)
#acc1.statement()
#acc2.statement()