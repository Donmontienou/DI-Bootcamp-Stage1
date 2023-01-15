from os import system
import random

print("\t\t\t\tEXERCICE 1")
def display_message():
	print("Nous avons vu:\nLa syntaxe d'une fonction\nLes fonctions Lambda,Map,Reduce,Filter")
display_message()
system("pause")

print("\t\t\t\tEXERCICE 2")
def favorite_book(title):
	print("One of my favorite books is", title)
favorite_book("Une si longue lettre de Mariama BA")


print("\t\t\t\tEXERCICE 3")
def describe_city(city,country):
	print(f"{city} est au {country}")
describe_city("Diebougou","Burkina_Faso")
system("pause")
def describe_city(city,country="Ghana"):
	print(f"{city} est au {country}")
describe_city("Kumasi")
system("pause")




print("\t\t\t\tEXERCICE 5")
def make_shirt(taille,texte):
	print(f"La taille de mon tee-shirt est {taille} et le texte est {texte}")
make_shirt("M","Royalty")
system("pause")

def make_shirt(taille,texte="restes determiner!"):
	print(f"Le texte et la taille d'une chemise {taille} et {texte}")
make_shirt("xxL")
system("pause")

def make_shirt(taille,texte="restes determiner!"):
	print(f"Le texte et la taille d'une chemise {taille} et {texte}")
make_shirt("L")
system("pause")

def make_shirt(taille,texte="restes determiner!"):
	print(f"Chemise de n'importe quelle taille {taille} et {texte}")
make_shirt("XXXL","l'union fait la force")
system("pause")


print("\t\t\t\tEXERCICE 6")
magician_names=["Harry Houdini","David BLZINE","Criss Angel"]
def show_magicians(magician_names):
	for names in magician_names:
		print(names)
show_magicians(magician_names)

system("pause")
def make_great(magician_names):
	#x=" the Great"
	i=0
	for name in magician_names:
		magician_names[i]=name+" the Great"
		i+=1
make_great(magician_names)
show_magicians(magician_names)
system("pause")

print("\t\t\t\tEXERCICE 7")
print("Question 1")
def get_random_temp():
	return random.randint(-10,40)
get_random_temp()
print(get_random_temp())
system("pause")

print("Question 2")
def main():
	v=get_random_temp()
	print(f"la temperature actuelle est {v}")
main()
system("pause")

print("Question 3")

def main():
	v=get_random_temp()
	if v<0:
		print(f"{v} c'est glacial! porter des couches supplementaires aujourd'hui")
	elif 0<=v<16:
		print(f"{v} c'est assez froid! N'oubliez pas votre manteau")
	elif 16<=v<=23:
		print(f"{v} c'est moyen vous pouvez laisser votre manteau")
	elif 24<=v<32:
		print(f"{v} c'est un peu chaud")
	else:
		print(f"{v} c'est brulant!!!")
main()
system("pause")


