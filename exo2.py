def my_function_2():
    surfaceA = ""
    surfaceB = ""
    surfaceC = ""
    boulean = True
    while boulean:
        try:
            surfaceA = int(input("rentrer la taille de A: "))
            surfaceB = int(input("rentrer la taille de B: "))
            surfaceC = int(input("rentrer la taille de C: "))
        except:
            continue
            
        surfaceTrapeze = ((surfaceA + surfaceB) * surfaceC * 0.5)
        if surfaceA > 0 and surfaceB > 0 and surfaceC > 0:
            boulean = False
            print("La surface du trapèze est de ", surfaceTrapeze, "m²" )
