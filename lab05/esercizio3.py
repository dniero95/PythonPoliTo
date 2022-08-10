# In una simulazione predatore-preda, si calcolano le popolazioni di predatori (predators, abbreviatopred) e prede (preys) usando le equazioni seguenti:
# 
#                   preyn+1 = preyn×(1 + A –B ×predn)
# 
#                   predn+1 = predn×(1 –C + D ×preyn)
# 
# In queste equazioni, le costanti hanno i seguenti significati:
# 
# •A è il ritmo con cui le prede, in assenza di predatori, incrementano il proprio numero (tenendo conto delle nuove nascite e delle morti naturali)
# 
# •B è il tasso di predazione, ossia il numero di prede uccise da ciascun predatore•C è il ritmo con cui i predatori, in assenza di cibo, riducono il proprio numero (tenendo conto delle morti di per assenza di ciboe delle nascite)
# 
# •D è il tasso con cui i predatori aumentano in presenza di cibo, ossia il numero di predatori sopravvissuti per avere mangiato una preda.
# 
# Scrivete un programma che chieda questi valori all’utente, oltre alle dimensioni iniziali delle popolazioni di prede e predatori, e al numero di intervalli di tempo che coinvolgono la simulazione. La simulazioneprocede applicando ripetutamente le due formule, con l’accortezza che nessuna popolazione può diventare negativa. Successivamente, il programma deve visualizzare la dimensione delle due popolazioni per il numero di intervalli di tempo assegnato. Eseguite,come esempio, una simulazione con A = 0.1, B = C = 0.01 e D = 0.00002, con popolazione iniziale di 1000 prede e 20 predatori.

predator_population = int(input("Inserire il numero di predatori: "))
prey_population = int(input("Inserire il numero delle prede: "))

A = int(input("Inserire il ritmo con cui le prede incrementano il proprio numero in assenza di predatori: "))