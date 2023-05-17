import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from solution import load_dataset
from merge_and_analyze_data import merge_and_analyze_data


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

    def test_merge_and_analyze_data(self):
        additional_data = pd.DataFrame({
            'product_id': [301, 402, 501],
            'product_name': ['Smartphone', 'T-Shirt', 'Garden Tool']
        })

        expected_merged_data = pd.merge(
            self.test_data.dropna(), additional_data, on='product_id')

        merged_data = merge_and_analyze_data(
            self.test_data.dropna(), additional_data, 'product_id')
        assert_frame_equal(merged_data, expected_merged_data)


if __name__ == "__main__":
    unittest.main()
