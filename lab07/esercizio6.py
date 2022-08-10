# Scrivete la funzione sum_without_smallestche calcoli la somma di tutti i valori di una lista, escludendo il valore minimo

def sum_without_smallest(list):
    
    sum = 0
    for i in range(len(list)):
        sum += list[i]  
    return sum - min(list)

a = [1, 2, 3, 5,2, 9]

