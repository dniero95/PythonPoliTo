# def countWords(string)che restituisca il numero di parole presenti nella stringa string. Le parole sono sequenze di caratteri separate da spazi(si ipotizzi che tra due parole consecutive vi sia esattamente uno spazio). Ad esempio, countWords("Mary had a little lamb")restituisce 5.[P5.7]Come si potrebbe estendere l’esercizio in modo da trattare correttamente delle stringhe in cui siano presenti più spazi tra le parole?

from re import *

str = input("Inserisci una stringa: ")

def countWords(string):
    find_word = "\w+"
    return len(findall(find_word, str))

print("Il numero di parole in", str, "è", countWords(str))
