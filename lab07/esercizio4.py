# Scrivete un programma che generi una sequenza di 20 valori casuali compresi tra 0 e 99, poi visualizzi la sequenza generata, la ordini e la visualizzi di nuovo, ordinata. Usate il metodo sort.

from random import *

sequence = []
for i in range(20):
    sequence.append(randint(0,99))

print(sequence)

sequence.sort()

print(sequence)