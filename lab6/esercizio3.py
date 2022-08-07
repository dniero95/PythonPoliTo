# Un’organizzazione non governativa ha bisogno di un programma per calcolare la quota di sussidio economico da assegnare a ciascuna famiglia bisognosa di assistenza. La formula è la seguente:
#     •Se il reddito annuo della famiglia è compreso tra $ 30 000 e $ 40 000 e la famiglia ha almeno tre figli, il sussidio è pari a $ 1000 per ogni figlio.
    
#     •Se il reddito annuo della famiglia è compreso tra $ 20 000 e $ 30 000 e la famiglia ha almeno due figli, il sussidio è pari a $ 1500 per ogni figlio.
    
#     •Se il reddito annuo della famiglia è minore di $ 20 000, il sussidio è pari a $ 2000 per ogni figlio.
    
# Scrivete una funzione che faccia questi calcoli, poi scrivete un programma che in un ciclo chieda all’utente di fornire il reddito annuo e il numero di figli di ciascuna famiglia richiedente il sussidio, visualizzando il valore corrispondentemente restituito dalla funzione. Usate –1 come valore sentinella per terminare l’immissione dei dati.

def economic_subsidy_children_income(child_num, income_value):
    if 30000 <= income_value <= 40000 and child_num >= 3:
        return "$ " + str(1000*child_num)
    elif 20000 <= income_value < 30000 and child_num >= 2:
        return "$ " + str(1500*child_num)
    elif 20000 > income_value:
        return "$ " + str(2000*child_num)

    # Se il reddito annuo della famiglia è compreso tra $ 30 000 e $ 40 000 e la famiglia ha almeno tre figli



while True:
    child_num = int(input("Inserire il numero di figli: "))
    income_value = int(input("Inserire il proprio reddito annuo: "))
    print("Riceverà un sussidio economico di", economic_subsidy_children_income(child_num, income_value))
    escape = int(input("Inserire -1 per uscire o qualsiasi altro numero per continuare: "))
    if escape == -1:
        break
