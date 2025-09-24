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
