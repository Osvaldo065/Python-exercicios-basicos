"Exercicio de largura x altura"

a = float(input('Digite a altura em metros:'))
l = float(input('Digite a largura em metros:'))
area = (l*a) 
print('Sua parede tem a dimensão de {} x {} e o tamanho da área é: {}m²'.format(a, l, area))
r = (area/2)
print('Para pintar essa parede vai ser necessário {} litros de tinta'.format(r))

"Exercico de porcentagem"

prod = float(input('Informe o valor do produto: R$'))
des = prod-(prod * 5 / 100)
print('O produto com o desconto de 5%, ficou no valor de: R$ {}'.format (des))

"Exercicio de aumento de sálario"

print('Qual o seu sálario?')
salario = float(input('Digite:'))
aumento = salario+(salario*15/100)
print('O valor do seu aumento sálarial ficou em: {}'.format(aumento))

c = float(input('Digite a temperatura:'))
f = (c*1.8+32)
print(' A temperatura em graus celsius convertida em fahrenheit é: {:.2f}'.format(f))

"Exercico do aluguel do carro "

dia = float(input('Quantos dias você alugou o carro?'))
km = float(input('Informe quantos KM você andou:'))
r = dia*60
r1 = km*0.15
print('O valor dos dias alugados é: {} e o valor dos kms percorridos é: {:.2f}'.format(r, r1))
total= r+r1
print('O valor total do aluguel é: {}'.format(total))