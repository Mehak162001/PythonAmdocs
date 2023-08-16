class BankAccount:
    # _balance = None

    def __init__(self, account_holder_name, initial_account):
        # the initial amount should be equal to 0 or greater than zero
        if initial_account >= 0:
            self._balance = initial_account
            self._account_holder_name = account_holder_name
            print("HEY", account_holder_name, "your account created with balance :", self._balance)
        else:
            raise ValueError("Initial Amount cannot be negative :")

    def deposit(self, amount):
        # adding the deposit money in current balance
        # negative money should not be added
        if amount > 0:
            self._balance += amount
            print("Successfully Money Deposited {} in account {}. Your Current balance: {}"
                  .format(amount, self._account_holder_name, self._balance))
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        # money withdrawn should be greater than 0 and less and current balance
        # if not give error
        if 0 < amount <= self._balance:
            self._balance -= amount
            print("Money Withdraw {} from {} . Your Current balance :{}"
                  .format(amount, self._account_holder_name, self._balance))
        else:
            print("Invalid amount entered /insufficient balance .")

    # function to check current balance
    def chk_balance(self):
        print("Your Current Balance of {} is :{}".format(self._account_holder_name, self._balance))

    def transfer(self, amount, account):
        if 0 < amount <= self._balance:
            self.withdraw(amount)
            account.deposit(amount)
            print("Transfer successful from account {}".format(self._account_holder_name))
        else:
            print("Invalid transfer amount or insufficient balance.")
