from account import Account

acc1 = Account(1, 'Thales Lira', 0)
acc2 = Account(2, "Maria Vitória", 0)
acc3 = Account(3, "Cássia Regina", 0)

acc1.statement()
acc2.statement()
acc3.statement()

acc1.deposit(500)
acc2.deposit(1356.9)
acc3.deposit(-100)

acc1.withdraw(502)
acc2.withdraw(466.1)