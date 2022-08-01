if __name__ == '__main__':
    books_number = int(input('Inserire il numero di libri: '))
    books_price = int(input('Inserire il prezzo totale:'))

    tax_amount = books_price * 0.075
    delivery_expenses = books_number * 2

    total_price = books_price + tax_amount + delivery_expenses

    print(f"Costo totale dell'ordine: {total_price}")


