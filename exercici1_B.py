""""En aquest exercici el que fem es introduir dos numeros
 on si un es més gran que l'altre imprimeix un text,
 i si son iguals no imprimeix res. """
def granIPetitit():
    a = input("Escriu un número:")
    b = input("Escriu un altre:")
    if(a > b):
        print("El {a} és més gran què {b}".format(a=a, b=b))
    elif(a < b):
        print("El {b} és més gran què {a}".format(b=b, a=a))
    else:
        print("")
granIPetitit()