from os import system
#Exercice1:Conversion des listes en dictionnaires
keys=["Ten","Twenty","Thirty"]
values=[10,20,30]
nombres={x:y for x,y in zip(keys,values)}
#dictionnaire=dict(zip(keys,values))
print(nombres)
system("pause")
print("*************************************************")



#Exercice2: Cinémax

family={"rick":43,"beth":13,"morty":5,"summer":8}
for key,value in family.items():
	if value<3:
		prix=0
	elif 3<=value<12:
		prix=10
		n+=10
	else:
		prix=15
		n+=15
	print(f"{key} paye {prix} $")
print(f"La famille doit payer {n} $")


nom=input("Quel votre nom: ")
age=int(input(f"{nom} quel est votre âge: "))
famille={}
while nom!=0 and age!=0:
	famille.update({nom:age})
	nom=input("Quel votre nom: ")
	age=int(input(f"{nom} quel est votre âge: "))
print(famille)
system("pause")
print("************************************************")

print("**********EXERCICE 3:ZARA**********")
#2
brand={"name":"Zara", "creation_date":1975,
 "creator_name":"Amancio Ortega Gaona",
 "type_of_clothes":["men","women","children","home"],
 "international_competitors":["Gap","H&M","Benetton"],
 "number_stores":7000, "major_color":{"France":"blue",
 "Spain":"red", "US":["pink", "green"]}}
#3
brand["number_stores"]=2
#4
x=brand["type_of_clothes"]
x=" ".join(x)
print(f"Les clients de Zaras sont: {x}")
#5
brand["country_creation"]="Spain"
#6
print(brand["international_competitors"])
brand.update({"international_competitors":["Gap", "H&M", "Benetton", "Desigual"]})

#7
del brand["creation_date"]
#8
y=brand["international_competitors"][-1]
print(f"Le dernier concurrent internationnal est {y}")
#9
j=brand["major_color"]["US"]
j=" ".join(j)
print(f"Les principales couleurs de vêtements aux Etats-Unis sont:{j}")
#10
print(len(brand))
#11
for key in brand.keys():
	print(key)
#12
more_on_zara={"creation_date":1975, "number_stores":10000}
#13
brand.update(more_on_zara)
#14
i=brand["number_stores"]
print(f"La valeur de la clé number_stores est {i}")
system("pause")

