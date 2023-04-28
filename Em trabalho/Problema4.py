#solução do quarto problema
"""
#-----------------------------ok esse aqui 
#solução força bruta crescente 
maior = 0 
for i in range(100,1000):
    for j in range(100,1000):
        num = str(i*j)
        num_invertido = num[::-1]
        if num == num_invertido and i*j > maior: 
            maior = i*j
            
            
print(maior) #Solução força bruta

"""
#-----------------------------
#solução força bruta decrescente 
i = 999
j = 999
while i >= 100 and j >= 100:
    produto = i * j
    if str(produto) == str(produto)[::-1]:
        print(f"O produto {i} x {j} = {produto} é um palíndromo!")
        break
    j -= 1
    if j < 100:
        i -= 1
        j = 999

#-----------------------------
"""

#teste 
#solução matemática ok esse aqui 
maior = 0 
ciclos = 0 
for i in range(1000,100,-1):
    for j in range(1000,100,-1):
        if i % 11 == 0 or j % 11 == 0:
            num = str(i*j)
            num_invertido = num[::-1]
            if num == num_invertido and i*j > maior: 
                ciclos += 1 #Número de palindromos achados 
                print(i,j)
                maior = i*j
            continue 
print(maior,ciclos) #Solução matemática 
"""