from bank_manager import BankManager
from account_repository import AccountRepository

if __name__ == "__main__":
    account_repo = AccountRepository()
    main = BankManager("GTBank",account_repo)
    main.run()
