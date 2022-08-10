# Scrivete la funzione merge(a, b)che “fonde” due liste, alternando un elemento della prima e un elemento della seconda. Se una lista è più corta dell’altra, gli elementi vengono alternati fin quando è possibile, poi gli elementi rimasti nella lista più lunga vengono aggiunti ordinatamente in fondo. Le liste di partenza non devono essere modificate. Se, ad esempio, il contenuto di aè 1 4 9 16e il contenuto di bè 9 7 4 9 11, l’invocazionedi merge(a, b)restituisce una nuova lista contenente i valori 194794169 11.

def merge(a, b):
    merged_list = []

    shortest_list_len = (len(a) if len(a) < len(b) else len(b))

    j = 0 
    k = 0
    for i in range(shortest_list_len*2):
        if i % 2 == 0:
            merged_list.append(a[j])
            j +=1
        else:
            merged_list.append(b[k])
            k += 1

    if len(a)==len(b):
        return merged_list

    merged_list = merged_list + (a[shortest_list_len:] if len(a) > len(b) else b[shortest_list_len:])

    return merged_list


list1 = [1, 2, 3, 4]
list2 = [10, 122, 1000, 1234, 3000, 5432, 1000000]
print(merge(list1, list2))


