import util
def exo4():
    nombre = ""
    bol = True
    str_nombre = ""
    boll = True
    résultat = 1
    while bol:
        nombre = util.DemanderUnInput(("rentrer un entier positif: "),"int")
        nombreaffich = nombre
    if nombre >= 0:
        bol = False
        while boll:
            str_nombre += str(nombre) +  " x "    #variable string du calcul
            résultat *= nombre                    #calcul de la variable
            nombre -= 1
            if nombre <= 0:
                boll = False
    print("la factorielle de ", nombreaffich, ", notée ", nombreaffich, "!, et vaut :") #affichage du calcul
    print(str_nombre[0: len(str_nombre) - 3][:: -1], "=", résultat) #affichage du calcul dans l'ordre croissant 
    print(résultat, "=", str_nombre[0: len(str_nombre) - 3][:: -1]) #affichage du calcul puis décroissant