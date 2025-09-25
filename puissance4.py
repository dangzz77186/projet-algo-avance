def afficher_grille(grille):
    # Affiche la grille du jeu de Puissance 4
    for ligne in grille:
        ligne_affichee = '| '
        for cell in ligne:
            ligne_affichee += cell + ' | '  # Chaque cellule affichée avec des séparateurs
        print(ligne_affichee)
    # Affiche une ligne de séparation horizontale
    print('-' * (len(grille[0]) * 4 + 1))

    # Affiche les numéros de colonnes sous la grille
    nums = ' '
    for i in range(len(grille[0])):
        nums += ' ' + str(i) + '  '
    print(nums)


def verifier_victoire(grille, symbole):
    # Vérifie s'il y a une victoire horizontale
    for ligne in grille:
        for i in range(len(ligne) - 3):
            if ligne[i] == symbole and ligne[i+1] == symbole and ligne[i+2] == symbole and ligne[i+3] == symbole:
                return True

    # Vérifie s'il y a une victoire verticale
    for col in range(len(grille[0])):
        for lig in range(len(grille) - 3):
            if (grille[lig][col] == symbole and grille[lig+1][col] == symbole and
                grille[lig+2][col] == symbole and grille[lig+3][col] == symbole):
                return True

    # Vérifie une victoire diagonale descendante (du haut-gauche vers bas-droite)
    for lig in range(len(grille) - 3):
        for col in range(len(grille[0]) - 3):
            if (grille[lig][col] == symbole and grille[lig+1][col+1] == symbole and
                grille[lig+2][col+2] == symbole and grille[lig+3][col+3] == symbole):
                return True

    # Vérifie une victoire diagonale montante (du bas-gauche vers haut-droite)
    for lig in range(3, len(grille)):
        for col in range(len(grille[0]) - 3):
            if (grille[lig][col] == symbole and grille[lig-1][col+1] == symbole and
                grille[lig-2][col+2] == symbole and grille[lig-3][col+3] == symbole):
                return True

    return False  # Pas de victoire détectée


def jouer_coup(grille, colonne, symbole):
    # Place le symbole dans la colonne choisie en partant du bas
    for i in range(len(grille)-1, -1, -1):  # On part de la dernière ligne (le bas)
        if grille[i][colonne] == ' ':
            grille[i][colonne] = symbole
            return True  # Coup validé
    return False  # Colonne pleine, coup impossible


def puissance4():
    # Initialisation de la grille de 6 lignes x 7 colonnes
    lignes = 6
    colonnes = 7
    grille = []
    for i in range(lignes):
        ligne = []
        for j in range(colonnes):
            ligne.append(' ')  # Case vide
        grille.append(ligne)

    tour = 0  # Compteur de tours
    joueurs = ['X', 'O']  # Symboles des joueurs

    # Boucle principale du jeu
    while True:
        afficher_grille(grille)  # Afficher la grille
        symbole = joueurs[tour % 2]  # Détermine le joueur (X ou O)

        # Demande au joueur de saisir un numéro de colonne
        colonne_str = input('Joueur ' + symbole + ', entrez le numéro de la colonne (0-' + str(colonnes - 1) + '): ')

        # Vérifier la validité de l’entrée (doit être un nombre)
        if not colonne_str.isdigit():
            print('Entrée invalide, entrez un nombre.')
            continue

        colonne = int(colonne_str)

        # Vérifie si la colonne est dans la plage valide
        if colonne < 0 or colonne >= colonnes:
            print('Colonne invalide, réessayez.')
            continue

        # Essaye de jouer le coup dans la colonne choisie
        if not jouer_coup(grille, colonne, symbole):
            print('Cette colonne est pleine, réessayez.')
            continue

        # Vérifie si le joueur courant a gagné
        if verifier_victoire(grille, symbole):
            afficher_grille(grille)
            print('Le joueur ' + symbole + ' a gagné !')
            break

        # Vérifie si la grille est pleine
        plein = True
        for c in range(colonnes):
            if grille[0][c] == ' ':
                plein = False
                break
        if plein == True:
            afficher_grille(grille)
            print('Match nul !')
            break

        # Passage au joueur suivant
        tour += 1
# Lancement du jeu
puissance4()
