"Exercicio 18-Lista"
import random
print('Sejam Bem-vindos.')

id1 = str(input('Digite o participante 01:'))
id2 = str(input('Digite o participante 02:'))
id3 = str(input('Digite o participante 03:'))
id4 = str(input('Digite o participante 04:'))

lista = [id1, id2, id3, id4]

escolhido = random.choice(lista)
print('Parabéns o escolhido foi: {}'.format(escolhido))









