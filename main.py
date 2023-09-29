"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load, myload
from mylib.query import query, myquery

def main():
    # Extract
    print("Extracting data...")
    extract()

    # Transform and load
    print("Transforming data...")
    load()
    myload()
    # Query
    print("Querying data...")
    print("Printing first 5 rows of the GroceryDB table:\n")
    print(
        "..............................................."
        ".................................................."
        ".............................."
    )
    print(query())
    print(
        "..............................................."
        ".................................................."
        "..............................\n"
    )
    print("Printing Top Sales by category from MysalesDB table:\n")
    print(myquery())
    return "Success"

if __name__ == "__main__":
    main()