# Handling Duplicate Data

Duplicate data can lead to incorrect analysis or biased results. In this sub-challenge, you will identify and handle any duplicate data present in the dataset.

## TODO

1. Identify any duplicate rows in the DataFrame.
2. Determine the most appropriate method for handling duplicate data (e.g., keep the first occurrence, drop duplicates based on specific criteria, etc.).
3. Implement your chosen method to handle duplicate data.
4. Verify that the duplicate data has been handled correctly.

Please complete the above functions in the `handle_duplicate_data.py` file handle_duplicate_data function.

## Example

You can run the `handle_duplicate_data.py` file to verify the correctness of the code:

```zsh
python3 handle_duplicate_data.py

# Output:
#    transaction_id  customer_id  product_id product_category transaction_date  quantity   price    rating
# 0               1          101         301      Electronics         2021/5/1         2  199.99  4.500000
# 1               2          102         402          Apparel         2021/5/1         1   49.99  4.277778
# 2               3          101         501    Home & Garden         2021/5/2         3   29.99  5.000000
# 3               4          103         301      Electronics         2021/5/2         1  199.99  3.500000
# 5               6          102         601           Beauty         2021/5/3         2   12.99  4.500000
# 6               7          105         501    Home & Garden         2021/5/4         4   24.99  3.500000
# 7               8          103         701        Furniture         2021/5/5         1  499.99  5.000000
# 8               9          101         402          Apparel         2021/5/6         2   39.99  4.000000
# 9              10          106         301      Electronics         2021/5/7         1  179.99  4.500000
```
