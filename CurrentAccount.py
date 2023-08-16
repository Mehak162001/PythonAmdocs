from ProjectAmdocs import BankAccount


class CurrentAccount(BankAccount):

    # overriding it from ProjectAmdocs
    def __init__(self, account_holder_name, initial_account):
        super().__init__(account_holder_name, initial_account)
        print("*******Current Account Created*******")
    def withdraw(self, amount):
        withdraw_fee = 200
        if amount + withdraw_fee <= self._balance:
            print("Successfully money withdrawn from Current Account :")
            super().withdraw(amount + withdraw_fee)
        else:
            print("Insufficient Balance for withdraw and to charge fee amount ")
