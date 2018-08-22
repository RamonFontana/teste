
def tabuada(n):
    if (n<=0):
        print('Informe um numero valido')
    else:
        for multiplicador in range(1,11):
            resultado = multiplicador * n
            print (n,"x",multiplicador,"=",resultado)

def exibiLista(lista):
    print(lista)

def somaLista(lista1,lista2):
    x = sum(lista1)+sum(lista2)
    print(x)

    
