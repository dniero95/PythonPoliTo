# Quando utilizzate uno sportello bancario automatico (ATM, automatic teller machine) con la vostra carta, dovete usare un numero identificativo personale (PIN, personal identification number) per poter accedere al vostro conto. Se un utente sbaglia tre volte l’inserimento del PIN, la macchina trattiene la carta e la blocca.Nell’ipotesi che il PIN dell’utente sia “1234”, scrivete un programma che chieda all’utente di digitare il PIN, consentendo al massimo tre tentativi e agendo in questo modo:

# •se l’utente inserisce il numero corretto, visualizzate il messaggio “Your PIN is correct” e terminate il programma;
# 
# •se l’utente inserisce un numero sbagliato, visualizzate il messaggio “Your PIN is incorrect” e, se avete chiesto il PIN meno di tre volte, chiedetelo di nuovo;
# 
# •se l’utente inserisce un numero sbagliato per tre volte, visualizzate il messaggio “Your bank card is blocked” e terminate il programma.


PIN = 1234

for i in range(3):
    PIN_check = int(input("Inserisci il PIN: "))
    if PIN_check == PIN:
        print("Your PIN is correct")
        break
    elif(i == 2):
        print("Your bank card is blocked")
        break
    
    print("Your PIN is incorrect")