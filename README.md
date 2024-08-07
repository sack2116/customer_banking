# Customer_Banking Assigment#3
Module 4 Challenge 3 - Customer_Banking

## Overview

This project is designed to simulate a simple banking system where users can create savings and CD (Certificate of Deposit) accounts. The system calculates the interest earned based on user-provided parameters such as initial balance, interest rate, and the number of months.

    """
    Args: For Savings Account
        initial_balance (float): The starting amount of money in the savings account.
        interest_rate (float): The annual interest rate applied to the savings account.
        months (int): The duration (in months) for which the interest is calculated.
        : For CD Account
    Args:
        initial_balance (float): The starting amount of money in the CD account.
        interest_rate (float): The annual interest rate applied to the CD account.
        months (int): The duration (in months) for which the interest is calculated.
        
    Returns: For Savings Account
        tuple: A tuple containing:
            - updated_balance (float): The balance in the savings account after adding interest.
            - interest_earned (float): The amount of interest earned during the period.

            : For CD Account
        tuple: A tuple containing:
            - updated_balance (float): The balance in the CD account after adding interest.
            - interest_earned (float): The amount of interest earned during the period.
    Raises:
        ValueError: If any of the input values are negative or if months is zero.

    Examples:For Savings Account
        >>> create_savings_account(1000.0, 5.0, 12)
        (1050.0, 50.0)

        >>> create_savings_account(500.0, 2.0, 6)
        (505.0, 5.0)

            : For CD Account

        >>> create_cd_account(1000.0, 5.0, 12)
        (1050.0, 50.0)

        >>> create_cd_account(2000.0, 3.0, 24)
        (2100.0, 100.0)


    Note:
        Ensure to run this function in an environment where input() is supported.
    """

## Features

- Interest Calculation:
- Both savings and CD accounts compute interest based on the balance, interest rate, and time period (in months).
- Balance Update:
- After calculating the interest, the system updates the account balance by adding the interest earned.
- Formatted Output:
- The program displays the interest earned and the updated balance formatted to two decimal places for clarity.
- User Input Handling:
- Prompts the user to input necessary details for both savings and CD accounts.
- Ensures that user inputs are correctly used to perform calculations and update balances.

## Requirements

- Python 3.6 or later

## Setup

1. Clone this repository to your local machine:
    ```sh
    git clone https://github.com/sack2116/customer_banking.git
    ```
2. Navigate to the project directory:
    ```sh customer_banking
    cd customer_banking
    ```

## Usage

To run the Banking System, execute the following command in your terminal:
```sh
python customer_banking.py
```
1. Run the customer_banking.py file to start the program
2. Follow the prompts to enter the initial balance, interest rate, and number of months for both savings and CD accounts.
3. The program will calculate and display the interest earned and the updated account balances.

## Code Structure

* Account.py: Contains the Account class definition.
* savings_account.py: Contains the create_savings_account function.
* cd_account.py: Contains the create_cd_account function.
* customer_banking.py: Contains the main function to run the program.

## Example
Examples: For Savings Account

        >>> create_savings_account(1000.0, 5.0, 12)
        (1050.0, 50.0)

        >>> create_savings_account(500.0, 2.0, 6)
        (505.0, 5.0)

            : For CD Account

        >>> create_cd_account(1000.0, 5.0, 12)
        (1050.0, 50.0)

        >>> create_cd_account(2000.0, 3.0, 24)
        (2100.0, 100.0)
        
## PseudoCode

### Savings Account Setup

1. Import necessary classes and modules.
2. Define the Savings Account Function
3. Ask the user for the initial balance of the savings account.
4. Ask the user for the interest rate and the number of months.
5. Create a savings account with the provided balance and interest rate.
6. Calculate the interest earned based on the balance, interest rate, and months.
7. Update the balance by adding the interest earned.
8. Return the updated balance and the interest earned.

### CD Account Setup

1. Define the CD Account Function
2. Ask the user for the initial balance of the CD account.
3. Ask the user for the interest rate and the number of months.
4. Create a CD account with the provided balance and interest rate.
5. Calculate the interest earned based on the balance, interest rate, and months.
6. Update the balance by adding the interest earned.
7. Return the updated balance and the interest earned.

### Main Program Execution

1. Ask the user to enter details for the savings account:

Balance
Interest rate
Number of months

2. Call the savings account function with the entered details.
3. Display the interest earned and the updated balance, formatted to two decimal places.
4. Ask the user to enter details for the CD account:

Balance
Interest rate
Number of months

5. Call the CD account function with the entered details.
6. Display the interest earned and the updated balance, formatted to two decimal places.

## How it Works

1. Starting the Program:
* The program begins by importing necessary classes and modules.

2. Savings Account Function:
* The user provides the initial balance, interest rate, and number of months.
* An instance of the savings account is created using these parameters.
* The program calculates the interest earned over the specified number of months using the formula:
interest_earned = initial_balance * (interest_rate / 100) * (months / 12)
* The account balance is updated by adding the interest earned to the initial balance.
* The updated balance and interest earned are returned and displayed.

3. CD Account Function:
* The user provides the initial balance, interest rate, and number of months.
* An instance of the CD account is created with these details.
* The program calculates the interest earned similarly to the savings account function.
* The balance is updated by adding the calculated interest.
* The updated balance and interest earned are returned and displayed.

4. Main Program Execution:

* The user is prompted to enter the details for both savings and CD accounts.
* The corresponding functions are called to process these details.
* The results, including the interest earned and updated balances, are printed out in a user-friendly format.

5. Results:
* The program completes execution after displaying all necessary results.


