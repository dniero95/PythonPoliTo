# Scrivete un programma che converta un numero romano, come MCMLXXVIII, nella sua rappresentazione decimale. 
# 
# Suggerimento:per prima cosa, scrivete una funzione che restituisce il valore numerico di ciascuna singola lettera,
# 
# poi usate l’algoritmo seguente:
# 
# totale = 0
# 
# Finché la stringa s contenente il numero romano non è vuota
#   Se s ha lunghezza 1 oppure valore(primo carattere di s)è almeno uguale a valore(secondo carattere di s)
#       Aggiungi valore(primo carattere di s)a totale. 
#       Elimina il primo carattere di s.
#   Altrimenti
#       Aggiungi a totalela differenza:
#           valore(secondo carattere di s)–valore(primo carattere di s)
#       Elimina il primo e il secondo carattere di s.[P5.27]

import re

def roman_to_int(str):
    base = [("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000)]  #corrispondenze numeri romani-numeri decimali

    arr_of_roman_number = list(str)
    arr_of_decimal_number = []
    for char in arr_of_roman_number:
        for couple in base:
            if(char ==couple[0]):
                arr_of_decimal_number.append(couple[1])
    
    index_of_max_num = arr_of_decimal_number.index(max(arr_of_decimal_number))
    decimal_number = arr_of_decimal_number[index_of_max_num]
    for subtract in range(index_of_max_num):
        decimal_number -= arr_of_decimal_number[subtract]

    for add in range(index_of_max_num+1, len(arr_of_decimal_number)):
        decimal_number += arr_of_decimal_number[add]

    
    return decimal_number

roman_number = input("Inserisci un numero romano: ")

print("Il corrispondente numero decimale è", roman_to_int(roman_number))

