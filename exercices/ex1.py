import math

def est_premier(p):
    """"
    Retourne si p est premier

    Args : 
        p: valeur entière positif

    Returns: 
        booléen

    >>>est_premier(1)
    True
    >>est_premier(9)
    False

    """
    premier = True
    a= int(math.sqrt(p))+1
    for d in range (2,a) :
        if p % d == 0 :
            premier = False
            ##print (p," = ", d," x ", int(p/d) ,":", premier)
            break
    ##print(p, ":", premier)
    return premier

def next_prime():
    x = int(input("entrez une valeur: "))
    premier = False 
    i=0
    while premier != True :
        x+=1
        premier = est_premier(x)       
    print(x," est premier")

def twin_prime():
    x = int(input("entrez une valeur: "))
    premier = False 
    
    while not premier : 
        x =x+ 1 
        premier = est_premier(x)
        if premier and est_premier(x+2):
            print("break")
            break
    print(x,"et ",x+2,"sont des nombres premiers jumeaux ")

def germain_prime():
    x = int(input("entrez une valeur: "))
    premier = False 
    
    while not premier : 
        x =x+ 1 
        premier = est_premier(x)
        if premier and est_premier(2*x+1):
            print("break")
            break
    print(x,"et ",2*x+1,"sont des nombres premier de Germain ")


print(est_premier(2**2**0 + 1))
next_prime()
twin_prime()
germain_prime()

