def afficher_grille(grille):
    for ligne in grille:
        ligne_affichee = '| '
        for cell in ligne:
            ligne_affichee += cell + ' | '
        print(ligne_affichee)
    print('-' * (len(grille[0]) * 4 + 1))

    nums = ' '
    for i in range(len(grille[0])):
        nums += ' ' + str(i) + '  '
    print(nums)

def verifier_victoire(grille, symbole):
    for ligne in grille:
        for i in range(len(ligne) - 3):
            if ligne[i] == symbole and ligne[i+1] == symbole and ligne[i+2] == symbole and ligne[i+3] == symbole:
                return True
    for col in range(len(grille[0])):
        for lig in range(len(grille) - 3):
            if (grille[lig][col] == symbole and grille[lig+1][col] == symbole and
                grille[lig+2][col] == symbole and grille[lig+3][col] == symbole):
                return True
    for lig in range(len(grille) - 3):
        for col in range(len(grille[0]) - 3):
            if (grille[lig][col] == symbole and grille[lig+1][col+1] == symbole and
                grille[lig+2][col+2] == symbole and grille[lig+3][col+3] == symbole):
                return True
    for lig in range(3, len(grille)):
        for col in range(len(grille[0]) - 3):
            if (grille[lig][col] == symbole and grille[lig-1][col+1] == symbole and
                grille[lig-2][col+2] == symbole and grille[lig-3][col+3] == symbole):
                return True
    return False


def jouer_coup(grille, colonne, symbole):
    for i in range(len(grille)-1, -1, -1):
        if grille[i][colonne] == ' ':
            grille[i][colonne] = symbole
            return True
    return False

def puissance4():
    lignes = 6
    colonnes = 7
    grille = []
    for i in range(lignes):
        ligne = []
        for j in range(colonnes):
            ligne.append(' ')
        grille.append(ligne)

    tour = 0
    joueurs = ['X', 'O']

    while True:
        afficher_grille(grille)
        symbole = joueurs[tour % 2]

        colonne_str = input('Joueur ' + symbole + ', entrez le numéro de la colonne (0-' + str(colonnes - 1) + '): ')

        if not colonne_str.isdigit():
            print('Entrée invalide, entrez un nombre.')
            continue

        colonne = int(colonne_str)

        if colonne < 0 or colonne >= colonnes:
            print('Colonne invalide, réessayez.')
            continue

        if not jouer_coup(grille, colonne, symbole):
            print('Cette colonne est pleine, réessayez.')
            continue

        if verifier_victoire(grille, symbole):
            afficher_grille(grille)
            print('Le joueur ' + symbole + ' a gagné !')
            break

        plein = True
        for c in range(colonnes):
            if grille[0][c] == ' ':
                plein = False
                break
        if plein == True:
            afficher_grille(grille)
            print('Match nul !')
            break

        tour += 1
puissance4()
