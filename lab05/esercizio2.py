# Usando la formula seguente(in cui a, b, r, ed m sono numeri interi):

#                             rnew= (a ⋅rold+ b) % m

# e, poi, ripetendo il calcolo assegnando rnewa rold, si ottiene un semplice generatore casuale.Scrivete un programma che chieda all’utente di fornire un valore iniziale per rold(valore che viene chiamato “seme”, seed), poi visualizzi i primi 100 numeri interi generati dalla formula, usando a= 32310901, b= 1729 e m= 224. 

rold = int(input("Inserisci un numero che faccia da seme: "))

for a in range(100):
    rnew = (32310901*rold+1729)%224
    rold = rnew
    print(rnew)