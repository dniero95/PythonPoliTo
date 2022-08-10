# Spesso i valori raccolti durante un esperimento vanno corretti, per togliere parte del rumore di misura. Un approccio semplice a questo problema prevede di sostituire, in una lista, ciascun valore con la media tra il valore stesso e i due valori adiacenti (o un unico adiacente se il valore in esame si trova a una delle due estremità della lista). Realizzate un programma che svolga tale operazione, senza creare un’altra lista.

def measure_correction(l):
    correction1 = 0
    correction2 = 0
    for i in range(len(l)):
        if i == 0:
            correction1 = (l[i]+l[1])/2
        elif i == len(l)-1:
            l[i] = (l[i]+l[i-1])/2
            l[i-1] = correction1
        else:
            correction2=(l[i-1]+l[i]+l[i+1])/3
            l[i-1] = correction1
            correction1 = correction2
    
    return l

print(measure_correction([1,2,2,2,1]))

            