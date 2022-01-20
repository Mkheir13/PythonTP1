def my_function_5():
    nombre = ""
    bol = True
    str_nombre = ""
    nombre_calc = 1
    while bol:
        try:
            nombre = int(input("rentrer un entier positif: "))
        except:
                continue
        résultat = nombre * nombre_calc
        print("Exemple Table de ", nombre, ":")
        while bol:
            résultat = nombre * nombre_calc
            print(nombre, " x ", nombre_calc, " = ", résultat)
            nombre_calc += 1
            if nombre_calc == 11:
                bol = False
