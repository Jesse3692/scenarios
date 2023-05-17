# Handling Duplicate Data

Duplicate data can lead to incorrect analysis or biased results. In this sub-challenge, you will identify and handle any duplicate data present in the dataset.

## TODO

1. Identify any duplicate rows in the DataFrame.
2. Determine the most appropriate method for handling duplicate data (e.g., keep the first occurrence, drop duplicates based on specific criteria, etc.).
3. Implement your chosen method to handle duplicate data.
4. Verify that the duplicate data has been handled correctly.

## Example

You can run the `handle_duplicate_data.py` file to verify the correctness of the code:

```zsh
python3 handle_duplicate_data.py
# Output:
#    transaction_id  customer_id  product_id  ... quantity   price  rating
# 0               1          101         301  ...        2  199.99    4.50
# 1               2          102         402  ...        1   49.99    4.25
# 2               3          101         501  ...        3   29.99    5.00
# 3               4          103         301  ...        1  199.99    3.50
```