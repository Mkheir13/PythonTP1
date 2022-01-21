import exo1
import exo2
import exo3
import exo4
import exo5
import exo6
import exo7
import util
from distutils import text_file
def error():
    print("")

def main():
        boulean = True                                      
        print("========== Menu Excercies Python ==========")        #affichage du menu
        print("")
        print("1 - Excercice Types prédéfinis")
        print("2 - Excercice Calcul d’une surface")
        print("3 - Excercice Somme")
        print("4 - Excercice factorielle")
        print("5 - Excercice Table multiplication")
        print("6 - Excercice Saisie de nombres et de caractères")
        print("7 - Excercice Calcul de crédit")
        print("8 - Fin")
        print("")
        while boulean:
            Exer = util.DemanderUnInput("Quelle exercice voulez vous voir?","int") #la boucle qui permet de gérer la menu
            if Exer > 0 and Exer < 9:
                match Exer:
                    case 1:
                        exo1.exo1()
                    case 2:
                        exo2.exo2()
                    case 3:
                        exo3.exo3()
                    case 4:
                        exo4.exo4()
                    case 5:
                        exo5.exo5()
                    case 6:
                        exo6.exo6()
                    case 7:
                        exo7.exo7()
                    case 8:
                        break
            else:
                print("Veuillez choisir entre 1 et 8")    #gestion d'erreur

        

#def main():
 #   Menu()
if __name__ == '__main__':
    main()