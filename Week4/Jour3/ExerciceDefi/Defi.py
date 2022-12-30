from os import system
print("******************Defi 1******************")

mot=input("Entrez un mot: ")
liste=[]
dic_mot={}
for letter in mot:
	indice=[]
	for i in range(len(mot)):
		if mot[i]==letter:
			indice.append(i)
	dic_mot[letter]=indice
print(dic_mot)
system("pause")
print("******************Defi 2******************")


articles=[]
produits={}
article=input("Entrez un article dans votre magazin: ")
prix=int(input(f"Entrez le prix de {article}: "))
while prix!=0:
	produits[article]=prix
	article=input("Entrez un article dans votre magazin: ")
	prix=int(input(f"Entrez le prix de {article}: "))
print(produits)

somme=int(input("Entrez la somme que vous avez: "))
n=0
for article in produits.keys():
	if produits[article]<=somme:
		articles.append(article)
		#print(articles)
	else:
		pass
	articles.sort()
print(articles)
