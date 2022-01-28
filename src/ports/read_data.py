import pandas as pd

# Parses a Pandas dataframe
# and returns `dimensions`
# 
# `df` must be a Pandas dataframe
# 
# `dimensions` - an array of each
# dimension. A dimension is a descriptive
# attribute or characteristic of
# data, usually categorical in nature
# 
# GROUND TRUTH - The dimension is _always_
# in the first column 
def parse_dimensions(df):
    return {
        "name": df.columns[0],
        "values": list(df[df.columns[0]].values)
    }