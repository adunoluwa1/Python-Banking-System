from account import Account

def main():
    # Welcome screen
    while True:
        response = welcome()
        match response.lower():
            case "1":
                try:
                    my_acc = Account()
                    print("Account created successfully")
                except ValueError as e:
                    print(f"Account Creation Error: {e}")
                    pass
            case "2":
                try:
                    email = input("Email: ").lower()
                    acc = find_account(email)
                    transactions(acc)
                except ValueError as e:
                    print(f"Account Error: {e}")
                    pass
            case "x" | "":
                break
            case _:
                pass

def welcome():
    response = input(
"""
    ==============================
          Welcome to GTBank
    ==============================
        1. Create an account
        2. Account transactions
        x. Exit
          
""").lower()
    if response not in ["1","2","x", ""]:
        print("Invalid response")
    return response

def transactions(acc:Account) -> None:
    if not acc.login:
        acc.get_pin()
    if not acc.status:
        raise ValueError("Your account is locked")
    while acc.login:
        response = input(
"""
    ==============================
          Account transactions
    ==============================
        1. Check your balance
        2. Deposit money
        3. Withdraw cash
        x. Exit
          
""").lower()
        match response:
            case "1":
                account_balance(acc)
            case "2":
                account_deposit(acc)
            case "3":
                account_withrawal(acc)
            case "x":
                acc.login = False
                return

def account_balance(acc:Account) -> None:
    print(f"""
    ==============================
          Account balance
    ==============================

    your account balance is ${acc.balance:,.2f}

""")

def account_deposit(acc:Account) -> None:
    while True:
        amount = input("Enter amount to deposit or [x to Exit]: ").lower()
        if amount == "x":
            return
        try:
            if not amount.isnumeric():
                raise ValueError("Enter a numeric value or [x to exit]")
            acc.deposit(float(amount))
            print(f"""
    ==============================
             Cash deposit
    ==============================

    ${float(amount):,.2f} deposited sucessfully!

    your new account balance is ${acc.balance:,.2f}

""")
            return
        except ValueError as e:
            print(f"Transaction Failed: {e}")
            pass

def account_withrawal(acc:Account) -> None:
    while True:
        amount = input("Enter amount to withdraw or [x to Exit]: ").lower()
        if amount == "x":
            return
        try:
            if not amount.isnumeric():
                raise ValueError("Enter a numeric value or [x to exit]")
            acc.withdraw(float(amount))
            print(f"""
    ==============================
            Cash Withdrawal
    ==============================

    ${float(amount):,.2f} withrawal sucessful!

    your new account balance is ${acc.balance:,.2f}

""")
            return
        except ValueError as e:
            print(f"Transaction Error: {e}")
            pass

def find_account(email) -> Account:
    for acc in Account.accounts:
        if acc.email == email:
            return acc
    else:
        raise ValueError("Account does not exist")


if __name__ == "__main__":
    main()
