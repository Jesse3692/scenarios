from typing import Dict, Any
import numpy as np


def customer_stats(transactions: np.ndarray) -> Dict[str, Any]:
    """
    Calculates statistics about customer transactions.

    Parameters
    ----------
    transactions : np.ndarray
        A 2D NumPy array of shape (num_customers, num_products) representing the number of purchases of each product by each customer.

    Returns
    -------
    Dict[str, Any]
        A dictionary containing the following keys and values:
            'total_purchases_by_customer': np.ndarray
                A 1D NumPy array of shape (num_customers,) containing the total number of purchases for each customer.
            'total_purchases_by_product': np.ndarray
                A 1D NumPy array of shape (num_products,) containing the total number of purchases for each product.
            'total_revenue_by_customer': np.ndarray
                A 1D NumPy array of shape (num_customers,) containing the total revenue generated by each customer.
            'total_revenue_by_product': np.ndarray
                A 1D NumPy array of shape (num_products,) containing the total revenue generated by each product.
            'average_purchases_per_customer': float
                The average number of purchases per customer.
            'average_purchases_per_product': float
                The average number of purchases per product.
    """
    num_customers, num_products = transactions.shape

    # Calculate the total number of purchases for each customer and product
    total_purchases_by_customer, total_purchases_by_product = None

    # Calculate the total revenue generated by each customer and product
    total_revenue_by_customer, total_revenue_by_product = None

    # Calculate the average number of purchases per customer and product
    average_purchases_per_customer = None
    average_purchases_per_product = None

    # TODO: Round all values to 2 decimal places

    return {
        "total_purchases_by_customer": total_purchases_by_customer,
        "total_purchases_by_product": total_purchases_by_product,
        "total_revenue_by_customer": total_revenue_by_customer,
        "total_revenue_by_product": total_revenue_by_product,
        "average_purchases_per_customer": average_purchases_per_customer,
        "average_purchases_per_product": average_purchases_per_product,
    }
