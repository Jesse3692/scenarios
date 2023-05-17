import pandas as pd

from solution import load_dataset


def handle_nan_values(df: pd.DataFrame) -> pd.DataFrame:
    """Handle missing values (NaNs) in the dataset using appropriate methods."""
    # Fill missing values in 'rating' column with the mean rating
    df['rating'].fillna(df['rating'].mean(), inplace=True)

    # Drop rows with missing values in 'transaction_date' column
    df.dropna(subset=['transaction_date'], inplace=True)

    return df


if __name__ == "__main__":
    file_path = "sales_data.csv"
    sales_data = load_dataset(file_path)
    cleaned_data = handle_nan_values(sales_data)
    print(cleaned_data)
