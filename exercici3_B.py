"""Aqui introdueixes la teva edat i els teus ingressos,
i si tens més de 18 anys, i els teus ingressos són més de 1200 surt per pantalla que tens que fer la declaració,
 si no compleixes els requisits no tens que fer la declaracio."""
def hisenda():
    edat = input("Introdueix la teva edat:")
    ingressos = input("Introdueix els teus ingressos:")

    if(int(edat) >= 18 and int(ingressos) > 1200):
        print("És necessari que facis la declaració d’hisenda,"
              "ja que tens {edat} anys i els teus ingressos son de {ingressos} €.".format(edat=edat, ingressos=ingressos))
    elif(int(edat) < 18 or int(ingressos) < 1200):
        print("Encara no pots fer la declaració.")
hisenda()
