import numpy as np
import pandas as pd
from nojazz.pandas import (
    fill_between_valid,
    fill_time_series_nulls,
    realign_nonnull_data,
    realign_time_series_df,
)


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


def test_fill_time_series_nulls():
    df = pd.DataFrame(
        [
            [np.nan, 1, np.nan, np.nan, 1],
            [1, 1, np.nan, np.nan, 1],
            [np.nan, 1, np.nan, 1, np.nan],
        ],
    )

    expected = pd.DataFrame(
        [
            [np.nan, 1, 0, 0, 1],
            [1, 1, 0, 0, 1],
            [np.nan, 1, 0, 1, np.nan],
        ],
    ).astype(np.float64)
    result = fill_time_series_nulls(df)

    pd.testing.assert_frame_equal(expected, result)


class TestRealign:
    def test_move_to_front(self):
        series = pd.Series([np.nan, 0, 1, 2])

        expected = pd.Series([0, 1, 2, np.nan])
        result = realign_nonnull_data(series)

        pd.testing.assert_series_equal(expected, result)

    def test_all_valid(self):
        series = pd.Series([0, 1, 2, 3])

        expected = pd.Series([0, 1, 2, 3])
        result = realign_nonnull_data(series)

        pd.testing.assert_series_equal(expected, result)

    def test_none_valid(self):
        series = pd.Series([np.nan, np.nan, np.nan])

        expected = pd.Series([np.nan, np.nan, np.nan])
        result = realign_nonnull_data(series)

        pd.testing.assert_series_equal(expected, result)


def test_realign_time_series_df():
    df = pd.DataFrame(
        [
            [np.nan, np.nan, np.nan, 1],
            [np.nan, np.nan, 1, 1],
            [np.nan, 1, 1, 1],
            [1, 1, 1, 1],
        ]
    )

    expected = pd.DataFrame(
        [
            [1, np.nan, np.nan, np.nan],
            [1, 1, np.nan, np.nan],
            [1, 1, 1, np.nan],
            [1, 1, 1, 1],
        ]
    ).astype(np.float64)
    result = realign_time_series_df(df)

    pd.testing.assert_frame_equal(expected, result)
