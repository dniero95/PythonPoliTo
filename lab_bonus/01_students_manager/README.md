## Testo dell'esercizio

Si consideri il file Studenti.csv. Si richiede la costruzione di un software che consenta le seguenti operazioni:
- stampa dell'elenco degli studenti
- stampa dell'elenco dei soli studenti di una certa 
classe (data in input)
- visualizzare l'elenco degli studenti che hanno il 
cognome che inizia con una certa lettera data in input
- raggruppare gli studenti per classe e visualizzare il 
risultato
- creare un file di testo(studenti-quarta.txt) per stampare un elenco di studenti appartenenti alla classe quarta

## Approccio alla soluzione

1. Creo i file: main.py, student.py, sm_functions.py
2. In sm_functions.py definisco la funzione print_menu() 
   che stampa il menù delle opzioni disponibili per l'utente
3. In main.py definisco l'input per memorizzare 
   l'opzione dell'utente e una struttura ```python if...
   elif...else``` per differenziare i vari casi.
4. Creo un loop while per consentire all'utente di 
   inserire le opzioni più volte