# Fattorizzazione di interi. Scrivete un programma che chieda all’utente un numero intero e ne visualizzi i fattori. Se, adesempio, l’utente fornisce il numero 150, il programma deve visualizzare:
# 2
# 3
# 5
# 5


num = int(input("Inserisci un numero intero: "))
num2 = num
i = 2
factor = []
while num != 1:
    if num % i ==0:
        factor.append(i)
        num /=i
    else:
        i += 1
    

print("I fattori primi di", int(num2), "sono", factor)