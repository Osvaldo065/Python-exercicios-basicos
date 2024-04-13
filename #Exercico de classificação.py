#Exercico de classificação

id = int(input('Digite sua idade:'))

if id == 1 or id < 10:
    print('Sua classificação é mirim.')
elif id == 10 or id < 15:
    print('Sua classificação é infantíl.')
elif id == 15 or id < 19:
    print('Sua classificação é junior.')
elif id == 19 or id ==20:
    print('Sua classificação é Senior')
elif id > 20:
    print('Sua classificação é master.')

#Exercico de verificação de triangulo
    
lado1 = float(input('Informe o valor do lado A:'))
lado2 = float(input('Informe o valor do lado B:'))
lado3 = float(input('Informe o valor do lado C:'))

if lado1 == lado2 and lado2 != lado3:
    print('Seu triangulo é Isoceles.')
elif (lado2 == lado3 or lado1 == lado3 )and lado1 != lado2:
    print('Seu triangulo é Isoceles.')
elif lado1 != lado2 and lado1 != lado3:
    print('Seu triangulo é Escaleno.')
elif lado1 == lado2 and lado2 == lado3:
    print('Seu triangulo é Equilatero.')

# Exercicio do cálculo do IMC
    
peso = float(input('Informe seu peso:'))
altura = float(input('Informe sua altura:'))

imc = (peso/(altura**2))
print('Seu IMC é {:.2f}'.format(imc))

if imc< 18.5:
    print('Você está abaixo do peso.')
elif imc == 18.5 or imc < 26:
    print('Você está com o peso ideal.')

elif imc > 25 or imc < 31:
    print('Você está com sobrepeso.')

elif imc > 30 or imc < 41:
    print('Você está com obesidade.')

elif imc > 40:
    print('Você está com obesidade mórbida.')

#Exercicio de condição de pagamento.
    
prod = float(input('Informe o valor do produto: R$'))

forma_pagamento = float(input('Qual a forma de pagamento? \n[1]Dinheiro/PIX. \n[2]Debito a vista. \n[3]Credito parcelado até 2x. \n[4]Crédito parcelado 3x ou mais. \n'))

if forma_pagamento == 1:
    valor = (prod-((prod*10)/100))
    print('O valor da compra ficou: R${}'.format(valor))
elif forma_pagamento == 2:
    valor = (prod-((prod*5)/100))
    print('O valor da compra ficou: R${}'.format(valor))
elif forma_pagamento == 3:
    parcelas1 = prod/1
    parcelas2 = prod/2
    print('O valor da compra ficou: R${} \nParcela de: R${} em 1x. \nParcelas de: R${} em 2x.'.format(prod, parcelas1, parcelas2))
elif forma_pagamento == 4:
    valor = (prod+((prod*20)/100))
    parcelas1 = valor/2
    parcelas2 = valor/3
    print('O valor da compra ficou: R${} \nParcelas de: R${} em 2x. \nParcelas de: R${} em 3x.'.format(valor, parcelas1, parcelas2 ))






