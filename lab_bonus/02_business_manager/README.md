## Testo dell'esercizio

Argomenti: classi, ereditarietà, polimorfismo, collezioni di oggetti


Descrizione della consegna:

Testo del problema

Realizzare le seguenti classi:

1) Persona è una classe astratta con

proprietà: Nome, Cognome, Stipendio
metodi: Tredicesima():double, ToString
2) Venditore che eredita da Persona con
proprietà: Settore che descrive il tipo di settore vendite a cui fa capo es Auto o Moto
metodi: Tredicesima() che restituisce il 91% in più dello stipendio, Clone, ToString
3) Meccanico eredita da Persona con
proprietà: Tipologia che descrive il tipo di settore a cui fa capo es Carrozzeria o Meccanica
metodi: Tredicesima che restituisce il 93% in più dello stipendio, Equals, ToString
4) ResponsabileVenditori eredita da Venditore con
proprietà: Venditori che serve a contenere i venditori di cui è responsabile
metodi: AggiungiVenditore(Venditore venditore) che aggiunge in coda alla lista un venditore, RestituisciVenditore(int index) che mi restituisce il venditore alla posizione index, CancellaVenditore(int index) che mi cancella il venditore alla posizione index, Tredicesima che restituisce il doppio dello stipendio più un bonus del 15% della tariffa giornaliera per ogni venditore di cui è responsabile, ToString
5) CapoOfficina eredita da Meccanico con
proprietà: Ordini lista di tipo Ordine.
metodi: AggiungiOrdine(Ordine ordine, int index), NoOrdini che restituisce il numero di ordini che sono stati inseriti; Tredicesima che ridefinisce il metodo e restituisce il doppio dello stipendio più il 5% dell’importo di ogni ordine da gestire, ToString
6) Prodotto che contiene come

proprietà: Codice, Prodotto, Descrizione, Prezzo
metodi: ToString
7) Ordine (classe che impedisce l’ereditarietà) che contiene come

proprietà: IdOrdine, la Data, ElencoProdotti: lista di Prodotto, Venditore di tipo Venditore
metodi: NoProdotti che restituisce la quantità totale di prodotti ordinati, Totale il costo complessivo, ToString per stampare un risultato globale dell’ordine, Scontrino è un metodo per stampare l’elenco dettagliato dell’ordine dove per ogni riga è presente il codice prodotto, nome del prodotto, quantità ordinata, prezzo unitario, subtotale

Costruire il Main con la possibilità di scegliere tra le seguenti azioni (creare un menu testuale):

- Stampa dell’elenco dei venditori
- Stampa dell’elenco dei meccanici
- Stampa di un certo ordine
- Stampa dei dati del responsabile venditori
- Stampa dei dati del capo officina