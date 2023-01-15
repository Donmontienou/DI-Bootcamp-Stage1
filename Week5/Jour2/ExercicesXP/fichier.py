import random
from xp import Dog

class PetDog(Dog):
	def __init__(self,name,age,weight,trained=False):
		self.trained=trained
		super().__init__(name,age,weight)

	def train(self):
		self.trained=True
		print(f"{self.name} aboie")

	def play(self,*args):
		for elem in args:
			print(elem,end=",")
		print("jouent tous ensemble")

	def do_a_trick(self):
		liste=["fait un tonneau","se dresse sur ses pattes arrière","te serre la main","fait le mort"]
		random.shuffle(liste)
		self.x=random.choice(liste)
		if self.trained==True:
			print(f"{self.name} {self.x}")
		else:
			pass

chien=PetDog("chic",2,1,True)
chien.train()
chien.play("rex","milou","cao","tac","pie")
chien.do_a_trick()

