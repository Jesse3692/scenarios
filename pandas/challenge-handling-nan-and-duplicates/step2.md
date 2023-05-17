# Handling Nan Values

Now that you better understand the dataset, the next step is to handle the missing values (NaNs). In this sub-challenge, you will be required to implement various strategies to deal with NaN values and decide which method is the most appropriate for each column.

## TODO

1. Determine the most appropriate method for handling NaN values in each column (e.g., fill with a constant value, interpolate, drop rows or columns, etc.).
2. Implement your chosen methods to handle NaN values for each column.
3. Verify that the NaN values have been handled correctly.

## Example

You can run the `handle_nan_values.py` file to verify the correctness of the code:

```zsh
# python3 handle_nan_values.py
#    transaction_id  customer_id  product_id  ... quantity   price  rating
# 0               1          101         301  ...        2  199.99    4.50
# 1               2          102         402  ...        1   49.99    4.25
# 2               3          101         501  ...        3   29.99    5.00
# 3               4          103         301  ...        1  199.99    3.50
```