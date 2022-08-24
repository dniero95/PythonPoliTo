## Testo dell'esercizio

L’algoritmo seguente individua la stagione (Spring, Summer, Fall o Winter, cioè, rispettivamente, primavera, estate, autunno o inverno) a cui appartiene una data, fornita come mese e giorno.
```
Se mese è 1, 2 o 3, stagione = “Winter”
Altrimenti se mese è 4, 5 o 6, stagione = “Spring” 
Altrimenti se mese è 7, 8 o 9, stagione = “Summer” 
Altrimenti se mese è 10, 11 o 12, stagione = “Fall” 
    Se mese è divisibile per 3 e giorno >= 21
    Se stagione è “Winter”, stagione = “Spring”
    Altrimenti se stagione è “Spring”, stagione = “Summer” 
    Altrimenti se stagione è “Summer”, stagione = “Fall” 
    Altrimenti stagione = “Winter”
```
Scrivete un programma che chieda all’utente un mese e un giorno e, poi, visualizzi la stagione determinata da questo algoritmo.