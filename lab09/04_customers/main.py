# this function receve in input two lists and return the best customer name
def nameOfBestCustomer(sales, customers):
    if len(sales) != len(customers):
        return 'Error! sales and customers must have the same length'

    max_sale = max(sales)
    customer_index = sales.index(max_sale)
    best_customer = customers[customer_index]


    return best_customer



if __name__ == '__main__':
    print(nameOfBestCustomer([34, 65.8, 110], ['Dario', 'Marika', 'Mattia']))