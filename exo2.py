import util


def exo2():
    boulean = True
    while boulean:                                                                  #boucle pour gérer les erreurs 
        surfaceA = util.DemanderUnInput(("rentrer la taille de A en m: "),"int")    #Demande de chaque mesure 
        surfaceB = util.DemanderUnInput(("rentrer la taille de B en m: "),"int")
        surfaceC = util.DemanderUnInput(("rentrer la taille de C en m: "),"int")
        surfaceTrapeze = ((surfaceA + surfaceB) * surfaceC * 0.5)                   #Calcule de l'aire d'un trapèse 
        if surfaceA > 0 and surfaceB > 0 and surfaceC > 0:                          #Condition permettant d'empécher les nombres négatif
            boulean = False
            print("La surface du trapèze est de ", surfaceTrapeze, "m²" )
