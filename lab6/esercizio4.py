# Scrivete una funzione che calcoli il saldo di un conto bancario accreditando gli interessi annualmente. La funzione ricevecome parametri il numero di anni, il saldo iniziale e il tasso d’interesse annuo.


def balance_interests(b, y, i):
    return b*(1+i)**y


current_balance = float(input("Inserisci il tuo attuale saldo bancario: "))
years_num = float(input("Per quanti anni lascerai questo saldo in banca? "))
interest_rate = float(input("Inserisci il tuo tasso di interesse annuo: "))

print("Tra", years_num, "anni sul tuo conto bancario avrai", balance_interests(current_balance, years_num, interest_rate))