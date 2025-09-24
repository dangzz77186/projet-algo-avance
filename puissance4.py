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
