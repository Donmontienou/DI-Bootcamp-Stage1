#Défi 1

number=int(input("Entrez un number: "))
length=int(input("Entrez un length: "))
liste=[]
x=0
while x<length: 
	liste.append(x*number)
	x+=1
print(liste)
input()


#Défi 2
liste=[]
chaîne=input("Entrez une chaîne: ")

liste.append(chaîne[0])
for i in chaîne:
	if liste[-1]!=i:
		liste.append(i)
print("".join(liste))

