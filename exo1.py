from distutils import text_file
import util
def exo1():                                                             #Je définie une fonction pour plus tard l'appeler dans mon menu
    txt_cara = util.DemanderUnInput(("rentrer un caractère :"),"chr")   #je vais utiliser ma fonction pour demander un input pour récupérer un caractère
    boulean = True                                                             
    while boulean:                                                      # je crée une boucle pour pouvoir gérer la limite
        txt_entier = util.DemanderUnInput(("rentrer un entier :"),"int") #je demande un entier
        if txt_entier > 0 and txt_entier < 1114111:                     #je crée ma limite
            boulean = False
            print(txt_cara, "vaut", ord(txt_cara))
            print(txt_entier, "vaut", chr(txt_entier))
        else:                                                           #je demande la limite au cas le nombre est négatif ou trop gros
            print("L'entier doit être compris entre 0 et 1114111")