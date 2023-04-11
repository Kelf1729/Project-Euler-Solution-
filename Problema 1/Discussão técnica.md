[Problema 1](https://projecteuler.net/problem=1)

## Descrição do problema
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

## Discussão técnica 
Ao analisar o problema temos que encontrar todos os números múltiplos de 3 e de 5 de tal forma que eles sejam inferiores a 1000. 
Como queremos múltiplos de 3, podemos considerar que existe uma sequência 3,6,9 ... logo, sendo uma PA de ordem 3, o mesmo ocorre analisando a sequência de múltiplos para o número 5

Contudo entre os múltiplos de 3 ou 5 existe o múltiplo de ambos os números, 15, portanto para obter a solução do problema é necessário considerar essa intersecção de múltiplos, sendo portanto a solução desejada. 

$\large3_1, 6_2, 9_3, \dots, 3_n$

$\large5_1, 10_2, 15_3, \dots, 5_n$

$\large15_1, 30_2, 45_3, \dots, 15_n$

Aplicando a condições de intersecção das PAs temos a seguinte expressão:

$$P(3\cap 5) = P(3) + P(5) - P(3\cup 5)$$

Onde a intersecção pode ser interpretada como: 

$$P(3\cup 5) = 15_1, 30_2, 45_3, \dots, 15_n $$

Para obter o número n de cada, PA basta considera o maior número múltiplo de 3,5 e 15 abaixo de 1000, sendo respectivamente, 333,200 e 60. 
Logo a solução do problema é:

$$\sum_{i=1}^{333} 3_i + \sum_{i=1}^{200} 5_i - \sum_{i=1}^{60} 15_i =  233168$$

Segue no arquivo em python da solução. 
