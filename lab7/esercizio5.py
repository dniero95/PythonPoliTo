# Leggere una sequenza di numeri interi conclusa da una riga vuota.Stampare la posizione dei massimi locali (numeri maggiori sia del valore precedente che di quello successivo) se ce ne sono, altrimenti stampare il messaggio “Non ci sono massimi locali

sequence = []

while True:
    temp = input("Inserisci un numero intero (premere invio per uscire: ")
    
    if temp == "":
        break

    sequence.append(int(temp))

index_of_max_local = []
for i in range(1, len(sequence)-1):
    if sequence[i-1] < sequence[i] > sequence[i+1]:
        index_of_max_local.append(i)



if index_of_max_local == []:
    print("Non ci sono massimi locali")
else:
    print("I massimi locali si trovano in posizione: ", index_of_max_local) #Gli le posizioni partono da 1 e non da 0
    