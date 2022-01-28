import pandas as pd

# Parses a Pandas dataframe
# and returns `dimension`
# 
# `df` must be a Pandas dataframe
# 
# `dimension` - a dictionary with
# the name and values of each dimension.
# A dimension is a descriptive
# attribute or characteristic of
# data, usually categorical in nature
# 
# GROUND TRUTH - The dimension is _always_
# in the first column 
def parse_dimension(df):
    return {
        "name": df.columns[0],
        "values": list(df[df.columns[0]].values)
    }

# Parse a Pandas dataframe
# and returns `divisor`
# 
# `df` must be a Pandas dataframe
# 
# `divisor` - a dictionary with the
# name and values of each divisor.
# The divisor is the value a metric
# is divided by to find the metric rate
# 
# GROUND TRUTH - The divisor is _always_
# in the second column
def parse_divisor(df):
    return {
        "name": df.columns[1],
        "values": list(df[df.columns[1]].values)
    }