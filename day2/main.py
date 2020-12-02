import re

def lecture(nom_fichier):
	liste = []
	with open(nom_fichier, "r") as fichier:
		for ligne in fichier:
			liste.append(ligne)
	return liste


def regles_1(borne_min, borne_max, lettre, password): 						 
	valide = False
	compteur = 0
	for i in password :
		if i == lettre:
			compteur = compteur + 1
	if compteur >= borne_min and compteur <= borne_max :
		valide = True
	return valide


def regles_2(position_1, position_2, lettre, password):
	valide = False
	if lettre == password[position_1-1] and lettre != password[position_2-1] or lettre == password[position_2-1] and lettre != password[position_1-1]:
		valide = True
	return valide

def decoupage(chaine):
	chaine_decoupe = re.split('[-: ]+', chaine)
	borne_min = int(chaine_decoupe[0])
	borne_max = int(chaine_decoupe[1])
	lettre = chaine_decoupe[2]
	password = chaine_decoupe[3]
	return(borne_min, borne_max, lettre, password)
	
	
def compteur_password(liste, nb_regle):
	compteur = 0
	for i in range(0,len(liste)):
		borne_min, borne_max, lettre, password = decoupage(liste[i])
		if nb_regle == 1:
			resultat = regles_1(borne_min, borne_max, lettre, password)
		else:
			resultat = regles_2(borne_min, borne_max, lettre, password)
		if resultat == True:
			compteur = compteur + 1
	return compteur

liste = lecture("Valeurs.txt")

resultat_1 = compteur_password(liste, 1)
print(resultat_1)

resultat_2 = compteur_password(liste, 2)
print(resultat_2)






