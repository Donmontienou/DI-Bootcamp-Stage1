from os import system
matrice=[
			["7","T","h","i","s","$","#","^"],
			["i","s","%"," ","M","a","t","r"],
			["3","i","x","#"," "," ","%","!"]
		]
chaine=""
x=0
for m in matrice:
	for n in m:
		if n.isalpha():
			chaine+=n
		else:
			x+=1
			if x==2:
				chaine+=" "
				x=0
print(chaine)