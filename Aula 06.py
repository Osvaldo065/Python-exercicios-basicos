"Aula 07"

from tkinter import N


n1 = int(input('Digite um valor:'))
n2 = int(input('Digite o segundo número:'))
a = n1+n2
s = n1-n2
d = n1/n2
m = n1*n2
di = n1//n2
e = n1**n2
print('O valor da adição é: {} \nA subtração é: {} \nA divisão é: {} \nA multiplicação é: {}'.format(a, s, d, m))
print('O valor da divisão inteira é: {:.3f}'.format(di), '\nO valor da exponenciação é: {:.20f}'.format(e))

"Exercicio 01"

num = int(input('Digite um valor:'))
d = num*2
t = num*3
r = num**1/2
print('O dobro é: {} \nO triplo é: {} \nA raiz é: {}'.format(d, t, r))


"exercicio 02"

n3 =int(input('Digite um valor:'))
r1 = n3+1
r2 = n3-1
print('O sucessor é:',r1)
print ('O antecessor é:',r2)

"exercicio 03"

m = int(input('Digite o valor de metros:'))
cm = m*100
mm = m*1000
print('O valor em CM é: {} \nO valor em MM é: {}'.format(cm,mm))