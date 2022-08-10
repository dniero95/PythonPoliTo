# Scrivete un’applicazione che gestisca la prevendita di un numero limitato di biglietti del cinema. Ogni acquirente può comprare al massimo 4 biglietti e non ne possono essere venduti più di 100. Il programma deve chiedere all’utente quanti biglietti intende acquistare, per poi visualizzare il numero di biglietti rimasti. L’operazione va ripetuta fino all’esaurimento dei biglietti, visualizzando al termine il numero di acquirenti. [P4.33]



num_ticket =  10

num_costumer = 0



while num_ticket > 0:
    # too_much_tk = True
    # while too_much_tk:

        num_ticket_sell = int(input("Quanti biglietti vuoi acquistare?  "))

        if(num_ticket_sell > 4 and num_ticket > 4):
            print("Stai acquistando troppi biglietti. Puoi acquistarne al massimo 4")
            continue
        elif num_ticket < 4 and num_ticket_sell> num_ticket:
            print("Sono rimasti solo " + str(num_ticket) + " biglietti, quanti biglietti vuoi acquistare?")
            continue
        else:
            # too_much_tk = False
            num_ticket -= num_ticket_sell
            num_costumer += 1

print("Sono stati venduti biglietti a " + str(num_costumer) + " clienti\n")