import re

def lecture(nom_fichier):
	file = open(nom_fichier)
	lines = file.read().splitlines()
	file.close()
	return lines


def regles_1(borne_min, borne_max, lettre, password): 						 
	compteur = 0
	for char in password:
		if char == lettre:
			compteur = compteur + 1
	return compteur >= borne_min and compteur <= borne_max
		

def regles_2(position_1, position_2, lettre, password):
	return (lettre == password[position_1-1]) != (lettre == password[position_2-1])
	

def regles(position_1, position_2, lettre, password, num_regle):
	if num_regle == 1:
		return regles_1(position_1, position_2, lettre, password)
	else:
		return regles_2(position_1, position_2, lettre, password)
		  

def decoupage(chaine):
	chaine_decoupee = re.split('[-: ]+', chaine)
	borne_min = int(chaine_decoupee[0])
	borne_max = int(chaine_decoupee[1])
	lettre = chaine_decoupee[2]
	password = chaine_decoupee[3]
	return (borne_min, borne_max, lettre, password)
	
	
def compteur_password(liste, num_regle):
	compteur = 0
	for ligne in liste:
		borne_min, borne_max, lettre, password = decoupage(ligne)
		if regles(borne_min, borne_max, lettre, password, num_regle):
			compteur += 1
	return compteur

liste = lecture("Valeurs.txt")

print("résultat puzzle 1:", compteur_password(liste, 1))

print("résultat puzzle 2:", compteur_password(liste, 2))
