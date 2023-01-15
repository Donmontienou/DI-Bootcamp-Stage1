from os import system

print("							Exercice1")
print(" ")

class Pets():
	def __init__(self,animals):
		self.animals=animals

	def walk(self):
		for animal in self.animals:
			print(animal.walk())

class Cat():
	is_lazy=True

	def __init__(self,name,age):
		self.name=name
		self.age=age

	def walk(self):
		return f"{self.name} is just walking around"

class Bengal(Cat):
	def sing(self,sounds):
		return f"{sounds}"

class Chartreux(Cat):
	def sing(self,sounds):
		return f"{sounds}"

class Siamese(Cat):
	def sing(self,sounds):
		return f"{sounds}"

all_cats=[Bengal("rex",2),Chartreux("milou",1),Siamese("mian",2)]
Sara_pets=Pets(all_cats)
Sara_pets.walk()

system("pause")



print("						Exercice2")

print(" ")

class Dog():
	def __init__(self,name,age,weight):
		self.name=name
		self.age=age
		self.weight=weight

	def bark(self):
		print(f"{self.name} aboie")

	def  run_speed(self):
		self.n=self.weight/self.age*10
		return self.n

	def fight(self,other_dog):
		self.other_dog=other_dog
		self.vitesse=self.n*self.weight
		if self.vitesse>other_dog.n*self.weight:
			print(f"{self.name} a la plus grande vitesse")
		else:
			print(f"{other_dog.name} a la plus grande vitesse")
		


chien1=Dog("Mian",5,12)
chien2=Dog("Bil",2,4)
chien3=Dog("Tata",4,9)

chien1.bark()
chien2.bark()
chien3.bark()

chien1.run_speed()
chien2.run_speed()
chien3.run_speed()


chien1.fight(chien2)
chien2.fight(chien3)
chien3.fight(chien1)




