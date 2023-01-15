from os import system
sequences=input("Entrez une squence de mot separée par des virgules: ")
liste=sequences.split(" ")
liste=sorted(liste)
liste=",".join(liste)
print(liste)
