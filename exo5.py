import util
def exo5():
    nombre = ""
    bol = True
    str_nombre = ""
    nombre_calc = 1
    while bol:
        nombre = util.DemanderUnInput(("rentrer un entier positif: "),"int")
        résultat = nombre * nombre_calc
        print("Exemple Table de ", nombre, ":")      #Exemple des tables de mutiplication
        while bol:
            résultat = nombre * nombre_calc          #Exécution de la table de mutlriplication
            print(nombre, " x ", nombre_calc, " = ", résultat) #Affichage de la table de mutiplication
            nombre_calc += 1
            if nombre_calc == 11:                   #Arret du calcul
                bol = False
