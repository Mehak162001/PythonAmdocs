from ProjectAmdocs import BankAccount
from CurrentAccount import CurrentAccount
from SavingAccount import SavingAccount

print("**********WELCOME*********\n")

try:
    # Test BankAccount
    B1 = BankAccount("Mehak", 500)
    B2 = BankAccount("John", 200)
    B1.withdraw(200)
    B2.deposit(1000)
    print("\n")
    B2.transfer(500, B1)
    B1.chk_balance()
    B2.chk_balance()

    # Test SavingsAccount
    print("\n")
    S1 = SavingAccount("Kitty", 2000)
    S1.deposit(500)
    S1.chk_balance()

    # Test CurrentAccount
    print("\n")
    C1 = CurrentAccount("kitty", 2000)
    C1.deposit(500)
    C1.withdraw(100)
    C1.transfer(500, S1)
    C1.chk_balance()
    S1.chk_balance()

except ValueError as ve:
    print("ValueError:", ve)
