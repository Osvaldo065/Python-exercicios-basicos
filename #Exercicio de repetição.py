#Exercicio de repetição, verificando o valor da nota.

n = int(input('Digite uma nota de 0 a 10:'))

while (n > 10):
    print('Valor inválido, \nTente novamente.')
    n = int(input('Digite uma nota de 0 a 10:'))
    

# Exercicio que verifica se o nome é igual a senha, se a senha for igual o nome ele rejeita e pede para digitar novamente.

nome = str(input('Digite seu nome:')).strip()
senha = str(input('Digite sua senha:'))

while(senha==nome):
    print('Senha inválida. \nTente novamente.')
    senha = str(input('Digite sua senha:'))
    


#Exercicio que verifica de 0 a 50 todos os números pares.

for c in range(0, 50):
    if (c%2)==0:
        print(c)

print('Exercicio impares')
#Exercicio de números impares multiplo de 3.
soma = 0
for b in range(0, 500):
    if  (b%2)!=0 and (b%3)==0:
        soma += b
        print('A soma de todos os números são {}'.format(soma))

    
    #Exercicio de tabuada 
print('Exercicio da tabuada')

num = int(input('Informe um valor:'))
print('\nCalculando a tabuda:')
for a in range(0, 11):
    r = num*a
    print('\n{} X {} = {}'.format(num, a, r))


 
#Exercicio soma dos numeros inteiros pares
    
print('Soma dos numeros inteiros pares.')
r = 0
for c in range(0, 6):
 c = int(input('Informe um valor:'))
 if (c%2)==0:
     r += c
print('O valor total da soma dos números pares são:{}'.format(r))




# Exercicio de PA - Progressão aritimetica

print('\nExercicio de PA:')

primeiro = int(input('Informe o primeiro termo:'))
razao = int(input('Informe o valor da razão:'))
soma = 0
for c in range (0, 10):
  termo = (primeiro+razao)
  soma += termo
  print('Valor do termo: {}'. format(soma))
  
  
# Exercicio de número primo (OBS: Com exceção do numero 2 todos os numeros primos são impares)

print('Exercicio número primo:')
 
n1 = int(input('Digite um valor:'))

for c in range (1, n1):
    if (n1!=2) and (n1%2)==0 and (n1%3)!=0:
        print('Esse valor não é um número primo. \nTente novamente...')
        n1 = int(input('Informe um valor:'))
    elif (n1==2) and (n1%2)!=0 and (n1%3)==0:
        print('Esse valor é um número primo')


#Exercicio de maioridade:
import datetime 
r = 0
total = 0
data = datetime.date.today().year

for c in range(0, 7):
    id = int(input('DIgite seu ano de nascimento:'))
    if (id-data)==21:
        r += id
        print('A quantidade de pesssoa menores são: {}'.format(r))
  
    

    