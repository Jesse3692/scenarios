# Merging and Analyzing Cleaned Data

Now that you have cleaned the dataset by handling NaN values and duplicate data, you will merge the cleaned dataset with another dataset to analyze the combined data. This sub-challenge will test your ability to manipulate and merge data from different sources.

## TODO

1. Load the second dataset into a `pandas` DataFrame.
2. Merge the cleaned dataset from Sub-Challenge 3 with the new DataFrame based on a common key.
3. Perform a brief analysis of the merged dataset to extract insights or answer specific questions.

Please complete the above functions in the `merge_and_analyze_data.py` file merge_and_analyze_data function.

## Example

You can run the `merge_and_analyze_data.py` file to verify the correctness of the code:

```zsh
python3 merge_and_analyze_data.py

# Output:
product_category
Apparel          3
Electronics      4
Home & Garden    7
Name: quantity, dtype: int64
   transaction_id  customer_id  product_id product_category transaction_date  quantity   price    rating product_name
0               1          101         301      Electronics         2021/5/1         2  199.99  4.500000   Smartphone
1               4          103         301      Electronics         2021/5/2         1  199.99  3.500000   Smartphone
2              10          106         301      Electronics         2021/5/7         1  179.99  4.500000   Smartphone
3               2          102         402          Apparel         2021/5/1         1   49.99  4.277778      T-Shirt
4               9          101         402          Apparel         2021/5/6         2   39.99  4.000000      T-Shirt
5               3          101         501    Home & Garden         2021/5/2         3   29.99  5.000000  Garden Tool
6               7          105         501    Home & Garden         2021/5/4         4   24.99  3.500000  Garden Tool
```
