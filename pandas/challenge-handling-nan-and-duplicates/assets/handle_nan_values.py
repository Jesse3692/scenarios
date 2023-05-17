import pandas as pd

from solution import load_dataset


def handle_nan_values(df: pd.DataFrame) -> pd.DataFrame:
    """Handle missing values (NaNs) in the dataset using appropriate methods."""
    # Fill missing values in 'rating' column with the mean rating
    # TODO Complementary code

    # Drop rows with missing values in 'transaction_date' column
    # TODO Complementary code

    return df


if __name__ == "__main__":
    file_path = "sales_data.csv"
    sales_data = load_dataset(file_path)
    missing_percentage = handle_nan_values(sales_data)
    print(missing_percentage)
