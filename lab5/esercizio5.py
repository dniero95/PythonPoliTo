# In francese i nomi delle nazioni sono femminili quando terminano con la lettera e, altrimenti sono maschili, con l’eccezione dei nomi seguenti, che sono maschili anche se terminano con la e:
# 
# •le Belize
# •le Cambodge
# •le Mexique
# •le Mozambique
# •le Zaïre
# •le Zimbabwe
# 
# Scrivete un programma che acquisisca il nome di una nazione in francese e vi aggiunga l’articolo: “le” per i nomi maschili e “la” per quelli femminili, come “le Canada” o “la Belgique”.Se, però, il nome della nazione inizia con una vocale, l’articolo diventa “l’” (ad esempio, l’Afghanistan). Infine, per i paesi qui elencati, che hanno un nome plurale, si usa l’articolo “les”:
# •les Etats-Unis
# •les Pays-Bas

import re

nation_name = input("Inserisci il nome di una nazione in francese:")

plural_name = ["Etats-Unis", "Pays-Bas"]
male_name_exeption = ["Belize", "Cambodge", "Mexique", "Mozambique", "Zimbabwe", "Zaïre"]

if re.search("^[AEIOUaeiou]", nation_name):
    print("l'" +nation_name)
elif nation_name in plural_name:
    print("les", nation_name)
elif nation_name[len(nation_name)-1] == "e" and nation_name not in male_name_exeption:
    print("la", nation_name)
elif nation_name[len(nation_name)-1] != "e" or nation_name in male_name_exeption:
    print("le", nation_name)
