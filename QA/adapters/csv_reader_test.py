# Bring your packages onto the path
import sys, os
sys.path.append('../../')

# import csv_reader.py
import src.ports.adapters.csv_reader as csv_reader

REL_TEST_FILEPATH = "./example-ga-export.csv"
ABS_TEST_FILEPATH = os.path.abspath(REL_TEST_FILEPATH)

openedCSV = csv_reader.open_csv(ABS_TEST_FILEPATH)

print(openedCSV)