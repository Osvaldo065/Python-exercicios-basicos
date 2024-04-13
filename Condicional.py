#Exercicio de condicional - * nesse exercicio poderia ter usado o Radiant*

import random
print('Seja bem vindo')
print('Você está pronto para começar o jogo?')

print('Então vamos lá...')
print('Pense de 0 a 5')

lista = [0, 1, 2, 3, 4, 5]
escolhido = random.choice(lista)

r = int(input(' Qual número foi escolhido?'))
if r ==escolhido:
    print('Parabéns, você ganhou.')
else:
    print('O número escolhido foi: {}'.format(escolhido))
    print('Você perdeu tente de novo.')

#Exercico de KM

km = float(input('Qual a sua velocidade?'))
if km==80 or km<80:
    print('Você está no limite permitido.')
elif km>80:
    mt= (km-80)*7
    print('Você está acima da velocidade, \nE está sendo multado, \nO valor da multa é: {}'.format(mt))

    #Exercicio de par ou impar"

n1 = int(input('Digite um valor:'))
r = n1%2
if r==0:
    print('Esse número é par.')
else:
    print('Esse valor é impar.')

    #Exercicio de cálculo da viagem"

dist = float(input('Digite a distância da sua viagem:'))
if dist<200 or dist==200:
    r1 = (dist*0.50)
    print('O valor da sua viagem é: {}'.format(r1))
elif dist>200:
    r2= (dist*0.45)  
    print('O valor da sua viagem é: {}'.format(r2)) 

"Exercicio do ano Bissexto"

ano = int(input('Informe um ano:'))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print('O ano é bissexto.')
else:
    print('O ano não é bissexto.')

    
    "Exercicio do maior e menor"

n1 = int(input('Informe o primeiro valor:'))
n2 = int(input('Informe o segundo valor:'))
n3 = int(input('Informe o terceiro valor:'))
if (n1>n2) and (n1>n3):
    print('O maior valor é: {}'.format(n1))
elif (n2>n1) and (n2>n3):
        print('O maior valor é: {}'.format(n2))
elif (n3>n1) and (n3>n2):
        print('O maior valor é: {}'.format(n3))
else: 
    print('Todos os número são iguais.')

    #Exercicio do salário R$

sal = float(input('Qual o seu salário?'))
if sal>1250:
     au = (sal*10)/100
     au1 = au+sal
     print('O seu aumento foi de 10%, o valor do seu salário atual é: {}'.format(au1))
elif (sal==1250) or (sal<1250):
     au = (sal*15)/100
     au1= au+sal
     print('O seu aumeto foi de 15%, o valor do seu salário atual é: {} '.format(au1))



#Exercicio descobrindo o triangulo
     
r1 = float(input('Informe um comprimento:'))
r2 = float(input('Informe o segundo comprimento:'))
r3 = float(input('Informe o terceiro comprimento:'))

tri = (r1+r2)

if tri>r3:
     print('Os segmentos informados, formam um triangulo.')
else:
     print('Os segmentos informados, não formam um triangulo.')
