"Modulo 02 "

#Exercicio do empréstimo

nome = str(input('Informe seu nome completo:')).strip()
sal = float(input('Informe seu salário mensal:'))
v1 = float(input('Qual o valor da casa?'))
meses = int(input('Quantas parcelas você deseja?'))

anos = meses/12
prestação = (v1/meses)
limite = (sal*30)/100

if prestação > limite:
    print('{}, você foi negado, o valor da prestação é superior que 30% do seu salário'.format(nome))
elif prestação < limite:
    print('{}, você foi aprovado, parabéns!! \nSuas parcelas ficaram no valor de {:.2f} e vão ser finalizadas em {:.0f} anos.'.format(nome, prestação, anos))

#Exercicio de comparação de numeros inteiros
    
n1 = int(input('Digite um valor:'))
n2 = int(input('Digite o segundo valor:'))

if (n1>n2) or (n2<n1):
    print(' O primeiro valor é maior.')
elif (n2>n1) or (n1<n2):
    print('O segundo número é o maior.')
elif (n1==n2):
    print('Os dois números são iguais')

#Exercicio de alistamento
    
    import datetime
    
nome = str(input('Digite seu nome:')).strip()
ano = int(input('Qual seu ano de nascimento?'))
atual = datetime.date.today().year
idade = (atual-ano)

if (idade==17):
    print('Você deve se alistar até junho.')
elif idade<17:
    falta= 17-idade
    print('Você não precisa se alistar, faltam {} ano'.format(falta))
elif idade>17: 
   falta = 17-idade
   print('Você já deveria ter se alistado, e está {} ano em atraso.'.format(falta))

   #Exercicio de conversão de numero

num1 = int(input('Digite um valor:'))
num = int(input('Digite[1] para converte em binário. \nDigite[2] para converter em hexadecimal. \nDigite[3] para converter em octal. \n'))

if num == 1:
    conversão = bin(num1)[2:]
elif num == 2:
    conversão = hex(num1)[2:]
elif num == 3:
    conversão = oct(num1)[2:]
else:
    print('Número inválido.')

print('O seu número convertido é {}'. format(conversão))


#Exercicio de média

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite sua segunda nota:'))
n3 = float(input('Digite sua terceira nota:'))

md = (n1+n2+n3)//3

if md == 7:
    print('Você foi na média')
elif (md < 7) or (md > 5):
    print('Você está de recuperação.')
elif md < 5: 
    print('Você está reprovado.')
else:
    print('Você está acima da média.')