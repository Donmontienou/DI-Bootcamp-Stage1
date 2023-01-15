#Exercice1:Set
my_fav_numbers={"4","8","17","2"}
my_fav_numbers.update(["5","10"])
print(type(my_fav_numbers))
x=my_fav_numbers.pop()
print(my_fav_numbers)

friend_fav_numbers={"12","7","9","14"}
our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)
print("*************************************************************************")
input()

#Exercice 2: Tuple
print("Il n'est pas possible d'ajouter plus d'entiers au tuple")
print("*************************************************************************")
input()

#Exercice 3:Liste
basket=["Banana","Apples","Oranges","Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("kiwi")
basket.insert(0,"Apples")
n=basket.count("Apples")
print(f"Il y'a {n} pommes dans le panier")
basket.clear()
print(basket)
print("****************************************************")
input()

#Exercice4: flotteurs

print("Un float est un nombre à virgule")
print("La difference entre un entier et un flottant est que un entier ne doit pas avoir une virgule c'est à dire un entier naturel alors que le flottant peut avoir une virgule comme il peut ne pas avoir de virgule cas des réels ")
print("")
liste=[]
i=1
while i<=5:
	liste.append(i)
	i+=0.5
print(liste)
print("****************************************************")


#Exercice5: Boucle for
for i in range(1,21):
	print(i)
input()
x=range(1,21)
for i in x:
	if x.index(i)%2==0:
		print(i)
		print("****************************************************")
input()

#Exercice6: Boucle while

nom=input("Entrez votre nom=")
mon_nom="Merveille La Star"
while nom!=mon_nom:
	nom=input("Entrez votre nom=")
print("****************************************************")
input()

#Exercice7:Frfuits préférés

fruits=input("Entrez vos fruits préférés: ")
liste=list(fruits.split(" "))
fruit=input("Entrez le nom d'un fruit= ")
if fruit in liste:
	print("Vous avez choisi l'un de vos fruits préférés! Prenez plaîsir!")
else:
	print("Vous avez choisi un nouveau fruit. J'espère que vous appréciez")
print("****************************************************")
input()

#Exercice 8: Qui a commandé une Pizza

serie_gar=input("Entrez une serie de garniture de pizza: ")
liste=[]
prix=10
while serie_gar!="quitter":
	#serie_gar=input("Entrez une serie de garniture de pizza: ")
	prix+=2.5
	print(f"Vous avez ajouté {serie_gar} à leur pizza")
	serie_gar=serie_gar.split(" ")
	liste=liste+serie_gar
	serie_gar=input("Entrez une serie de garniture de pizza: ")
	
print(f"Les garnitures sur la pizza sont:{liste}.\nLe prix est {prix}")
print("****************************************************")
input()	


#Exercice 9: Cinémax

nombre=int(input("Entrez le nombre de personnes qui veulent le billet: "))
prix_billet=0
i=1
while i<=nombre:
	age=int(input("Quel est l'âge d'une personne qui veut le billet: "))
	if age<3:
		print(f"Le billet est gratuit pour les personnes de {age} ans")
	elif 3<=age<=12:
		prix_billet+=10
	else:
		prix_billet+=15
	i+=1
print(f"Le coût total de tous les billets est: {prix_billet} $")

noms=input("Donnez les noms des adolescents qui sont venus dans la salle: ")
noms=list(noms.split(" "))
print(len(noms))
i=1
while i<=len(noms):
	for nom in noms:
		âge=int(input(f"{nom} donnez votre age: "))
		if 10<=âge<=19:
			continue
		else:
			noms.remove(nom)
	i+=1
print(noms)
print("****************************************************")
input()


#Exercice 10: Commande Sandwich

sandwich_orders=["Tuna sandwich","Avocado sandwich","Egg sandwich","Sabih sandwich","Pastrami Sandwich"]
finished_sandwishes=[]
i=0
while len(sandwich_orders)!=0:
	for sandwich in sandwich_orders:
		x=input(f"Entrez oui si {sandwich} est préparé:")
		if x=="oui":
			finished_sandwishes.append(f"{sandwich_orders.pop(sandwich_orders.index(sandwich))}")
			print(f"{sandwich} a été préparé")
print(finished_sandwishes)		

#Exercice11:
