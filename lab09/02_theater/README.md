# 02_theater

## Testo dell'esercizio

Lo schema dei posti a teatro è una tabella con i prezzi dei biglietti per ciascun posto, come questa. 

```
10 10 10 10 10 10 10 10 10 10
10 10 10 10 10 10 10 10 10 10
10 10 10 10 10 10 10 10 10 10
10 10 20 20 20 20 20 20 10 10
10 10 20 20 20 20 20 20 10 10
10 10 20 20 20 20 20 20 10 10
20 20 30 30 40 40 30 30 20 20
20 30 30 40 50 50 40 30 30 20
30 40 50 50 50 50 50 50 40 30
```

Scrivete un programma che gestisca un menù che chieda all’utente di scegliere un posto, un prezzo o l’uscita dal programma. Contrassegnate con un prezzo uguale a 0 i posti già venduti. Quando l’utente specifica un posto, accertatevi che sia libero e che le coordinate siano all’interno della tabella. Quando, invece, specifica un prezzo, assegnategli un posto qualsiasi tra quelli disponibili a quel prezzo.