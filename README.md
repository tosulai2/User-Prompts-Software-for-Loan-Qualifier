# User-Prompts-Software-for-Loan-Qualifier

UC Fintech Bootcamp Challenge 2
Module 2 Challenge assignment for the UC Berkeley Fintech Bootcamp. 

In this challenge, I applied software-engineering best practices to add new features and enhancements to the loan qualifier application. 

Using the loan qualifier CLI, the tool prompts the user to save the results as a CSV file. 

If no qualifying loans exist, when prompting a user to save a file, then the program should notify the user and exit.

Given a list of qualifying loans, when I’m prompted to save the results, then I should be able to opt out of saving the file.

Given a list of qualifying loans, when I choose to save the loans, the tool should prompt for a file path to save the file.

Using the loan qualifier CLI, when I choose to save the loans, then the tool should save the results as a CSV file.

---

## Technologies

This project uses Python programming language, user prompts in the command line interface, the libraries and functions in the below file structure, and Windows OS. 

File Structure
    App.py (load_bank_data, get_applicant_info, find_qualifying_loans, save_qualifying_loans, run):
        Data:
            daily_rate_sheet.csv
        Utilized files/functions/libraries (file name & functions):
            Csv library
            Sys library
            Fire library
            Questionary library
            calculators.py (calculate_monthly_debt_ratio, calculate_loan_to_value_ratio)
            fileio.py (load_csv, save_csv)
            Max_loan_size.py (filter_max_loan_size)
            Credit_score (filter_credit_score)
            Debt_to_income (filter_debt_to_income)
            Loan_to_value (filter_loan_to_value)
        Actions (broken out by file name and functions):
            -

---

## Installation Guide

Make sure to install Fire and Questionary on any device that uses this code using the following commands

pip install fire

pip install questionary

---

## Usage

Example 1: 
If you run the code and input the user prompts / loan criteria as in the below input, you will get the test1.csv file in the folder with the following output

Input/Prompt =>
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


Example 2: 
If you run the code and input the user prompts / loan criteria as in the below input, you will get the test2.csv file in the folder with the following output

Input/Prompt =>
$ python app.py
? Enter a file path to a rate-sheet (.csv): ./data/daily_rate_sheet.csv
? What's your credit score? 780
? What's your current amount of monthly debt? 1000
? What's your total monthly income? 100000
? What's your desired loan amount? 200000
? What's your home value? 230000
The monthly debt to income ratio is 0.01
The loan to value ratio is 0.87.
Found 6 qualifying loans
? Do you want to save the qualifying loans to a csv file? Yes
? Nice! What's the path you want to save this to? (Type in with .csv at the end) test2.csv
Perfect! It saved the file to: test2.csv

Output =>
Lender	Max Loan Amount	Max LTV	Max DTI	Min Credit	Interest Rate
West Central Credit Union - Premier Option	400000	0.9	0.35	760	2.7
FHA Fannie Mae - Premier Option	500000	0.9	0.47	780	3.6
Bank of Fintech - Premier Option	300000	0.9	0.47	740	3.15
Citi MBS - Premier Option	400000	0.9	0.47	780	3.6
FHA Fannie Mae - Starter Plus	200000	0.9	0.37	630	4.2
iBank - Starter Plus	300000	0.9	0.4	620	3.9

---

## Contributors

Name: Taofik Sulaiman | Phone: 2407162877 | Email: taofik.sulaiman@gmail.com | Linkedin: https://linkedin.com/in/taofik-sulaiman | Twitter: https://twitter.com/taofik_smk


---

## License

OpenSource License, feel free to use as needed but make sure to givce me credit and contact me to let me know the cool ways you used this. 
I obtained portions of this code via the University of California BerekelY Fintech Bootcamp curated by Trilogy U Edcuation



