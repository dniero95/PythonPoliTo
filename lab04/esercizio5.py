# Numeri primi. Scrivete un programma che chieda all’utente un numero intero e, poi, visualizzi tutti i numeri primi minori o uguali a tale numero. Se, ad esempio, l’utente fornisce il numero 20, il programma deve visualizzare:
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19

num = int(input("Inserisci un numero: "))
flag = "primo"
print("I numeri primi da 0 a " + str(num) + " sono:")
for a in range(2, num):
    for b in range(2, a):
        if(a%b== 0 and a!=b):
            flag = "non primo"
        
    if flag == "primo":
        print(a)
    else:
        flag = "primo"

