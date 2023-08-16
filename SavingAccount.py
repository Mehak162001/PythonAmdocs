from ProjectAmdocs import BankAccount


# inheritance
class SavingAccount(BankAccount):

    def __init__(self, account_holder_name, initial_account):
        super().__init__(account_holder_name, initial_account)
        print("********Saving Account Created******")

    # Overriding it from ProjectAmdocs
    def deposit(self, amount):
        if amount > 0:
            interest = amount * 0.03  # with every dep 3% interest
            print("Successfully money deposited from Saving Account:")
            super().deposit(amount + interest)
            print("With Interest of 3% .")
            # calling bankAccount dep function
        else:
            print("Deposit Amount is invalid ")
