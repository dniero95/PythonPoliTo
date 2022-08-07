# Scrivete un programma che inizializzi una lista con dieci numeri interi casuali tra 1 e 100 e, poi, visualizzi quattro righe di informazioni, contenenti:
# a.Tutti gli elementi di indice pari.
# b.Tutti gli elementi di valore pari.
# c.Tutti gli elementi in ordine inverso.
# d.Il primo e l’ultimo elemento.[P6.1]


from random import *


random_list = []
for i in range(10):
    random_list.append(randint(1, 100))

print(random_list)
print("Elementi di indice pari:")
for i in range(0,10, 2):
    print(random_list[i])


print("Elementi di valore pari:")
for i in range(10):
    if(random_list[i]%2==0):
        print(random_list[i])

print("Elementi in ordine inverso:")

for i in range(10):
    print(random_list[len(random_list)-i-1])

print("Primo e l’ultimo elemento:", random_list[0], random_list[len(random_list)-1])

