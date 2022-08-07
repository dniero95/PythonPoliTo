# Scrivete la funzione merge_sorted(a, b)che fonde due liste ordinate(si supponga quindi che siano già ordinate in modo crescente), restituendo una nuova lista ordinata in modo crescente. Gestite un indice corrente per ciascuna lista, in modo da tenere traccia della porzione già elaborata. Le liste di partenza non devono essere modificate. Se, ad esempio, il contenuto di a è 1 4 9 16 e il contenuto di b è 4 7 9 9 11, l’invocazione merge_sorted(a, b)restituisce una nuova lista contenente i valori 1 4 4 7 9 9 9 11 16. Non utilizzare il metodo sort né la funzione sorted(sfruttare l’informazione che gli elementi di ciascuna lista sono già ordinati per ottenere una soluzione più efficiente).

def merge_sorted(a, b):
    
    merged_list = []

    #shortest_list_len = (len(a) if len(a) < len(b) else len(b))

    j = 0 
    k = 0
    
    while True:
        if  a[j]<b[k]:
            
            merged_list.append(a[j])
            if j == len(a)-1:
                flag = False
                break
            
            
            j +=1
            
        else:
            merged_list.append(b[k])
            if k == len(b)-1:
                flag = True
                break
            
            
            k += 1
            

    merged_list = merged_list + (a[j:] if flag else b[k:])

    return merged_list

list1 = [1,2,3]
list2 = [10, 122,  5432, 1000000]

print(merge_sorted(list1, list2))