# Scrivete un programma che legga una parola e visualizzi tutte le sue sottostringhe, ordinate per lunghezza crescente. Se, ad esempio, l’utente fornisce la stringa “rum”, il programma deve visualizzare
# r u m ru um



word = str(input("Inserisci una parola: "))

j = 1
 
while j < len(word):
    i = 0
    while i < len(word):
        if i+j>len(word):
            i +=1
            continue
        print(word[i:i+j])
        i +=1
    j+=1

