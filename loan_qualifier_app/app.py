# -*- coding: utf-8 -*-
"""Loan Qualifier Application.

This is a command line application to match applicants with qualifying loans.
It follows some user prompts and then saves the qualified loans in a desired csv file path.

Example:
    $ python app.py
    ? Enter a file path to a rate-sheet (.csv): ./data/daily_rate_sheet.csv
    ? What's your credit score? 780
    ? What's your current amount of monthly debt? 1000
    ? What's your total monthly income? 100000
    ? What's your desired loan amount? 200000
    ? What's your home value? 1000000
    The monthly debt to income ratio is 0.01
    The loan to value ratio is 0.20.
    Found 17 qualifying loans
    ? Do you want to save the qualifying loans to a csv file? (Yes or No) Yes
    ? Nice! What's the path you want to save this to? (Type in with .csv at the end) test1.csv
    Perfect! It saved the file to: test1.csv

    Output =>
    Lender	Max Loan Amount	Max LTV	Max DTI	Min Credit	Interest Rate
    Bank of Big - Premier Option	300000	0.85	0.47	740	3.6
    West Central Credit Union - Premier Option	400000	0.9	0.35	760	2.7
    FHA Fannie Mae - Premier Option	500000	0.9	0.47	780	3.6
    Bank of Fintech - Premier Option	300000	0.9	0.47	740	3.15
    iBank - Premier Option	500000	0.85	0.46	780	3.15
    Goldman MBS - Premier Option	500000	0.8	0.4	770	3.6
    Citi MBS - Premier Option	400000	0.9	0.47	780	3.6
    Prosper MBS - Premier Option	400000	0.85	0.42	750	3.45
    Developers Credit Union - Premier Option	300000	0.85	0.47	770	3.45
    Bank of Big - Starter Plus	300000	0.85	0.39	700	4.35
    West Central Credit Union - Starter Plus	300000	0.8	0.44	650	3.9
    FHA Fredie Mac - Starter Plus	300000	0.85	0.45	550	4.35
    FHA Fannie Mae - Starter Plus	200000	0.9	0.37	630	4.2
    General MBS Partners - Starter Plus	300000	0.85	0.36	670	4.05
    iBank - Starter Plus	300000	0.9	0.4	620	3.9
    Citi MBS - Starter Plus	300000	0.8	0.39	740	4.05
    Developers Credit Union - Starter Plus	200000	0.85	0.46	640	4.2
"""
import csv

import sys
import fire #make sure to install the Python Fire library
import questionary #make sure to install the Python Questionary library
from pathlib import Path

from qualifier.utils.fileio import load_csv
from qualifier.utils.fileio import save_csv #added for Part 3 - Systems Design: Organize Code

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value

"""
Moving this 'save_csv' function below to fileio.py here as part of the challenge Part 3 - Systems Design: Organize Code
"""
# def save_csv():
#     """"
#     Saves the qualifying loans from the 'qualifying_loans' dictionary to a CSV file 'save_csv_function_output.csv'

#     Args:
#         None.

#     Returns:
#         None.
#     """
#     save_csv_csvpath = Path("save_csv_function_output.csv") #placeholder for a filepath to save the csv file for this function

#     with open(save_csv_csvpath, "w", newline='') as csvfile:
#         csvwriter = csv.writer(csvfile)

#         # Write the CSV Header columns: Lender, Max Loan Amount, Max LTV, Max DTI, Min Credit, Interest rate
#         header = ['Lender', 'Max Loan Amount', 'Max LTV', 'Max DTI', 'Min Credit', 'Interest Rate']
#         csvwriter.writerow(header)

#         # Write the data from 'qualifying_loans' dictionary
#         for row in qualifying_loans:
#             csvwriter.writerow(row.values())
#     return


def load_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file.

    Returns:
        The bank data from the data rate sheet CSV file.
    """

    csvpath = questionary.text("Enter a file path to a rate-sheet (.csv):").ask()
    csvpath = Path(csvpath)
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

    return load_csv(csvpath)


def get_applicant_info():
    """Prompt dialog to get the applicant's financial information.

    Returns:
        Returns the applicant's financial information.
    """

    credit_score = questionary.text("What's your credit score?").ask()
    debt = questionary.text("What's your current amount of monthly debt?").ask()
    income = questionary.text("What's your total monthly income?").ask()
    loan_amount = questionary.text("What's your desired loan amount?").ask()
    home_value = questionary.text("What's your home value?").ask()

    credit_score = int(credit_score)
    debt = float(debt)
    income = float(income)
    loan_amount = float(loan_amount)
    home_value = float(home_value)

    return credit_score, debt, income, loan_amount, home_value


def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
    """Determine which loans the user qualifies for.

    Loan qualification criteria is based on:
        - Credit Score
        - Loan Size
        - Debit to Income ratio (calculated)
        - Loan to Value ratio (calculated)

    Args:
        bank_data (list): A list of bank data.
        credit_score (int): The applicant's current credit score.
        debt (float): The applicant's total monthly debt payments.
        income (float): The applicant's total monthly income.
        loan (float): The total loan amount applied for.
        home_value (float): The estimated home value.

    Returns:
        A list of the banks willing to underwrite the loan.

    """

    # Calculate the monthly debt ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

    # Calculate loan to value ratio
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

    # Run qualification filters
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    print(f"Found {len(bank_data_filtered)} qualifying loans")

    return bank_data_filtered


def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.
    First asks if the user wants to save a CSV file
    If user types in yes then it asks for a file path they want to save it to
    If they provide a path, it saves it to the user inputed file path and prints 

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    # YOUR CODE HERE!
    #save the confirmation condition as a True or False value
    save_confirmation = questionary.confirm("Do you want to save the qualifying loans to a csv file?").ask()
    
    if save_confirmation: #if user said Yes i.e. True
        #Asks user where they want to save the file if they said yes
        csvpath = questionary.text("Nice! What's the path you want to save this to? (Type in with .csv at the end)").ask()
        save_csv_csvpath = Path(csvpath) #placeholder for a filepath to save the csv file for this function
        
        #include the csv header [Lender, Max Loan Amount, Max LTV, Max DTI, Min Credit, Interest rate]
        csvheader = ['Lender', 'Max Loan Amount', 'Max LTV', 'Max DTI', 'Min Credit', 'Interest Rate']
        save_csv(save_csv_csvpath, csvheader, qualifying_loans) 
        print(f"Perfect! It saved the file to: {csvpath}")



def run():
    """The main function for running the script."""

    # Load the latest Bank data
    bank_data = load_bank_data()

    # Get the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    # Find qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

    # Save qualifying loans
    save_qualifying_loans(qualifying_loans)


if __name__ == "__main__":
    fire.Fire(run)
