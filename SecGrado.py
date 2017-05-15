import math

print "Inserisci a , b e c per risolvere l'equazioni di secondo grado "

a = input(" a: ")
b = input(" b: ")
c = input(" c: ")

if a==0 and b==0 and c==0 :
    
    print " a , b e c sono = 0 quindi l'equazione ammette infinite soluzioni"

elif a==0 and b==0 :
    
    print " L'equazione ha c = 0 quindi non ammette soluzioni"

elif a==0 :
    
    print "L'equazione ha a=0 quindi diventa di primo grado"
    print "Risultato : ", -float(c) / float(b)

else :
    
    delta = b * b - 4 * a * c
    
    if delta < 0 :
        
	print "Delta < 0 quindi l'equazione non ha soluzioni"
        
    elif delta == 0:
        
	print "Delta = 0 , quindi l'equazione ha un solo risultato cioe' x = ", -float(b) / (2.0 * float(a))
        
    else:
        print "L'equazione ammette due soluzioni :"
        rdelta = math.sqrt(delta)
        print "x1 = ", (-float(b) + rdelta) / (2.0 * float(a))
        print "x2 = ", (-float(b) - rdelta) / (2.0 * float(a))
