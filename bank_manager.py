"""Bank manager module for managing user accounts and transactions."""

from account import Account
from account_repository import AccountRepository


class BankManager:
    """Class to manage bank accounts, handle user interactions, and perform account operations."""

    def __init__(self, name: str, account_repo: AccountRepository):
        self.name = name
        self.account_repo = account_repo

    def __str__(self):
        return f"Bank Manager for {self.name}"

    def __repr__(self):
        return f"BankManager(name={self.name!r})"

    @property
    def name(self):
        """Returns the Bank's name"""
        return self._name

    @name.setter
    def name(self, name):
        """Sets the Bank's name"""
        self._name = name.title()

    def run(self) -> None:
        """Main loop to interact with the user, allowing account creation and transactions."""
        while True:
            response = self.welcome()
            match response.lower():
                case "1":
                    try:
                        self.get_account()
                        print("Account created successfully")
                    except ValueError as e:
                        print(f"Account Creation Error: {e}")
                case "2":
                    try:
                        email = input("Email: ").lower()
                        acc = self.account_repo.get_account_by_email(email)
                        self.transactions(acc)
                    except ValueError as e:
                        print(f"Account Error: {e}")
                case "x" | "":
                    break
                case _:
                    print("Invalid response")

    def welcome(self):
        """Display the main menu and prompt the user for an action."""
        while True:
            response = input(
                f"""
        ==============================
            Welcome to {self.name}
        ==============================
            1. Create an account
            2. Account transactions
            x. Exit

        """
            ).lower()
            if response not in ["1", "2", "x", ""]:
                print("Invalid response")
                continue
            return response

    def find_account(self, email) -> Account:
        """
        Search for an account by email address using the repository.
        """
        return self.account_repo.get_account_by_email(email)

        # for acc in self.accounts:
        #     if acc.email == email:
        #         return acc
        # raise ValueError("Account does not exist")

    def transactions(self, acc: Account) -> None:
        """
        Handle user transactions for a given account, including login, \
            balance inquiry, deposit, and withdrawal.
        """
        if not acc.login:
            acc.get_pin()  # if account is locked get_pin will unlock it
        if not acc.status:
            raise ValueError("Your account is locked")
        while acc.login:
            response = input(
f"""
                {self.name}
        ==============================
              Account transactions
        ==============================
            1. Check your balance
            2. Deposit money
            3. Withdraw cash
            4. Change Pin
            x. Exit

            """
            ).lower()
            match response:
                case "1":
                    self.account_balance(acc)
                case "2":
                    self.account_deposit(acc)
                case "3":
                    self.account_withrawal(acc)
                case "4":
                    acc.change_pin()
                case "x":
                    acc.login = False
                    return

    def account_balance(self, acc: Account) -> None:
        """Display the account balance for the given account."""
        print(
            f"""
                 {self.name}
        ==============================
                Account balance
        ==============================

        your account balance is ${acc.balance:,.2f}

    """
        )

    def account_deposit(self, acc: Account) -> None:
        """
        Prompt the user to enter an amount to deposit, validate the input, perform the deposit,
        and display the updated account balance; allows exiting by entering 'x'.
        """
        while True:
            amount = input("Enter amount to deposit or [x to Exit]: ").lower()
            if amount == "x":
                return
            try:
                if not amount.isnumeric():
                    raise ValueError("Enter a numeric value or [x to exit]")
                acc.deposit(float(amount))
                print(
                    f"""
                {self.name}
        ==============================
                Cash deposit
        ==============================

        ${float(amount):,.2f} deposited sucessfully!

        your new account balance is ${acc.balance:,.2f}

    """
                )
                return
            except ValueError as e:
                print(f"Transaction Failed: {e}")
                # pass

    def account_withrawal(self, acc: Account) -> None:
        """
        Prompt the user to enter an amount to withdraw, validate the input, perform the withdrawal,
        and display the updated account balance; allows exiting by entering 'x'.
        """
        while True:
            amount = input("Enter amount to withdraw or [x to Exit]: ").lower()
            if amount == "x":
                return
            try:
                if not amount.isnumeric():
                    raise ValueError("Enter a numeric value or [x to exit]")
                acc.withdraw(float(amount))
                print(
                    f"""
                {self.name}
        ==============================
                Cash Withdrawal
        ==============================

        ${float(amount):,.2f} withrawal sucessful!

        your new account balance is ${acc.balance:,.2f}

    """
                )
                return
            except ValueError as e:
                print(f"Transaction Error: {e}")
                # pass

    def get_account(self):
        """
        Prompts the user for their first and last name, validates the input,\
              and returns a dictionary with the user's information.
        """
        # print("Hello, thanks for banking with us! ")
        firstname = input("What's your first name: ").strip().title()
        lastname = input("What's your last name: ").strip().title()
        email = input("What's your email: ").strip()
        try:
            acc = Account(firstname, lastname, email)
            self.account_repo.add_account(acc)
        except ValueError as e:
            print(f"Account creation failed: {e}")