def my_function_6():
    logarithme = ""
    bol = True
    while bol:
        try:
                logarithme = int(input("rentrer un entier positif: "))
        except:
                continue
        if logarithme >= 0:
            bol = False
            
        print("logarithme de l'entier =", math.log(logarithme))
        print("sinus de l'entier = ", math.sin(logarithme))
        print("cosinus de l'entier = ", math.cos(logarithme))
