import sys

sys.path.append("/home/labex/project")

import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from solution import load_dataset
from explore_and_analyze_data import explore_and_analyze_data


class TestPandasChallenge(unittest.TestCase):

    def setUp(self):
        self.test_data = pd.DataFrame({
            'transaction_id': [1, 2, 3, 4, 5],
            'customer_id': [101, 102, 101, 103, 104],
            'product_id': [301, 402, 501, 301, 301],
            'product_category': ['Electronics', 'Apparel', 'Home & Garden', 'Electronics', 'Electronics'],
            'transaction_date': ['2021-05-01', '2021-05-01', '2021-05-02', '2021-05-02', None],
            'quantity': [2, 1, 3, 1, 1],
            'price': [199.99, 49.99, 29.99, 199.99, 199.99],
            'rating': [4.5, None, 5.0, 3.5, 4.0]
        })

    def test_load_dataset(self):
        file_path = "test_data.csv"
        self.test_data.to_csv(file_path, index=False)
        loaded_data = load_dataset(file_path)
        assert_frame_equal(loaded_data, self.test_data)

    def test_explore_and_analyze_data(self):
        expected_missing_percentage = pd.Series(
            [0, 0, 0, 0, 20, 0, 0, 20], index=self.test_data.columns).astype(float)
        missing_percentage = explore_and_analyze_data(self.test_data)
        pd.testing.assert_series_equal(
            missing_percentage, expected_missing_percentage)


if __name__ == "__main__":
    unittest.main()
