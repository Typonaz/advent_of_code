def lecture(nom_fichier):
	liste = []
	with open(nom_fichier, "r") as fichier:
		for ligne in fichier:
			liste.append(int(ligne))
	return liste


def challenge_1(arr):
	for i in range (0, len(arr)):
		for j in range (i+1 , len(arr)):
			if arr[i] + arr[j] == 2020:
				return (arr[i], arr[j])


def challenge_2(arr):
	for i in range (0, len(arr)):
		for j in range (i+1 , len(arr)):
			for k in range (j+1, len(arr)):
				if arr[i] + arr[j] + arr[k] == 2020:
					return (arr[i], arr[j], arr[k])
		

liste = lecture("Valeurs.txt")
entry1, entry2 = challenge_1(liste)
print("challenge 1 answer =", entry1 * entry2)

entry1, entry2, entry3 = challenge_2(liste)
print("challenge 2 answer =", entry1 * entry2 * entry3)
