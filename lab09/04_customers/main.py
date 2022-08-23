# this function receives in input two lists and return the best customer name
def nameOfBestCustomer(sales, customers):
    if len(sales) != len(customers):
        return 'Error! sales and customers must have the same length'

    max_sale = max(sales)
    customer_index = sales.index(max_sale)
    best_customer = customers[customer_index]


    return best_customer



if __name__ == '__main__':

    sales = []
    customers = []
    while True:
        sales.append(float(input('Customer sale: ')))
        if sales[-1] == 0:
            sales.pop(-1)
            break
        customers.append(input('Customer name: '))


    print(nameOfBestCustomer(sales, customers))