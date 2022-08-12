# Scambiare tra loro il primo e l’ultimo elemento della lista.
from math import ceil, floor


def exchange_first_last(list):
    first = list[0]
    last = list[-1]
    list[0] = last
    list[-1] = first

# b. Far scorrere tutti gli elementi di una posizione “verso destra”, spostando l’ultimo elemento nella prima posizione. Ad esempio, la lista 1 4 9 16 25 deve diventare 25 1 4 9 16.

def shift_right(list):
    list.insert(0, list[-1])
    list.pop()

# c. Sostituire con 0 tutti gli elementi di valore pari.

def even_to_zero(list):
    for number in list:
        if isinstance(number, int) and number % 2 ==0:
            list[list.index(number)] = 0

# d. Sostituire ciascun elemento, tranne il primo e l’ultimo, con il più grande dei due elementi ad esso adiacenti. È possibile usare liste di appoggio.

def max_in_middle(list):
    pass # todo: define function

# e. Eliminare l’elemento centrale della lista se questa ha dimensione dispari, altrimenti eliminare i due elementi centrali.

def delete_central(list):
    if len(list) % 2 == 0:
        del list[int(len(list) / 2)]
        del list[int((len(list) / 2))]
    else:
        del list[int(len(list) / 2)]

# f. Spostare tutti gli elementi pari all’inizio della lista (lasciando quelli dispari in coda), preservando però l’ordinamento relativo tra gli elementi.

def shift_even_to_start(list):
    even_list = [number for number in list if number % 2 == 0]
    odd_list = [number for number in list if number % 2 != 0]
    list.clear()
    list.extend(even_list)
    list.extend(odd_list)

# g. Restituire il secondo valore maggiore della lista (senza pari meriti).

def second_top(list):
    top = max(list)
    del list[list.index(top)]
    return max(list)

# h. Restituire True se e solo se la lista è ordinata in senso crescente.

def is_asc(list):
    asc = True
    for count, number in enumerate(list[1:]):
        if count == 0:
            continue
        elif number <= list[count - 1]:
            asc = False

    return asc
