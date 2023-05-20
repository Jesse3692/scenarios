import sys

sys.path.append("/home/labex/project")

import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from load_dataset import load_dataset
from handle_nan_values import handle_nan_values


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

    def test_handle_nan_values(self):
        expected_cleaned_data = self.test_data.copy()
        expected_cleaned_data['rating'].fillna(4.25, inplace=True)
        expected_cleaned_data.dropna(subset=['transaction_date'], inplace=True)

        cleaned_data = handle_nan_values(self.test_data.copy())
        assert_frame_equal(cleaned_data, expected_cleaned_data)


if __name__ == "__main__":
    unittest.main()
