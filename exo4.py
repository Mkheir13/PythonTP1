def my_function_4():
    nombre = ""
    bol = True
    str_nombre = ""
    boll = True
    résultat = 1
    while bol:
        try:
            nombre = int(input("rentrer un entier positif: "))
            nombreaffich = nombre
        except:
                continue
        if nombre >= 0:
            bol = False
            while boll:
                str_nombre += str(nombre) +  " x "
                résultat *= nombre
                nombre -= 1
                if nombre <= 0:
                    boll = False

        print("la factorielle de ", nombreaffich, ", notée ", nombreaffich, "!, et vaut :")
        print(str_nombre[0: len(str_nombre) - 3][:: -1], "=", résultat)
        print(résultat, "=", str_nombre[0: len(str_nombre) - 3][:: -1])