import util
import math
def exo6():
    logarithme = ""
    bol = True
    while bol:
            logarithme = util.DemanderUnInput(("rentrer un entier positif: "),"int")
            if logarithme >= 0:
                bol = False        
    print("logarithme de l'entier =", math.log(logarithme))         #affichage des fonctions log
    print("sinus de l'entier = ", math.sin(logarithme))
    print("cosinus de l'entier = ", math.cos(logarithme))
