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
chaîne=input("Entrez une chaîne: ")
chaîne=set(chaîne)
new=" "
for i in chaîne:
	new=new+i
print(new)

