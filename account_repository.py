"""Module to represent an abstraction layer between account and bank managger classes. 
It stores and manages account objects."""
from account import Account


class AccountRepository:
    """Class to manage and store accounts. It provides methods for adding,\
          retrieving, updating and deleting accounts."""
    def __init__(self):
        self._accounts: dict[str, Account] = {}


    def add_account(self, account: Account) -> None:
        """Validates if the account already exists via its email address and \
            stores the account email and the account object as a \
                key: value pair in the account respository 

        :raises ValueError: If an account already exists with that email in the respository."""

        if account.email in self._accounts:
            raise ValueError("An account with this email already exists.")
        self._accounts[account.email] = account
        print(f"Account for {account.email} added successfully.")

    def get_account_by_email(self, email: str) -> Account:
        """Searches for the account using its email and returns the account object.

        :raises ValueError: If account does not exist.
        :return Account: Returns the unique account with the email provided.
        :rtype Account: Returns an Account onject.
        """
        account = self._accounts.get(email)
        if not account:
            raise ValueError("Account does not exist.")
        return account

    def account_exists(self, email: str) -> bool:
        """Check if an account exists using its unique email address"""
        return email in self._accounts

    def delete_account(self, email: str):
        """Deletes the account from the account_repository dictionary"""
        self._accounts.pop(email)
        print(f"Account '{email}' deleted successfully.")
