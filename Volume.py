import math

print "Inserisci 1 per calcolare il volume del cubo , inserisci 2 per calcolare il volume della sfera : "

scelta = input()

if scelta == 1 :

    lato = input("Inserisci le misure del lato del cubo : ")
    vcubo = lato*lato*lato
    print "Il volume del cubo di lato ", lato ," e' : ",vcubo

elif scelta == 2 :

    raggio = input("Inserisci le misure del raggio della sfera : ")
    vsfera = 4. / 3. * math.pi * (raggio * raggio * raggio)
    print "Il volume della sfera di raggio ",raggio," e' : ",vsfera

elif scelta > 2 or  scelta < 1 :

    print "La scelta effettuata non corrisponde a nessuna azione. "

