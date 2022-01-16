def suma(a,b):
    try:
        r=a+b
    except TypeError:
        print("Error! los valores que has introducido no son de tipo numérico")
    else:
        print("La suma de {} y {} es: {}".format(a,b,r))

 
def resta(a,b):
    try:
        r=a-b
    except TypeError:
        print("Error! los valores que has introducido no son de tipo numérico")
    else:
        print("La resta de {} menos {} es: {}".format(a,b,r))


def producto(a,b):
    try:
        r=a*b
    except TypeError:
        print("Error! los valores que has introducido no son de tipo numérico")
    else:
        print("La multiplicación de {} por {} es: {}".format(a,b,r))


def division(a,b):
    try:
        r=a/b
    except TypeError:
        print("Error! los valores que has introducido no son de tipo numérico")
    except ZeroDivisionError:
        print("Error! Has dividido tu número entre 0")
    else:
        print("la división de {} entre {} es: {}".format(a,b,r))


def potencia(a,b):
    try:
        r=a**b
    except TypeError:
        print("Error! los valores que has introducido no son de tipo numérico")
    else:
        print("la potencia de {} elevado a {} es: {}".format(a,b,r))