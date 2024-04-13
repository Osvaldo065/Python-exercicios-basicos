"Exercicio frase"

nome = str(input('Digite seu nome:')).strip()
print('O seu nome maiúsculo é: {}'.format(nome.upper()))
print('O seu nome minusculo é: {}'.format(nome.lower()))
print('A quantidade de letras no seu nome é:{}'.format(len(nome) - nome.count(' ')))
print('A quantidade de letras no seu primeiro nome é:{}'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))

"Exercicio Unidade, Dezena, Centena e Milhar"

num = int(input('Digite um número:'))
un =  num //1 % 10
de = num // 10 % 10
cen = num // 100 % 10
mi = num // 1000 % 10
print('A unidade é: {} \nA dezena é: {} \nA centena é: {} \nO milhar é: {}'.format(un, de, cen, mi))

"Exercicio descobrindo a cidade"

cidade = str(input("Digite uma cidade:")).strip()
print(cidade[:5].upper() == 'SANTO')

nam = str(input('Qual o seu nome completo:')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nam.lower()))


"Exercicio aprofundado na String"

nome = str(input('Digite seu nome:')).upper()
print('A quantidade de letra A é: {}'.format(  nome.count('A')))
print('A letra A aparece nas posições: {}'.format(nome.find('A')+1))
print('A ultima posição da letra A é: {}'.format(nome.rfind('A')+1))

"Exercicio primeiro e ultimo nome"


name = str(input('Digite seu nome completo:')).strip()
name1 = name.split()
print('Seu primeiro nome é: {}'. format(name1[0]))
print('Seu ultimo nome é: {}'.format(name1[len(name1)-1]))
