def tabuada(n):
    if (n<=0):
        print('Informe um numero valido')
    else:
        for multiplicador in range(1,11):
            resultado = multiplicador * n
            print (n,"x",multiplicador,"=",resultado)
    
