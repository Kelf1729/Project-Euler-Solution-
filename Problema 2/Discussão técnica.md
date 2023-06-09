[Problema 2](https://projecteuler.net/problem=2)

## Descrição do problema
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

## Discussão técnica 
Analisando o problema, temos que determinar a soma dos números da sequência de Fibonacci onde esses termos devem ser números pares.

Para isso, temos que analisar a sequência pela seguinte fórmula: 

$$
F_n = 
\begin{cases}
0 & \text{se } n = 0 \\
1 & \text{se } n = 1 \\
F_{n-1} + F_{n-2} & \text{se } n > 1
\end{cases}
$$

Analisando para a condição de n>1, temos que a soma dos dois termos anteriores representa o termo seguinte, analisando a sequência abaixo podemos observar:

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

O primeiro e segundo termos são números ímpares, isso faz com que a soma desses dois números sempre sejá um número par, isso pode ser demonstrado onde considerando 
a seguinte construção:

$$2k(par)$$ 

$$2k+1(ímpar)$$ 

Somando dois números ímpares, temos um número de 2, portanto sendo um número par.

$$(2n+1) + (2m+1) = 2n + 2m + 2 = 2(n + m + 1)$$

A sequência de fibonacci apresenta sempre, dois números impares e depois um número par, queremos apenas os números pares, logos os números na sequência abaixo:

3, 6, 9, 12, ... 

Agora é preciso achar o maior número de fibonacci que seja desse sequência, logo múltiplo de 3 de tal forma que o mesmo número seja maior que 4 milhões, para fazer
isso basta usar a "fórmula fechada" da sequência de Fibonacci e igualar isso a 4 milhões e encontrar o valor.

$\frac{1}{\sqrt{5}} \left(\left(\frac{1+\sqrt{5}}{2}\right)^n - \left(\frac{1-\sqrt{5}}{2}\right)^n\right) < 4000000$

O valor de n é igual a 34, sendo o múlitplo mais próximo 33, portanto temos que somar os números de fibonacci de tal forma a sequência de soma seja: 

$3, 6, 9, \dots, 30, 33$

Aqui podemos "normalizar" a sequência de tal forma que ele seja o nova sequência:

$3(1, 2, 3, \dots, 10, 11)$

Essa forma será útil para calcular a soma dos valores de forma manual, seguindo a seguinte manipulação:

$\left(\frac{1}{\sqrt{5}}\left(\frac{1+\sqrt{5}}{2}\right)^n - \frac{1}{\sqrt{5}}\left(\frac{1-\sqrt{5}}{2}\right)^n\right)$

Aplicando a sequência normalizada 

$\frac{1}{\sqrt{5}} \left(\left(\frac{1+\sqrt{5}}{2}\right)^{3n} - \left(\frac{1-\sqrt{5}}{2}\right)^{3n}\right)$

Isolando o n e separando as somas temos a soma de duas PGs, onde bastaria isolar a razão a aplicar a fórmula de soma de uma PG de n termos, 

$\frac{1}{\sqrt{5}} \left(\left(\frac{1+\sqrt{5}}{2}\right)^3\right)^n \left(\left(\frac{1+\sqrt{5}}{1-\sqrt{5}}\right)^n - \left(\frac{1-\sqrt{5}}{1+\sqrt{5}}\right)^n\right)$

$$ \sum_{n=1}^{11}\frac{1}{\sqrt{5}} \left( \left( \frac{1 + \sqrt{5}}{2} \right)^3 \right)^n \left( \left( \frac{1 + \sqrt{5}}{1 - \sqrt{5}} \right)^n - \left( \frac{1 - \sqrt{5}}{1 + \sqrt{5}} \right)^n \right) = 4613732$$

Sendo a solução 
