# Scrivete la funzione:def countVowels(string)che restituisca il numero di vocali presenti nella stringa string. Le vocali sono le lettere a, e, i, o e u, oltre alle rispettive versioni maiuscole.

from re import *

str = input("Inserisci una stringa: ")

def countVowels(str):
    str = str.lower()  #converte la stringa in minuscolo
    vocals = "[aeiou]"    #regex per trovare le vocali
    print(str)
    return len(findall(vocals, str))


print("Il numero di vocali in", str, "è", countVowels(str))

