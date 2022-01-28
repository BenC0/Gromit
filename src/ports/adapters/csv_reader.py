import pandas as pd

# Opens the CSV file specified by `path`
# `path` can be either relative or
# absolute filepath and must be a string
# returns a pandas dataframe
def open_csv(path):
    csv = pd.read_csv(path)
    return csv