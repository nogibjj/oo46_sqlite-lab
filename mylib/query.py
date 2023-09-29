"""Query the database"""

import sqlite3
import pandas as pd


def query():
    """Query the database for the top 5 rows of the GroceryDB table"""
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    query = "SELECT * FROM GroceryDB LIMIT 6"
    cursor.execute(query)
    print("Printing first 5 rows of the GroceryDB table:")
    top_5 = pd.DataFrame(cursor.fetchall())
    top_5.columns = [
        "id",
        "general_name",
        "count_products",
        "ingred_FPro",
        "avg_FPro_products",
        "avg_distance_root",
        "ingred_normalization_term",
        "semantic_tree_name",
        "semantic_tree_node",
    ]
    top_5 = top_5.set_index("id")
    top_5 = top_5.drop(columns=["semantic_tree_name", "semantic_tree_node"])
    conn.close()
    return top_5


def myquery():
    """Query the database for sales by category of the GroceryDB table"""
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    query = "SELECT c_name AS Category, SUM(total_amount)AS Amount_Sold" + \
    " FROM MysalesDB GROUP BY c_name ORDER BY Amount_Sold DESC LIMIT 6"
    cursor.execute(query)
   
    top_5 = pd.DataFrame(cursor.fetchall())
    top_5.columns = ["Product Category", "Amount Sold"]
   
    conn.close()
    return top_5
