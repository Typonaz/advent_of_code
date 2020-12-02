import re

def lecture(nom_fichier):
	liste = []
	with open(nom_fichier, "r") as fichier:
		for ligne in fichier:
			liste.append(ligne)
	return liste


def règles_1(borne_min, borne_max, lettre, password): 						 
	valide = False
	compteur = 0
	for i in password :
		if i == lettre:
			compteur = compteur + 1
	if compteur >= borne_min and compteur <= borne_max :
		valide = True
	return valide


def règles_2(position_1, position_2, lettre, password):
	valide = False
	if lettre == password[position_1-1] and lettre != password[position_2-1] or lettre == password[position_2-1] and lettre != password[position_1-1]:
		valide = True
	return valide

def découpage(chaine):
	chaine_découpé = re.split(r'[-:\s]\s*', chaine)
	borne_min = int(chaine_découpé[0])
	borne_max = int(chaine_découpé[1])
	lettre = chaine_découpé[2]
	password = chaine_découpé[3]
	return(borne_min, borne_max, lettre, password)
	
	
def compteur_password(liste, nb_règle):
	compteur = 0
	for i in range(0,len(liste)):
		borne_min, borne_max, lettre, password = découpage(liste[i])
		if nb_règle == 1:
			résultat = règles_1(borne_min, borne_max, lettre, password)
		else:
			résultat = règles_2(borne_min, borne_max, lettre, password)
		if résultat == True:
			compteur = compteur + 1
	return compteur

liste = lecture("Valeurs.txt")

résultat_1 = compteur_password(liste, 1)
print(résultat_1)

résultat_2 = compteur_password(liste, 2)
print(résultat_2)






