from os import system
print("\n")
print("\t\t\t\tExercice1: Famille introductions")
print("\n")

class Family():
	def __init__(self,membres,nom_famille):
		self.membres=[membres]
		self.nom_famille=nom_famille

	def born(self,**kwargs):
		self.membres.append(kwargs)
		print(f"Nos félicitation à la famille {self.nom_famille}")


	def is_18(self,name):
		for elem in self.membres:
			if elem["name"]==name:
				if elem["age"]>18:
					return True
				else:
					return False

	def family_presentation(self):
		for nom in self.membres:
			print(f"{self.nom_famille}:{nom}")



x={'name':'Michael','age':35,'gender':'Male','is_child':'False'}
y={'name':'Sarah','age':32,'gender':'Female','is_child':'False'}

Famille=Family(x,'Konate')
Famille.born(name='Gerome',age=5,gender='Male',is_child='True')
Famille.family_presentation()
print(Famille.is_18('Gerome'))

system("pause")


print("\n")
print("\t\t\t\tExercice2: Famille introductions")
print("\n")

class TheIncredibles(Family):
	def __init__(self):
		

