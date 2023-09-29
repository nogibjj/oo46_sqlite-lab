"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,avg_FPro_products,avg_distance_root,
ingred_normalization_term,semantic_tree_name,semantic_tree_node
"""
import sqlite3
import csv


# load the csv file and insert into a new sqlite3 database
def load(dataset="mylib/data/GroceryDB_IgFPro.csv"):
    """ "Transforms and Loads data into the local SQLite3 database"""

    # print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    conn = sqlite3.connect("GroceryDB.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS GroceryDB")
    c.execute(
        "CREATE TABLE GroceryDB (id,general_name, count_products, ingred_FPro,"
        "avg_FPro_products, avg_distance_root, ingred_normalization_term,"
        "semantic_tree_name, semantic_tree_node)"
    )
    # insert
    c.executemany("INSERT INTO GroceryDB VALUES (?,?, ?, ?, ?, ?, ?, ?, ?)", payload)
    conn.commit()
    conn.close()
    return "GroceryDB.db"


def myload(dataset="mylib/data/sales.csv"):
    """ "Transforms and Loads data into the local SQLite3 database"""

    # print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    conn = sqlite3.connect("GroceryDB.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS MysalesDB")
    c.execute(
        "CREATE TABLE MysalesDB (id, sale_id, emp_id, item_name,"
        "quantity, per, unit_price,total_amount,"
        "sales_date, no, c_name, s_name, teller)"
    )
    # insert
    c.executemany(
        "INSERT INTO MysalesDB VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", payload
    )
    conn.commit()
    conn.close()
    return "GroceryDB.db"
