# Exploring and Analyzing the Dataset

In this sub-challenge, you will explore the provided dataset to understand its structure, identify potential issues, and gather insights on handling the data. This is an important step in any data cleaning process, as it allows you to make informed decisions on how to handle missing or duplicate data.

## TODO

1. Load the dataset into a `pandas` DataFrame.
2. Display the first few rows of the DataFrame to get an understanding of its structure.
3. Use `pandas` functions to obtain summary statistics and identify any potential issues with the data, such as missing or duplicate values.
4. Determine the percentage of missing data in each column of the DataFrame.

Please complete the above functions in the `explore_and_analyze_data.py` file explore_and_analyze_data function.

## Example

You can run the `explore_and_analyze_data.py` file to verify the correctness of the code:

```zsh
python3 explore_and_analyze_data.py

# Output:
#    transaction_id  customer_id  product_id product_category transaction_date  quantity   price  rating
# 0               1          101         301      Electronics         2021/5/1         2  199.99     4.5
# 1               2          102         402          Apparel         2021/5/1         1   49.99     NaN
# 2               3          101         501    Home & Garden         2021/5/2         3   29.99     5.0
# 3               4          103         301      Electronics         2021/5/2         1  199.99     3.5
# 4               5          104         301      Electronics              NaN         1  199.99     4.0
#        transaction_id  customer_id  product_id   quantity       price    rating
# count        10.00000     10.00000   10.000000  10.000000   10.000000  9.000000
# mean          5.50000    102.80000  431.200000   1.800000  143.790000  4.277778
# std           3.02765      1.75119  141.767258   1.032796  149.595603  0.565194
# min           1.00000    101.00000  301.000000   1.000000   12.990000  3.500000
# 25%           3.25000    101.25000  301.000000   1.000000   32.490000  4.000000
# 50%           5.50000    102.50000  402.000000   1.500000  114.990000  4.500000
# 75%           7.75000    103.75000  501.000000   2.000000  199.990000  4.500000
# max          10.00000    106.00000  701.000000   4.000000  499.990000  5.000000
# transaction_id       0.0
# customer_id          0.0
# product_id           0.0
# product_category     0.0
# transaction_date    10.0
# quantity             0.0
# price                0.0
# rating              10.0
# dtype: float64
```
