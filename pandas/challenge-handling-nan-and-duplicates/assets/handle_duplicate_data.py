import pandas as pd

from solution import load_dataset
from explore_and_analyze_data import explore_and_analyze_data
from handle_nan_values import handle_nan_values


def handle_duplicate_data(df: pd.DataFrame) -> pd.DataFrame:
    """Handle duplicate data in the dataset using appropriate methods."""
    # Drop duplicate rows, keeping the first occurrence
    # TODO Complementary code
    
    return df


if __name__ == '__main__':
    file_path = "sales_data.csv"
    sales_data = load_dataset(file_path)
    missing_percentage = explore_and_analyze_data(sales_data)
    cleaned_data = handle_nan_values(sales_data)
    cleaned_data = handle_duplicate_data(cleaned_data)
    print(cleaned_data)
