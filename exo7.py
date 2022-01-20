def my_function_7():
    Capital = ""
    TauxAnnuel = ""
    Nombredans = ""
    boulean = True
    while boulean:
        try:
            Capital = int(input("le capital emprunté : "))
            TauxAnnuel= int(input("le taux annuel : "))
            Nombredans = int(input("le nombre d'années : "))
        except:
            continue
        TauxMensuel = (TauxAnnuel /12 )/ 100
        NombreMois = Nombredans * 12
        mensualite = Capital * TauxMensuel * ( ((1 + TauxMensuel)**NombreMois) / ((1 + TauxMensuel)**NombreMois - 1) )
        mensualite = round(mensualite, 0)
        if Capital > 0 and TauxAnnuel > 0 and Nombredans > 0 and Nombredans < 12:
            boulean = False

        print(mensualite)