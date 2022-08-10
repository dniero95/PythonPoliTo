# Scrivete un programma che acquisisca da tastiera una sequenza di numeri interi (terminata da una riga vuota), calcoli la somma alternata degli elementi di una lista. Ad esempio, se il programma legge i dati 1 4 9 16 9 7 4 9 11, deve calcolare e visualizzare 1 –4 + 9 –16 + 9 –7 + 4 –9 + 11 = –2

sequence = []

while True:
    temp = input("Inserisci un numero intero (premere invio per uscire: ")
    
    if temp == "":
        break

    sequence.append(int(temp))



tot = 0
for i in range(len(sequence)):
    if i%2 != 0:
        tot -= sequence[i]
    else:
        tot += sequence[i]

print("La somma alternata alla differenza di tutti gli elementi della sequenza è:", tot)