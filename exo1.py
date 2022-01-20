def my_function_1():
    txt_cara = input("rentrer un caractère :")
    while len(txt_cara) > 1:
        print("Veuillez rentrer un seul caractère !")
        txt_cara = input("rentrer un caractère:")

    txt_entier = ""
    boulean = True
    while boulean:
        try:
            txt_entier = int(input("rentrer un entier :"))
        except:
            continue

        if txt_entier > 0 and txt_entier < 1114111:
            boulean = False
            print(txt_cara, "vaut", ord(txt_cara))
            print(txt_entier, "vaut", chr(txt_entier))