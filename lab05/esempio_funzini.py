#dato un numero controlla se è pari o dispari. vengono inseriti programmi finchè non viene inserito 0. Inserito 0 stampa la lista dei pari e la lista dei dispari

# def main():

#     even_list = []
#     odd_list = []

#     num = -1

#     num = int(input("Inserisci un numero: "))
#     while num != 0:

#         if pari_dispari(num):
#             even_list.append(num)
#         else:
#             odd_list.append(num)

#         num = int(input("Inserisci un numero: "))

#     print("La lista dei pari è: ", even_list)
#     print("La lista dei dispari è: ", odd_list)

def pari_dispari(n):
    if n % 2 == 0:
        return True
    return False

# main()

def divisibile(n, div = 3):
    if n % div == 0:
        return True
    return False

if __name__ == "__main__": 
    even_list = []
    odd_list = []

    num = -1

    num = int(input("Inserisci un numero: "))
    while num != 0:

        if divisibile(n = num, div = 4):
            even_list.append(num)
        else:
            odd_list.append(num)

        num = int(input("Inserisci un numero: "))

    print("La lista dei pari è: ", even_list)
    print("La lista dei dispari è: ", odd_list)