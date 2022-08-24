if __name__ == '__main__':
    opening_balance = 1000
    INTEREST_RATE = 0.05

    first_year_balance = opening_balance * INTEREST_RATE + opening_balance
    second_year_balance = first_year_balance * INTEREST_RATE + first_year_balance
    third_yaar_balance = second_year_balance * INTEREST_RATE + second_year_balance

    print(f'''Saldo Iniziale: {opening_balance:.2f}\n
              \rSaldo Primo Anno: {first_year_balance:.2f}
              \rSaldo Secondo Anno: {second_year_balance:.2f}
              \rSaldo Terzo Anno: {third_yaar_balance:.2f}''')