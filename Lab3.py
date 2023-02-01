from sys import argv, exit
import os
from datetime import date
import pandas as pd

def main():
    sales_csv = get_sales_csv()
    oders_dir = create_orders_dir(sales_csv)
    proccess_sales_data(sales_csv, oders_dir)
    return

def get_sales_csv():
    num_params = len(argv) - 1
    if num_params >= 1:
        sales_csv = argv[1]
        if os.path.isfile(sales_csv):
            return sales_csv
        else: 
            print("Error: Invalid path to sales data csv file")
            exit(1)
    else:
        print("Error: Missing path to sales data csv file")
        exit(1)

def create_orders_dir(sales_csv):
    sales_dir = os.path.dirname(os.path.abspath(sales_csv))
    todays_date = date.today().isoformat
    orders_dir = os.path.join(sales_dir, f"Orders_{todays_date}")
    if os.path.isdir(orders_dir):
        os.makedirs(orders_dir)
    return

def proccess_sales_data(sales_csv, orders_dir):
    sales_df = pd.read_csv(sales_csv)
    sales_df.insert(7, "TOTAL PRICE",sales_df["ITEM QUANTITY"] * sales_df["ITEM PRICE"]) 
    return

if __name__ == '__main__':
    main()