from os import system

print("\n")
print("\t\t\t\tExercice Defi 1")
print("\n")
print("Ancienne Ferme de MacDonald")
print("\n")

class Farm():
    def __init__(self,name):
        self.name=name
        self.liste={}

    def get_info(self):
        for x,y in self.liste.items():
            print(x,":",y)
        
    def add_animal(self,name,nombre=1):
        if name in self.liste:
            self.liste[name]=nombre+nombre
        else:
            self.liste[name]=nombre


    def get_short_type(self):
       noms=[]
       for name in self.liste:
        noms.append(name)
        noms=sorted(noms)
       print(noms)
       return noms

    def get_short_info(self):
        print(f"La ferme McDonald possède des: {self.get_short_type()}")

macdonald=Farm("McDonald")  
macdonald.add_animal('Cow',5)
macdonald.add_animal('Sheep')
macdonald.add_animal('Sheep')
macdonald.add_animal('Goat',12)
macdonald.get_info()
macdonald.get_short_type()
macdonald.get_short_info()