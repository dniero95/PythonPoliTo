## Testo dell'esercizio

L’agenzia delle entrate vuole sperimentare l’introduzione di un nuovo codice fiscale e vi chiede di scrivere un programma che permetta di verificare la correttezza di un insieme di codici fiscali a partire dai dati degli utenti a cui corrispondono. Il programma chiede all’utente il nome di un file che contiene una lista di informazioni relative ad una persona e il relativo codice fiscale. Il nome del file è fatto da massimo 30 caratteri.

Ogni riga del file di ingresso contiene tutte le informazioni di una persona e ha il seguente formato:

```
      <nome>,<cognome>,<sesso>,<data di nascita>,<luogo di nascita>,<codice fiscale>
```

- Tutti i campi sono separati da virgole
- Nome, cognome sono stringhe lunghe al massimo 80 
  caratteri, non contengono spazi ed eventualmente al posto degli spazi contengono il carattere ‘_’
- Sesso è un carattere: ‘M’ per maschio e ‘F’ per femmina
- Luogo di nascita è un codice di 4 caratteri
- La data è nel formato gg/mm/aaaa
- Il codice fiscale è una stringa di 14 caratteri
- Il numero di elementi contenuto nel file di ingresso 
  <ins>non è noto</ins> a priori
- Si assuma che il formato del file sia sempre corretto

Le regole per il calcolo del nuovo codice fiscale sono le seguenti:

- 3 lettere maiuscole per il nome, che sono le prime 3 lettere (diverse dal carattere ‘ _’) e se il nome ha meno di tre lettere quelle rimanenti vanno segnate con X
- 3 lettere maiuscole per il cognome, che sono le prime 3 lettere (diverse dal carattere ‘ _’) e se il cognome ha meno di tre lettere quelle rimanenti vanno segnate con X
- 4 caratteri per la data di nascita, codificati come giorno + mese + anno; se il sesso è ‘F’ il risultato va aumentato ancora di 1000 (e.g. 11/12/2000 corrisponde a 2023 se la persona è ‘M’ e 3023 se ‘F’)
- Il luogo di nascita (codice originale di 4 caratteri)

Il programma deve, per ogni persona presente nel file di ingresso, calcolare il suo codice fiscale secondo le nuove regole e confrontarlo con quello presente nel file, e deve produrre in output (su schermo) i risultati della verifica, indicando (per i soli codici fiscali errati) quello corretto.

Inoltre, considerando che nel primo file ci sono al massimo 20 luoghi di nascita distinti, stampare su un file “log.txt” i luoghi e il numero di persone (per ogni luogo) in cui si sono verificati gli errori.

**Esempio:**

_File dati.txt:_

```
Rino,Gaetano,M,13/12/1956,FTRG,RINCAE1981FTRG
Lucio,Dalla,M,11/4/1943,BGNL,LUCDAL1858BGNL
Paola,De_Amicis,F,25/12/2017,FRRA,PAODEA3054FRRA
Zu,Pi,M,11/12/2015,BGNL,ZUXPII2038PKNN
Carola,Dibari,F,1/1/1915,PRLM,CARDIB2917PRLM
```

_Output del programma eseguito leggendo da dati.txt_:

```
Codice errato RINCAE1981FTRG codice corretto RINGAE1981FTRG
Codice errato LUCDAL1858BGNL codice corretto LUCDAL1958BGNL
Codice errato ZUXPII2038PKNN codice corretto ZUXPIX2038BGNL
```

_File log.txt:_

```
FTRG 1 errori
BGNL 2 errori
```