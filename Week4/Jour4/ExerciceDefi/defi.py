import os
import re
import string
nbr=string.digits
signe=string.punctuation
caractere=""
x=""
y=""
matrice =[["7i3"],["Tsi"],["h%x"],["i #"],["sM "],["&a "],["#t%"],["^r!"]]
for liste in matrice:
    chaine="".join(liste)
    caractere=caractere+chaine[0]
    c=caractere
    x=x+chaine[1]
    c=c+x
    y=y+chaine[2]
    c=c+y
    for elem in c:
        if elem in nbr:
            c=c.replace(elem,"")

        elif elem in signe:
            c=c.replace(elem," ")
        else:
            c=c+elem
print(c)

"""

    
    sc_list = '[@_!#$%^&*()<>?}{~:  ]
    res=re.findall(sc_list,chai)
    rese=re.sub(sc_list,' ',chai)
    chaine_liste=list(rese)
    dig=[]
    for sy in chaine_liste:
        if sy.isdigit():
            dig.append(sy)
    for d in dig:
        chaine_liste.remove(d)
    return "".join(chaine_liste)

print(f"\nDecripter vos messages comme par exemple le  text du tableau ci dessus :\n \t Resultat ======>>> {decriptage(chaine)}\n")

def main():
    chain=input("\nEntrer une chaine :")
    print(f"\nLe message est :\n=======>>> {decriptage(chain)}")

main()
os.system("pause")
"""
