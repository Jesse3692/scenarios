import pandas as pd


def load_dataset(file_path: str) -> pd.DataFrame:
    """Load dataset from a CSV file into a pandas DataFrame."""
    return pd.read_csv(file_path)
