# Bring your packages onto the path
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'src')))

# Now do your import
import src.ports.adapters.csv_reader as csv_reader

TEST_FILEPATH = "./example-ga-report.csv"

openedCSV = csv_reader.open_csv(TEST_FILEPATH)

print(openedCSV)