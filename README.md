# User-Prompts-Software-for-Loan-Qualifier
UC Fintech Bootcamp Challenge 2
Module 2 Challenge assignment for the UC Berkeley Fintech Bootcamp. 

In this challenge, I applied software-engineering best practices to add new features and enhancements to the loan qualifier application. 

Using the loan qualifier CLI, the tool prompts the user to save the results as a CSV file. 

If no qualifying loans exist, when prompting a user to save a file, then the program should notify the user and exit.

Given a list of qualifying loans, when I’m prompted to save the results, then I should be able to opt out of saving the file.

Given a list of qualifying loans, when I choose to save the loans, the tool should prompt for a file path to save the file.

Using the loan qualifier CLI, when I choose to save the loans, then the tool should save the results as a CSV file.

Structure
    App.py (load_bank_data, get_applicant_info, find_qualifying_loans, save_qualifying_loans, run, save_csv):
        Data:
            daily_rate_sheet.csv
        Utilized files/functions/libraries (file name & functions):
            Csv library
            Sys library
            Fire library
            Questionary library
            calculators.py (calculate_monthly_debt_ratio, calculate_loan_to_value_ratio)
            fileio.py (load_csv)
            Max_loan_size.py (filter_max_loan_size)
            Credit_score (filter_credit_score)
            Debt_to_income (filter_debt_to_income)
            Loan_to_value (filter_loan_to_value)
        Actions (broken out by file name and functions):
            -
