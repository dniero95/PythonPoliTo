## Testo dell'esercizio

Cifratura monoalfabetica casuale. Il cifrario di Cesare, che trasla ogni lettera di una quantità fissa, è troppo facile da violare. Ecco un’idea migliore: come chiave, invece di usare un numero, usiamo una parola, che immaginiamo essere FEATHER. Per prima cosa eliminiamo le lettere duplicate dalla parola chiave, ottenendo FEATHR, poi aggiungiamo in fondo ad essa le altre lettere dell’alfabeto, in ordine inverso:
FEATHRZYXWVUSQPONMLKJIGDCB
Ora cifriamo le lettere, seguendo questo schema:

ABCDEFGHIJKLMNOPQRSTUVWXYZ

↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓

FEATHRZYXWVUSQPONMLKJIGDCB

Tutti gli altri caratteri (spazi, cifre, punteggiatura, ...) devono rimanere invariati. Scrivete un programma che cifri o decifri un file di testo (il cui nome è inserito dall’utente) usando una parola chiave, inserita dall’utente e memorizzata in una variabile, e scrivendo le informazioni decifrate in un file di testo scelto dall’utente.