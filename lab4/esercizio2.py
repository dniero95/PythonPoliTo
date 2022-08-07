str = input("Inserisci un stringa: ")

#parte a
print("parte a:")
for carattere in str:
     if carattere.isupper():
         print(carattere, end="")
     
#parte b:
print("parte b:")

for i in range(1, len(str), 2):
    print(str[i])

#parte c

print("parte c:")

vocali = ["a","e","i","o","u" ] 
temp = ""

for carattere in str:
    if carattere.lower() in vocali:
        temp += "_"
    else:
        temp += carattere

print(temp)

print("parte d:")
gdm = 0
for carattere in str:
    if carattere.isdigit():
        gdm+=1

print("Il numero di cifre è: ", gdm)

#parte e

print("parte e:")

gdm = 0
gdm = 0
for carattere in str:
    
    if carattere.lower() in vocali:
        print(gdm)
    
    gdm+=1

    
#fai esercizio 5, 7 laboratorio 4 fulvio corno