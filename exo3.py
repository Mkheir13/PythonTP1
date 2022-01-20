def my_function_3():
    nombre = ""
    bol = True
    str_nombre = ""
    boll = True
    résultat = 0
    while bol:
        try:
            nombre = int(input("rentrer un entier positif: "))
        except:
                continue
        if nombre >= 0:
            bol = False
            while boll:
                str_nombre += str(nombre) +  " + "
                résultat += nombre
                nombre -= 1
                if nombre <= 0:
                    boll = False

        print(str_nombre[0: len(str_nombre) - 3][:: - 1], "=", résultat)
        print(résultat, "=", str_nombre[0: len(str_nombre) - 3][:: -1])
