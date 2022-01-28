# Bring your packages onto the path
import sys, os
sys.path.append('../../')

# import csv_reader.py
import src.ports.adapters.csv_reader as csv_reader

TEST_FILEPATH = "./example-ga-report.csv"

openedCSV = csv_reader.open_csv(TEST_FILEPATH)

print(openedCSV)