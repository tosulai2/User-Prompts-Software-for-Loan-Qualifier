# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv

from pathlib import Path #added as part of the challenge Part 3 - Systems Design: Organize Code

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

"""
Moving this 'save_csv' function from app.py to here as part of the challenge Part 3 - Systems Design: Organize Code
"""
def save_csv(save_csv_csvpath, csvheader, csvdata):
    """"
    Saves a CSV file at path provided with the csv header and data provided
    In this challenge, this will save the qualifying loans from the 'qualifying_loans' dictionary to a CSV file 'save_csv_function_output.csv'

    Args:
        save_csv_csvpath (Path): The csv file path you want to save to.
        csvheader (List): A list of the headers you want to include in the csv file.
        csvdata (Dictionary): The data you want to add to the csv file

    Returns:
        None.
    """
    #save_csv_csvpath = Path("save_csv_function_output.csv") #placeholder for a filepath to save the csv file for this function
    #csvheader = ['Lender', 'Max Loan Amount', 'Max LTV', 'Max DTI', 'Min Credit', 'Interest Rate']

    with open(save_csv_csvpath, "w", newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        # Write the CSV Header columns
        csvwriter.writerow(csvheader) #[Lender, Max Loan Amount, Max LTV, Max DTI, Min Credit, Interest rate]

        # Write the data from 'qualifying_loans' dictionary
        for row in csvdata: #qualifying_loans
            csvwriter.writerow(row.values())
