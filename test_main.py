"""
Test goes here

"""
from mylib.query import myquery, query
from mylib.transform_load import myload, load
from mylib.extract import extract
from main import main
import unittest


# load the data
query_1 = query()
query_2 = myquery()

# test the data
class TestMain(unittest.TestCase):
    def test_col_exist(self):
        message = "column names does not exist"
        # assert if columns exist
        assert {"Product Category", "Amount Sold"}.issubset(query_2.columns), message
        # assert if columns exist
        assert {
            "general_name",
            "count_products",
            "ingred_FPro",
            "avg_FPro_products",
            "avg_distance_root",
            "ingred_normalization_term",
        }.issubset(query_1.columns), message

    def test_sqlite_load(self):
        # assert if the database is loaded
        self.assertEqual(myload(), "GroceryDB.db")
        self.assertEqual(load(), "GroceryDB.db")

    def test_extract(self):
        # assert if the data is extracted
        self.assertEqual(extract(), "mylib/data/GroceryDB_IgFPro.csv")

    def test_main(self):
        # assert if the main function is running
        self.assertEqual(main(), "Success")

if __name__ == "__main__":
    unittest.main()
