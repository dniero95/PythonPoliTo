# Scrivete la funzione def sameSet(a, b)che verifichi se due liste contengono gli stessi elementi, indipendentemente dall’ordine e ignorando la presenza di duplicati. Ad esempio, le due liste 1 4 9 16 9 7 4 9 11 e 11 11 7 9 16 4 1 devono essere considerate uguali.La funzione non deve modificare le liste ricevute come parametri.



def sameSet(a, b):
    if len(a)>len(b):
        for i in range(len(b)):
            is_the_same = False
            for j in range(len(a)):
                if b[i] == a[j]:
                    is_the_same = True
            if is_the_same == False:
                break
    else:
        for i in range(len(a)):
            is_the_same = False
            for j in range(len(b)):
                if a[i] == b[j]:
                    is_the_same = True
            if is_the_same == False:
                break
    
    return is_the_same

l1 = [1, 4, 9, 16, 9, 7, 4, 9, 11]
l2 = [11, 11, 7, 9, 16, 4, 1]

print(sameSet(l1, l2))