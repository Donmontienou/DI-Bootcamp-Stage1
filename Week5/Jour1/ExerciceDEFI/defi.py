from os import system
sequences=input("Entrez une squence de mot separée par des virgules: ")
#sequences="Lundi","Girafe","Tigre","Abeille","Canard"
liste=list(sequences)
caractere=""
print(liste)
for i in liste:
	if "," in liste:
		liste.replace(","," ")
	liste.sort()
for n in range(len(liste)):
	if liste[n]==",":
		pass
	else:
		caractere+=liste[n]
print(caractere)

#print(sequences)
#print(liste)

