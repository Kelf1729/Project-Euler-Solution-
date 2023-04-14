#Solução do primeiro problema
def somatorio(n,r):
    '''
    Parameters
    ----------
    n : número de termos do somatório
    r : razão entre os termos, como o primeiro termo
    tem o mesmo valor razão, igualei
    Returns
    -------
    resultado do somatório
    '''
    return 0.5*(n*(2*r+r*(n-1)))

print(somatorio(333, 3)+somatorio(199, 5)-somatorio(66, 15))