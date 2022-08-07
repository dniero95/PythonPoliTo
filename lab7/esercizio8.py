# Leggere una sequenza di numeri interi conclusa da una riga vuota.Individuare i due massimi locali (numeri maggiori sia del valore precedente che di quello successivo) più vicini fra loro come posizione e stampare la loro posizione.

num_list = []

while True:
    num = input("Inserisci un numero, per terminare vai a capo: ")
    if not num.isdigit():
        break

    num_list.append(int(num))


index_of_max_local = []
for i in range(1, len(num_list)-1):
    if num_list[i-1] < num_list[i] > num_list[i+1]:
        index_of_max_local.append(i)



if index_of_max_local == []:
    print("Non ci sono massimi locali")
else:
    list_of_distance = []
    for i in range(len(index_of_max_local)-1):
        list_of_distance.append(index_of_max_local[1+i]-index_of_max_local[i])
    
    j = list_of_distance.index(min(list_of_distance))
    print("I due massimi locali più vicini sono in posizione: ", index_of_max_local[j],index_of_max_local[j+1])


    