"Aula 08"

from math import trunc
num = float(input('Digite um número:'))
int = trunc(num)

print('O valor inteiro é {}'.format(int))

"Exercicio 19"


cat1 = float(input('Digite o  valor do cateto adjascente:'))
cat2 = float (input('Digite o valor do cateto oposto:'))
hip = (cat1**2+cat2**2)**(1/2)
print('O valor da hipotenusa é: {}'.format(hip))

"Exercicio seno, conseno e trangente"

import math

ang = float(input('Digite o valor do angulo:'))
seno = math.sin(math.radians(ang))
print('O ângulo do seno é: {}'.format(seno))
cose = math.cos(math.radians(ang))
print('O ângulo do coseno é: {}'.format(cose))
tang= math.tan(math.radians(ang))
print('O ângulo da tangente é:{}'.format(tang))
