"""
 Funció que donat dos numeros de l'usuari amb un input, retorna un missatge dïent quin es el més petit i quin es
 el més gran.
"""
def comparaNumerosA():
    num1 = input("Insereix un numero: ")
    num2 = input("Insereix altre numero: ")

    int(num1)
    int(num2)

    if(num1 < num2):
        return('El número {num1} és el més petit i el número {num2}, el més gran'.format(num1 = num1, num2 = num2))
    elif(num2 < num1):
        return('El número {num2} és el més petit i el número {num1}, el més gran'.format(num1 = num1, num2 = num2))
    else:
        return('Els números son iguals')
