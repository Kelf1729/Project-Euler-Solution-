#Problema 6 
def soma_potencia(n):
    return (n*(n+1)*(2*n+1))/6

def soma_PA(n):
    return ((n*(1+n))/2)**2

print(soma_PA(100) - soma_potencia(100))