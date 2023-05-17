# Merging and Analyzing Cleaned Data

Now that you have cleaned the dataset by handling NaN values and duplicate data, you will merge the cleaned dataset with another dataset to analyze the combined data. This sub-challenge will test your ability to manipulate and merge data from different sources.

## TODO

1. Load the second dataset into a pandas DataFrame.
2. Merge the cleaned dataset from Sub-Challenge 3 with the new DataFrame based on a common key.
3. Perform a brief analysis of the merged dataset to extract insights or answer specific questions.

## Example

You can run the `merge_and_analyze_data.py` file to verify the correctness of the code:

```zsh
python3 merge_and_analyze_data.py
# Output:
#    transaction_id  customer_id  product_id  ...   price rating  product_name
# 0               1          101         301  ...  199.99   4.50    Smartphone
# 1               4          103         301  ...  199.99   3.50    Smartphone
# 2               2          102         402  ...   49.99   4.25       T-Shirt
# 3               3          101         501  ...   29.99   5.00   Garden Tool
```