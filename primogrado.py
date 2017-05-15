print "Inserisci a e b per svolgere un equazione di primo grado "
a = input("Inserisci a : ")
b = input("Inserisci b : ")

if a==0 and b==0 :

    print " a e b sono uguali a 0 , quindi l'equazione ammette infinite soluzioni. "

elif a == 0 :

    print " a e' uguale a 0 , quidi il risultato dell'equazione e' impossibile . "


else :

    x = -float(b)/float(a)
    print " L'incognita x con a ",a," e b ",b," ha valore : ",x
