## Testo dell'esercizio

Scrivere un programma che cerchi una data parola nel contenuto di un gruppo di file. Il programma innanzitutto chiede l’elenco dei file (da inserire su una sola riga, separati da virgole e la parola da cercare. I nomi dei file saranno memorizzati in una lista (files), la parola da cercare viene memorizzata in una variabile.
Occorre visualizzare tutte le righe che contengono la parola, indipendentemente da maiuscole o minuscole, ciascuna riga preceduta dal nome del file in cui si trova. Ad esempio, se la parola fosse “ring”, e lista contenesse:

```book.txt, address.txt, homework.py```

allora il programma potrebbe visualizzare quanto segue:

```
book.txt: There is only one Lord of the Ring, only one who can bend
it to his will
book.txt: The ring has awoken; it’s heard its masters call.
address.txt: Kris Kringle, North Pole
address.txt: Homer Simpson, Springfield
homework.py: string = "text"
```

La parola da cercare viene inserita dall’utente e sono valide anche le parole che contengono quella da cercare (es. ring e ringhiare).