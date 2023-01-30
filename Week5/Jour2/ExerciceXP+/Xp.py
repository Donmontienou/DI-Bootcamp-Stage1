from os import system
import random
print("\n")
print("\t\t\t\tExercice1: Famille introductions")
print("\n")

class Family():
	def __init__(self,membres,nom_famille):
		self.membres=membres
		self.nom_famille=nom_famille

	def born(self,**kwargs):
		self.membres.append(kwargs)
		print(f"Nos félicitation à la famille {self.nom_famille}")


	def is_18(self,name):
		for elem in self.membres:
			if elem['name']==name:
				if elem['age']>18:
					print(f"")
					print("True") 
				else:
					print("False")


	def family_presentation(self):
		for nom in self.membres:
			print(f"{self.nom_famille}:" ,nom["name"])


x=[{'name':'Michael','age':35,'gender':'Male','is_child':'False'},{'name':'Sarah','age':32,'gender':'Female','is_child':'False'}]

Famille=Family(x,'Konate')
Famille.born(name='Gerome',age=5,gender='Male',is_child='True')
Famille.is_18('Michael')
Famille.family_presentation()

system("pause")


print("\n")
print("\t\t\t\tExercice2: Famille introductions")
print("\n")

class TheIncredibles(Family):
	pass

	def user_power(self):
		for elem in self.membres:
			if elem["age"]>18:
				print(elem["power"])
			else:
				print("Vous n'êtes pas puissant")
				

	def incredible_presentation(self):
		super().__init__(self.membres,self.nom_famille)
		for nom in self.membres:	
				print(f"{self.nom_famille}:",nom["name"])

		super().family_presentation()

x1=[{'name':'Michael','age':35,'gender':'Male','is_child':'False','power':'fly','incredible_name':'MikeFly'},
{'name':'Sarah','age':32,'gender':'Female','is_child':'False','power':'read minds','incredible_name':'SuperWoman'}]


famille=TheIncredibles(x1, 'Traore')
famille.user_power()
famille.incredible_presentation()
famille.born('name':'Jack','age':0,'gender':'Male','is_child':True,'power': 'Puissance inconnue','incredible_name':'nom incredible inconnu')
famille.incredible_presentation()
