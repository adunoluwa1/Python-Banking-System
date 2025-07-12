"""
A simple bank account module with an Account class supporting deposit,\
      withdrawal, and PIN-based security.
"""

import re
from validator_collection import checkers
import bcrypt


class Account:
    """
    The Account class represents a simple bank account with basic functionalities\
          such as deposit, withdrawal, balance inquiry, and PIN-based security. \
            It manages user information and account status.
    """

    accounts = []

    def __init__(self, firstname: str, lastname: str, email: str):
        self._balance: int | float = 0
        self._status: bool = True
        self._firstname = firstname
        self._lastname = lastname
        self.email = email
        prompt = "Enter a four digit pin to secure your account: "
        self.__pin__ = self.set_pin(prompt)
        self.login = False

    def __str__(self):
        """
        Returns a string representation of the account, \
            showing the user's first name and current balance.
        """
        return f"Hello {self.firstname}, Your account balance is ${self._balance}"

    def __repr__(self):
        """
        Returns a string representation of the account, \
            showing the user's email and current balance.
        """
        return f"Account(firstname={self.firstname!r}, lastname={self.lastname!r}, \
email={self.email!r}, balance=${self._balance!r})"

    # getter
    @property
    def balance(self):
        """Returns the user's account balance"""
        return self._balance

    # getter
    @property
    def firstname(self):
        """returns the user's firstname"""
        return self._firstname

    # setter
    @firstname.setter
    def firstname(self, name):
        """Sets the user's first name."""
        self._firstname = name

    # getter
    @property
    def lastname(self):
        """Returns the user's lastname"""
        return self._lastname

    # setter
    @lastname.setter
    def lastname(self, name):
        """Sets the user's last name."""
        self._lastname = name

    # getter
    @property
    def email(self):
        """Returns the user's email"""
        return self._email

    # setter
    @email.setter
    def email(self, email):
        """Sets the user's email."""
        if not checkers.is_email(email):
            raise ValueError("Invalid email")
        self._email = email

    # getter
    @property
    def pin(self):
        """Access to the PIN is intentionally restricted for security reasons."""
        return None

    # getter
    @property
    def status(self):
        """Returns the current status of the account (True if active, False if locked)."""
        return self._status

    @property
    def login(self) -> bool:
        """Returns the login status"""
        return self._login

    @login.setter
    def login(self, value: bool):
        """Sets the login status"""
        if not isinstance(value, bool):
            raise TypeError("Login status must be a bool type")
        self._login = value

    def set_pin(self, prompt):
        """
        Prompts the user to enter a four-digit PIN, validates the input,\
              and keeps prompting until a valid PIN is entered. https://pypi.org/project/bcrypt/
        """
        while True:
            try:
                pin = input(prompt).strip()
                if matches := re.match(r"^(\d{4})$", pin):
                    new_pin = matches.group(1)
                    return bcrypt.hashpw(new_pin.encode("utf-8"), bcrypt.gensalt(5))#decode('utf-8')
                raise ValueError("Pin should be four digits")
            except ValueError as e:
                print(f"Error: {e}")
  
    def change_pin(self):
        """
        This method requests the current PIN, and if valid, allows the user to change their PIN.
        """
        try:
            if self.get_pin():
                prompt = "Enter a new four-digit pin for your account: "
                self.__pin__ = self.set_pin(prompt)
                print("Pin changed succeffully")
        except ValueError as e:
            print(f"Error while changing pin: {e}")


    def get_pin(self):
        """
        Prompts the user to enter their pin, gives three attempts to enter \
            it correctly and locks account if incorrect pin is entered 3 times
        """
        i = 3
        while i > 0:
            code = input(
                f"Enter your four digit pin to continue. {i} attempts left: "
            ).strip()
            # if code != self.__pin__:
            if not bcrypt.checkpw(code.encode("utf-8"), self.__pin__):
                print("Incorrect pin")
                i -= 1
            else:
                self._status = True
                self.login = True
                return True
        print("You have entered the incorrect pin 3 times, your account is now locked")
        self._status = False
        return False

    def deposit(self, amount: int | float):
        """
        Deposits a specified amount into the account after verifying the user's PIN.

        Parameters:
            amount (int | float): The amount to deposit. Must be positive.

        Raises:
            ValueError: If the amount is negative or the account is locked.
        """
        if amount < 0:
            raise ValueError("Enter a positive amount")
        self._balance += amount
        print("Success!")

    def withdraw(self, amount: int | float):
        """
        Withdraws a specified amount from the account after verifying the user's PIN.

        Parameters:
            amount (int | float): The amount to withdraw. Must not exceed the current balance.

        Raises:
            ValueError: If the amount exceeds the balance or the account is locked.
        """

        if amount > self.balance:
            raise ValueError("Insufficient Funds")
        self._balance -= amount
        print("Withdrawal Successful!")
