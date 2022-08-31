from order import Coffe_order

if __name__ == '__main__':
    order = Coffe_order(int(input('Numero di kg di caffè: ')))
    print(f'Ordine:\nCosto caffè: {order.calc_total_coffee_price()}\nNumero cartoni:\n{order.calc_number_of_box()}\nCosto totale: {order.calc_total_order_price()}')