"""En aquest exercici el que fem és introduir un número,
 i imprimeix si és parell o senar."""
def parellOSenar():
    num = input("Introdueix un numero:")

    if(int(num) % 2 ) == 0 :
        print("El {num} és parell".format(num=num))
    else:
        print("El {num} és senar".format(num=num))

parellOSenar()