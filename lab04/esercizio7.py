# Il gioco di Nim. Si tratta di un gioco molto noto, con un certo numero di varianti: quella qui descritta ha una strategia vincente davvero interessante. Due giocatori prelevano alternativamente biglie da un mucchietto. Ad ogni mossa, un giocatore sceglie quante biglie prendere: almeno una e al massimo metà delle biglie disponibili. Poi è il turno dell’altro giocatore. Il giocatore che prende l’ultima biglia perde la partita.
# Scrivete un programma che consenta all’utente di giocare contro il computer. Generate un numero intero compreso tra 10 e 100 e usatelo come dimensione iniziale del mucchietto di biglie. Generate un numero intero, 0 o 1, e utilizzatelo per decidere se sarà l’utente o il computer a giocare per primo. Generate un numero intero, 0 o 1, e usatelo per decidere se il computer giocherà in modo intelligente o stupido: giocando in modo stupido, ad ogni sua mossa il computer semplicemente preleva dal mucchietto un numero di biglie casuale (ma valido, cioè compreso tra 1 e n/2, se nel mucchietto sono rimaste n biglie); in modalità intelligente, invece, preleva un numero di biglie tale che il numero di quelle che rimangono nel mucchio sia una potenza di due diminuita di un’unità, cioè 3, 7, 15, 31 o 63. Quest’ultima è sempre una mossa valida, tranne quando la dimensione del mucchio è proprio uguale a una potenza di due diminuita di un’unità: in tal caso il computer fa una mossa scelta a caso (ovviamente tra quelle valide). Come potrete verificare sperimentalmente, il computer non può essere battuto quando gioca in modalità intelligente e fa la prima mossa, a meno che la dimensione iniziale del mucchio non sia 15, 31 o 63. Analogamente, un giocatore umano che faccia la prima mossa e conosca la strategia qui descritta è in grado di battere il calcolatore.


#genera un numero casuale di biglie compreso tra 10 e 100 e le mette in un "sacchetto"
from random import *
from math import *
num_marbles = randint(10,100)
num_marbles = range(1, num_marbles)
marbles_bag = []
for a in num_marbles:
    marbles_bag.append(a)

# print("restano queste biglie ", marbles_bag,"\n")   stampa il numero di biglie che restano per debug

print("\n***Nel sacchetto ci sono " + str(marbles_bag[len(marbles_bag)-1]) + " biglie.***\n")

#imposto chi giocherà per primo

if randint(0,1) == 1:
    turn_of = "computer" #inizia il pc
    print("Inizia il " + str(turn_of) +"\n")
else:
    turn_of = "user"  #inizia il giocatore
    print("Inizia l'" + str(turn_of) +"\n")     

#imposto l'intelligenza del computer

if randint(0,1) == 1:
    pc_intelligence = "smart" #il pc gioca in modo intelligente
    print("Sembra che il tuo avversario sia molto agguerrito oggi\n")
else:
    pc_intelligence = "dummy"  #il pc gioca in modo stupido
    print("Il tuo avversario non sembra molto in forma... Hai una possibilità di vincere!\n")

flag ="gamestart" #finchè il flag è su gamestart il gioco continua, se passa su gameover il gioco finisce

while flag == "gamestart":
    if turn_of == "user":
        correct_number_of_marbles = True    #Faccio prendere al giocatore un numero di biglie obbligandolo a prendre un numero previsto dal regolamento
        while(correct_number_of_marbles):
            user_takes_marbles = int(input("Quante biglie prendi? "))
            
            if len(marbles_bag) == 1 and user_takes_marbles == 1:  #il giocatore prende l'ultima biglia 
                marbles_bag.pop()
                print("Il giocatore ha preso l'ultima biglia e ha perso!")
                flag = "***gameover***\n"
                print(flag) #fine dei giochi
                break
            elif len(marbles_bag) == 1 and user_takes_marbles != 1:
                print("Hai quasi vinto, ma devi prendere solo l'ultima biglia. Non scoraggiarti ce l'hai quasi fatta...")
                continue
            
            
            if user_takes_marbles < 1 or user_takes_marbles > floor(len(marbles_bag)/2):
                print("Stai prendendo un numero di biglie sbagliato! Puoi prendere da 1 a " + str(floor(len(marbles_bag)/2)) + " biglie.")
            else:
                correct_number_of_marbles = False
            
        correct_number_of_marbles = True #imposto la variabile a true per la prossima iterazione

        if flag == "***gameover***\n": #se ha vinto il giocatore evita di fare un pop sulla lista vuota
            break

        i = 0
        
        while i < user_takes_marbles: #rimuovo dal sacchetto il numero di biglie prese dal giocatore
            marbles_bag.pop()
            i+=1
        
        print("\nRestano queste biglie ", len(marbles_bag), "\n")
        turn_of = "computer" #il prossimo turno sarà del computer
    elif turn_of == "computer":
        #il computer prende un numero randomico di biglie tra 1 e n/2

        if len(marbles_bag) == 1:  #il computer prende l'ultima biglia 
            marbles_bag.pop()
            print("Il computer ha preso l'ultima biglia e ha perso!")
            flag = "***gameover***\n"
            print(flag) #fine dei giochi
            break
        else:
            if pc_intelligence == "dummy":  #biglie prese dal computer in modalità stupida
                computer_takes_marbles = randint(1,floor(len(marbles_bag)/2))
            elif pc_intelligence == "smart": #biglie prese dal computer in modalità intelligente
                if (2**(log2(len(marbles_bag)+1)))-1==len(marbles_bag):
                    computer_takes_marbles = randint(1,floor(len(marbles_bag)/2))
                elif len(marbles_bag) > 63:
                    computer_takes_marbles = len(marbles_bag) - 63
                elif len(marbles_bag) > 31:
                    computer_takes_marbles = len(marbles_bag) - 31
                elif len(marbles_bag) > 15:
                    computer_takes_marbles = len(marbles_bag) - 15
                elif len(marbles_bag) > 7:
                    computer_takes_marbles = len(marbles_bag) - 7
                elif len(marbles_bag) > 3:
                    computer_takes_marbles = len(marbles_bag) - 3

        print("Il computer prende " + str(computer_takes_marbles) + " biglie")
        
        j = 0

        while j < computer_takes_marbles: #rimuovo dal sacchetto il numero di biglie prese dal computer
            marbles_bag.pop()
            j+=1

        print("\nRestano queste biglie ", len(marbles_bag), "\n")

        turn_of = "user" #il prossimo turno sarà dello user

