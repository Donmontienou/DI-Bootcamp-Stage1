from os import system

print("				EXERCICE1")
class Cat():
	def __init__(self,cat_name,cat_age):
		self.name=cat_name
		self.age=cat_age
		
cat1=Cat(cat_name="Rex",cat_age=3)
cat2=Cat(cat_name="Milou",cat_age=6)
cat3=Cat(cat_name="Mec",cat_age=2)

cats=[cat1,cat2,cat3]
def oldest():
	cat=cats[0]
	for i in range(len(cats)):
		if cats[i].age > cat.age:
			cat=cats[i]
	print(f"le chat le plus agé est {cat.name} son âge est {cat.age} ans")
oldest()
system("pause")


print("				EXERCICE2")

class Dog:
	def __init__(self,name,height):
		self.name=name
		self.height=height

	def bark(self):
		print(f"{self.name} va woof!")

	def jump(self):
		x=self.height*2
		print(f"{self.name} saute {x} cm de haut!")

davids_dog=Dog(name="Rex",height=50)
davids_dog.bark()
davids_dog.jump()

system("pause")

sarahs_dog=Dog(name="Teacup",height=20)
sarahs_dog.bark()
sarahs_dog.jump()

system("pause")

Dogs=[davids_dog,sarahs_dog]
if Dogs[0].height > Dogs[1].height:
	print(f"Le plus gros chien est {Dogs[0].name}")
else:
	print(f"Le plus gros chien est {Dogs[1].name}")
system("pause")

print("				EXERCICE3")
class Song():
	def __init__(self,lyrics):
		self.lyrics=lyrics

	def sing_me_a_song(self):
		for lyric in self.lyrics:
			print(lyric)
stairway=Song(["There's a lady who 's sure",
"all that glitters is gold",
"and she's buying a stairway to heaven"])
stairway.sing_me_a_song()
system("pause")

