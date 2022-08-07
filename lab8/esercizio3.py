# Quadrati magici. Una matrice n × n contenente i numeri interi 1, 2, 3, ..., n2 è un quadrato magico se la somma dei suoi elementi in ciascuna riga, in ciascuna colonna e nelle due diagonali ha lo stesso valore. Ad esempio, questo èun quadrato magico di dimensione 4:

# 16    3      2      13  
# 5    10     11       8
# 9     6      7      12
# 4    15     14       1
 
# Scrivete un programma che acquisisca in ingresso 16 valori e verifichi se, dopo averli disposti in una tabella 4 × 4 ordinatamente per righe, da sinistra a destra e dall’alto in basso, formano un quadrato magico. Dovete verificare due proprietà:
# 
# 1.Nei dati acquisiti sono presenti tutti e soli i numeri 1, 2, ..., 16?
# 
# 2.Quando i numeri vengono disposti nella tabella, le somme delle righe, delle colonne e delle diagonali sono tutte uguali l’una all’altra?

possible_values = range(1, 17)

matrix = [[],[],[],[]]

invalid = False
is_not_magic = False
magic_value = 0

for i in range(4):
    magic_value_checker = 0
    for j in range(4):
        value = int(input("Inserisci un numero intero: "))
        matrix[i].append(value)
        
        if i == 0:
            magic_value += value
        else:
            magic_value_checker += matrix[i][j]
            if j == 3 and magic_value != magic_value_checker:
                is_not_magic = True
            
            if i == 3 and j ==3 and magic_value != matrix[0][0]+matrix[1][1]+ matrix[2][2]+ matrix[3][3] and magic_value != matrix[0][3]+matrix[1][2]+ matrix[2][1]+ matrix[3][0]:
                is_not_magic = True
        if not (isinstance(value, int) and value in possible_values):
            invalid = True

magic_value = 0




print(matrix)

if invalid:
    print("Sono stati inseriti dei valori non validi!\n")
elif(is_not_magic):
    print("La matrice non è un quadrato magico!\n")
else:
    print("Complimenti! Hai inserito un quadrato magico!\n")
