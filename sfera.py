import math

print "Inserisci il raggio : "
raggio = input()

superficie = 4. * math.pi * (raggio * raggio)
volume = 4. / 3. * math.pi * (raggio * raggio * raggio)

print "La superficie della sfera e' : ", superficie , "e il volume e' : ", volume
