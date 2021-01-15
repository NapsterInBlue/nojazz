import pandas as pd


def fill_between_valid(series: pd.Series, value=0):
    """
    Finds the first and last valid (non-null) values in
    a Series and fills all NULL values with `value`
    """
    series = series.copy()

    first_valid = series.first_valid_index()
    last_valid = series.last_valid_index()

    series.loc[first_valid : last_valid + 1] = series[
        first_valid : last_valid + 1
    ].fillna(value)
    return series