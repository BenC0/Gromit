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

# Parse a Pandas dataframe
# and returns `metric`
# 
# `df` must be a Pandas dataframe
# 
# `metric` - a dictionary with the
# name and values of the metric.
# The metrics are the values we are
# specifically analysing in this table
# 
# GROUND TRUTH - The metric is _always_
# in the third column
def parse_metric(df):
    return {
        "name": df.columns[2],
        "values": list(df[df.columns[2]].values)
    }

# Parse a Pandas dataframe
# and returns `metric_rate`
# 
# `df` must be a Pandas dataframe
# 
# `metric_rate` - a dictionary with the
# name and values of the metric rate.
# The metric rate is the value result of
# the metric values divided by the
# divisor values
# 
# GROUND TRUTH - The metric rate is
# _always_ in the fourth column
def parse_metric_rate(df):
    return {
        "name": df.columns[3],
        "values": list(df[df.columns[3]].values)
    }

# Parse a Pandas dataframe and
# returns the shape in a more
# explicit & legible manner.
# 
# GROUND TRUTH 1 - The row number is
# always the first element in the tuple
# 
# GROUND TRUTH 2 - The column number is
# always the second element in the tuple
def parse_shape(df):
    return {
        "rows": df.shape[0],
        "columns": df.shape[1]
    }

# Parse a Pandas dataframe and returns
# dictionary of `dimensions`, `divisor`,
# `metric`, `metric_rate`, `shape`
def parse_df(df):
    return {
        "shape": parse_shape(df),
        "dimension": parse_dimension(df),
        "divisor": parse_divisor(df),
        "metric": parse_metric(df),
        "metric_rate": parse_metric_rate(df),
    }