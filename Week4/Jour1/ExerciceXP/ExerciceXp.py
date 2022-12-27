#Exercice1:Bonjour le monde
print(4*"Hello world\n")
print("*****************************************************")
input()

#Exercice2
resultat=(99**3)*8
print(resultat)
print("*****************************************************")
input()

"""
#Exercice3
>>>5<3
#resultat=True
>>>3==3
#resultat=True
>>>3=="3"
#resultat=False
>>>"3">3
#resultat=False
>>>"Hello"=="Hello"
#resultat=True
"""

#Exercice4
computer_brand="DESKTOP-SKGQ70K"
print(f"i have {computer_brand} computer")
print("*****************************************************")
input()

#Exercice5
name="DA"
age=25
shoe_size=39
info="Je suis"+" "+name+" "+"j'ai"+" "+str(age)+" "+"ans"+" "+"ma pointure est"+" "+str(shoe_size)
print(info)
print("*****************************************************")
input()

#Exercice6
a=int(input("a= "))
b=int(input("b= "))
if a>b:
	print("Hello world")
print("*****************************************************")
input()

#Exercice7
nombre=int(input("Entrez un nombre= "))
if nombre%2==0:
	print(f"{nombre} est pair")
else:
	print(f"{nombre} est impair")
print("*****************************************************")
input()

#xercice8
nom=input("Quel est votre nom? ")
print(f"{nom} nous n'avons pas les même noms")
print("*****************************************************")
input()

#Exercice9
taille=float(input("Quel est votr taille en pouces? "))
x=taille*2.54
if x>145.0:
	print(f"Votre taille est {x} cm vous êtes assez grands pour rouler")
else:
	print(f"Votre taille est {x} cm vous devez grandir un peu plus pour rouler")
print("*****************************************************")

