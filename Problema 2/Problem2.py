#Solução do segundo problema
#Fórmula fechada de Fibonacci 
from math import sqrt
def fibonacci(n):
    '''
    Parameters
    ----------
    n : posição n do termo da sequência de fibonacci 
    Returns
    -------
    retorna o valor do termo na posição n da sequência de fibonacci 
    '''
    return (1/sqrt(5))*(((1+sqrt(5))/2)**n - ((1-sqrt(5))/2)**n)

#Definindo qual o valor do n para um número menor que 4 milhões 
a = 0 
while fibonacci(a) <= 4*10**6:
    a = a + 1 

#O valor de há é 34
#Soma dos termos pares da seuqência de Fibonacci 
soma = 0 
for i in range(3,36,3):
    soma = soma + fibonacci(i)

print(soma)