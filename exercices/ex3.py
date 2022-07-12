for n in range (1,100):

    u0 = n 
    k = 0 
    m = 0
    tmpVolAlt = 0
    while n!=1:
        if n%2==0:
            n=n//2
        else :
            n = 3*n +1
        if n> m :
            m = n
        if n <= u0 and  tmpVolAlt == 0 :
            tmpVolAlt = k 
        k+=1
    
    print("temps de vol",k)
    print("valeur max ",m)
    print("temps de vol en altitude ",tmpVolAlt)