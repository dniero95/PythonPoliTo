# Scrivete un programma che giochi a tic-tac-toe (in italiano, tris o schiera). Il tic-tac- toe si gioca su una scacchiera 3 × 3, come quella qui raffigurata, da due giocatori che, a turno, posizionano in una casella libera il proprio simbolo (una croce per il primo giocatore e un cerchio per il secondo). Il giocatore che compone una schiera di tre propri simboli su una riga, una colonna o una diagonale, vince la partita. Il programma deve disegnare la scacchiera, chiedere all’utente le coordinate del suo prossimo simbolo, cambiare il giocatore di turno dopo ogni mossa e decretare il vincitore.



tris = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]

gameover = False
turn_of_X_or_O = True
turn_number = 0


print("\n    ****GAMESTART****\n\n    ****SCHIERA****\n\n    ****Turno_1\n\n    ****Gioca_X****\n")

while not gameover:
    
    row = int(input("Inserisci riga: ")) -1
    column = int(input("Inserisci Colonna: ")) -1

    print("\n    ****Turno_"+str(turn_number)+"****\n")

    if turn_of_X_or_O:
        tris[row][column] = "X"
        print("\n    ****Gioca_X****\n")
        turn_of_X_or_O = False
    else:
        tris[row][column] = "0"
        print("\n    ****Gioca_0****\n")
        turn_of_X_or_O = True

    
    turn_number += 1
    print("\t+-+-+-+\n\t|"+tris[0][0]+"|"+tris[0][1]+"|"+tris[0][2]+"|\n\t+-+-+-+\n\t|"+tris[1][0]+"|"+tris[1][1]+"|"+tris[1][2]+"|\n\t+-+-+-+\n\t|"+tris[2][0]+"|"+tris[2][1]+"|"+tris[2][2]+"|\n\t+-+-+-+\n")

    if tris[0][0]==tris[0][1]==tris[0][2]=="X" or tris[1][0]==tris[1][1]==tris[1][2]=="X" or tris[2][0]==tris[2][1]==tris[2][2]=="X" or tris[0][0]==tris[1][0]==tris[2][0]=="X" or tris[0][1]==tris[1][1]==tris[2][1]=="X" or tris[0][2]==tris[1][2]==tris[2][2]=="X" or tris[0][0]==tris[1][1]==tris[2][2]=="X" or tris[0][2]==tris[1][1]==tris[2][0]=="X":
        print("\n    ****Player_X_Win!****\n")
        break
    elif tris[0][0]==tris[0][1]==tris[0][2]=="0" or tris[1][0]==tris[1][1]==tris[1][2]=="0" or tris[2][0]==tris[2][1]==tris[2][2]=="0" or tris[0][0]==tris[1][0]==tris[2][0]=="0" or tris[0][1]==tris[1][1]==tris[2][1]=="0" or tris[0][2]==tris[1][2]==tris[2][2]=="0" or tris[0][0]==tris[1][1]==tris[2][2]=="0" or tris[0][2]==tris[1][1]==tris[2][0]=="0":
        print("\n    ****Player_0_Win!****\n")
        break
    elif turn_number == 9:
        print("\n    ****Draw!****\n")
        break
    




print("\n    ****GAMEOVER****\n")

#DA FINIRE