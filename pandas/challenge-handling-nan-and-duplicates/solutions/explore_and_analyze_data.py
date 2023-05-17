import pandas as pd
from typing import Tuple
from solution import load_dataset


def explore_and_analyze_data(df: pd.DataFrame) -> Tuple[float]:
    """Explore and analyze the dataset to obtain summary statistics and identify missing and duplicate values."""
    # Display first few rows
    print(df.head())

    # Obtain summary statistics
    print(df.describe())

    # Identify missing and duplicate values
    missing_values = df.isnull().sum()
    duplicate_values = df.duplicated().sum()

    # Determine percentage of missing data in each column
    missing_percentage = (missing_values / len(df)) * 100
    print(missing_percentage)

    return missing_percentage


if __name__ == '__main__':
    file_path = "sales_data.csv"
    sales_data = load_dataset(file_path)
    missing_percentage = explore_and_analyze_data(sales_data)
    print(missing_percentage)
