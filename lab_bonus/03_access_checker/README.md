## Testo dell'esercizio

Scrivere un programma C che permetta di rilevare accessi sospetti a un server analizzando un file di log degli accessi chiamato “access.txt”.

Il file memorizza su ogni riga il tentativo di accesso di un utente al server nel seguente formato:
<br />```<DATA> <ORA> <Username> <STATUS>```

Si facciano le seguenti ipotesi:

- La data è espressa nel formato AAAA-MM-GG.
- L’ora è espressa nel formato HH:MM:SS.
- Lo username è costituito da un massimo di 10 caratteri 
  privi di spazi.
- Lo stato può assumere 2 valori: S per indicare un 
  accesso corretto o F per indicare un accesso fallito.
- Il file è ordinato per data e ora crescenti
- **Non è noto il numero di righe che compongono il file.**

Il programma riceve sulla linea di comando un numero 
massimo di 10 utenti (username) da monitorare. Si definisce **ANOMALIA** due accessi consecutivi <ins>**falliti**</ins> da parte di un utente nello stesso giorno a distanza di meno di un minuto.

Il programma deve:

- Stampare le anomalie rilevate per gli utenti ricevuti in input (nell’ordine in cui vengono rilevate nel file access.txt) indicando username, data, ora del primo accesso fallito, ora del secondo accesso fallito.
- Stampare il numero totale di anomalie rilevate.
- Identificare l’utente tra quelli ricevuti in input con il maggior numero di anomalie rilevate

**Esempio**

Sia dato il seguente file access.txt

```
2015-01-01 12:00:01 rossi S 
2015-01-02 12:00:01 bianchi F 
2015-01-02 12:00:20 bianchi F 
2015-01-03 00:00:01 rossi S 
2015-01-03 11:12:20 verdi F 
2015-01-03 11:13:20 verdi F 
2015-01-03 11:13:42 verdi F 
2015-01-03 11:13:40 verdi S 
2015-01-05 09:00:01 verdi F 
2015-01-05 09:00:05 verdi F
```

Eseguendo il programma con i seguenti parametri:

```
C:\> esame rossi bianchi verdi

Anomalie rilevate:
bianchi 2015-01-02 12:00:01 12:00:20
verdi 2015-01-03 11:12:20 11:13:40
verdi 2015-01-03 11:13:40 11:13:42
verdi 2015-01-05 09:00:01 09:00:05

Numero totale di anomalie: 4
Utente con il maggior numero di anomalie: verdi
```
## Approccio alla soluzione