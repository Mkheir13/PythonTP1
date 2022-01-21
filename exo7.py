import util
def exo7():
    Capital = util.DemanderUnInput(("le capital emprunté : "),"int")        
    TauxAnnuel= util.DemanderUnInput(("le taux annuel : "),"int")
    Nombredans = util.DemanderUnInput(("le nombre d'années : "),"int")
    TauxMensuel = (TauxAnnuel /12 )/ 100                                #calcul du taux mensuel par rapport aux taux annuel
    NombreMois = Nombredans * 12                                        #Calcul du nombre de mois
    mensualite = Capital * TauxMensuel * ( ((1 + TauxMensuel)**NombreMois) / ((1 + TauxMensuel)**NombreMois - 1) )   #calcul de la mensualité
    mensualite = round(mensualite, 0)
    if Capital > 0 and TauxAnnuel > 0 and Nombredans > 0 and Nombredans < 12:
        print("les mensualités sont de :",mensualite)           #affichage de la mensualité