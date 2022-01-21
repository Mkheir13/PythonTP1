import util
def exo3():                 #je prépare mes variables que je vais utiliser 
    nombre = ""
    bol = True
    str_nombre = ""
    boll = True
    résultat = 0
    while bol:
        nombre = util.DemanderUnInput(("rentrer un entier positif: "),"int")
        if nombre >= 0:                                                         #gestion du nombre négatif
            bol = False                                     
            while boll:
                str_nombre += str(nombre) +  " + "                              #mise en place du calcul
                résultat += nombre
                nombre -= 1
                if nombre <= 0:
                    boll = False
        print(str_nombre[0: len(str_nombre) - 3][:: - 1], "=", résultat)        #affichage du calcul dans l'ordre croissant
        print(résultat, "=", str_nombre[0: len(str_nombre) - 3][:: -1])         #puis décroissant
