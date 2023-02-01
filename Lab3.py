from sys import argv, exit
import os



def main():
    sales_csv = get_sales_csv()
    oders_dir = create_orders_dir(sales_csv)

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
    sales_dir = os.path.dirname(sales_csv)
    
    return

def proccess_sales_data():
    return

if __name__ == '__main__':
    main()