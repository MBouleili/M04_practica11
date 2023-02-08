"""
 Funció que donat un numero escrit per l'usuari i un aleatori entre 0 i 100 pel programa, retorna un missatge  de felicitació
 en cas de que el numero sigui igual al aleatori, en cas de que sigui més petit o més gran que el aleatori, et diu que es més petit o
 més gran i torna a preguntar un numero.
"""
import random

def endevinaElNumeroA():
    rangMin = 0
    rangMax = 100
    numAEndevinar = random.randrange(0, 100)

    numUsuari = input("Endevina el numero del {rangMin} al {rangMax}: ".format(rangMin = rangMin, rangMax = rangMax))

    while(int(numUsuari) != numAEndevinar):

        if(int(numUsuari) < int(numAEndevinar)):
            rangMin = numUsuari
            print("El número és més gran")

        elif(int(numUsuari) > int(numAEndevinar)):
            rangMax = numUsuari
            print("El número és més petit")

        numUsuari = input("Endevina el numero del {rangMin} al {rangMax}: ".format(rangMin=rangMin, rangMax=rangMax))
        int(numUsuari)

    print("Molt bé!. Has endevinat el número")
