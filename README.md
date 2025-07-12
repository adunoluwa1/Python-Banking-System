# OOP Banking System

This repository contains a simple banking system implemented in Python, demonstrating core object-oriented programming (OOP) principles, security best practices (PIN hashing), and a clear separation of concerns through a layered architecture.

---

## Features

* **Account Creation**: Users can create new bank accounts with unique email addresses, first names, last names, and secure PINs.
* **Secure PIN Handling**: PINs are securely stored using `bcrypt` hashing, preventing plaintext storage and enhancing security.
* **Account Login & Security**: Accounts are secured with a 3-attempt PIN validation. Incorrect attempts lock the account.
* **Balance Inquiry**: Users can check their current account balance.
* **Deposits**: Deposit funds into an account.
* **Withdrawals**: Withdraw cash from an account with checks for sufficient funds.
* **PIN Change**: Users can securely change their account PIN after verifying the current one.
* **Modular Design**: The system is built with a clear separation of responsibilities across `Account`, `AccountRepository`, and `BankManager` classes.

---

## Project Structure

The project is organized into three main Python files, each representing a distinct layer of the application:

* `account.py`: Defines the `Account` class, representing a single bank account's data and core operations (deposit, withdrawal, PIN management).
* `account_repository.py`: Defines the `AccountRepository` class, which acts as an abstraction layer for storing and managing `Account` objects (currently in-memory using a dictionary). It handles adding, retrieving, and checking for the existence of accounts.
* `bank_manager.py`: Defines the `BankManager` class, which serves as the main application interface. It handles user interactions, navigates menus, gathers input, and orchestrates operations by interacting with the `AccountRepository`.
* `main.py`: The entry point of the application, responsible for initializing the `BankManager` and starting the banking system.



