#1
import random

chaîne=input("Entrez une chaîne= ")
if len(chaîne)<10:
	print(f"la chaîne de caractère {chaîne} n'est pas assez longue")
else:
	print(f"la chaîne de caractère {chaîne} est trop longue")
input()

#2
#chaîne.split(" ")
chaîne=list(chaîne)
print(f"Le prémier caractère est {chaîne[0]} et le dernier caractère est {chaîne[-1]}")
input()

#3
chaîne="".join(chaîne) 
n=""
for i in chaîne:
	n+=i
	print(n)
input()

#4
chaîne=list(chaîne)
random.shuffle(chaîne)
chaîne1=""
chaîne1=chaîne1.join(chaîne)
print(chaîne1)

