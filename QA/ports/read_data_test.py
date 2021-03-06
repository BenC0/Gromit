# Bring your packages onto the path
from asyncore import read
import sys, os
sys.path.append('../../')

# import csv_reader & read_data
import src.ports.adapters.csv_reader as csv_reader
import src.ports.read_data as read_data

REL_TEST_FILEPATH = "../test_files/example-ga-export.csv"
ABS_TEST_FILEPATH = os.path.abspath(REL_TEST_FILEPATH)

df = csv_reader.open_csv(ABS_TEST_FILEPATH)
parsed_df = read_data.parse_df(df)
print(parsed_df)