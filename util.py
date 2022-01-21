from turtle import clear


def CastageInput(val, testType): #Va caster un input dans le type demander
    try:
        if testType == "int": #un nombre entier
            return int(val)
        elif testType == "float": #un nombre décimal
            return float(val)
        elif testType == "chr": #un caractère
            if len(val) == 1:
                return val
        else:
            return None
    except:
        return None


def DemanderUnInput(message, leType):
    resultat = None
    while resultat == None:
        notreInput = input(message)   #va demander un input delon le message
        resultat = CastageInput(notreInput, leType) #va caster l'input dans le bon type
    return resultat #renvoie l'input caster