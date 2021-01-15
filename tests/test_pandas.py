import pandas as pd
import numpy as np

from nojazz.pandas import fill_between_valid


class TestFillBetween:
    def test_leading_null(self):
        series = pd.Series([np.nan, 0, np.nan, 2])

        expected = pd.Series([np.nan, 0, 0, 2])
        result = fill_between_valid(series)

        pd.testing.assert_series_equal(expected, result)

    def test_trailing_null(self):
        series = pd.Series([0, np.nan, 2, np.nan])

        expected = pd.Series([0, 0, 2, np.nan])
        result = fill_between_valid(series)

        pd.testing.assert_series_equal(expected, result)