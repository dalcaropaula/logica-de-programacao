#°°°°°°°°°°°°°°°°°°  Variáveis, Entrada e Saída de Dados      °°°°°°°°°°°°°°°°°° 
#01-  Escreva as seguintes expressões matemáticas em linguagem Python:
#     a) 2 + 3 x 3
#     b) 4² ÷ 3
#     c) (9² + 2) x 6 - 1
# -----------------------------------------------------------------------------------------
#02-  Douglas Adams nos ensinou que a resposta para o sentido da vida, do universo e tudo mais é 42.
#     Armazene em uma variável o sentido da vida
#     Crie uma mensagem que imprima na tela essa variável junto de uma frase dizendo que ela é o sentido da vida.
# -----------------------------------------------------------------------------------------
#03-  Crie uma variável que receba uma nota de um aluno. 
#     Crie outra variável que receba o resultado de uma comparação lógica entre a nota escolhida e o valor 7, 
#     que é a média para aprovação. 
#     Caso a nota seja maior ou igual a 7, o resultado deve ser verdadeiro. 
#     Imprima o resultado da comparação na tela.
# -----------------------------------------------------------------------------------------
#04-  Imprima na tela uma variável do tipo string que escreva a seguinte frase abaixo. 
#     Crie a string concatenando tudo em uma só linha de código.
#               Linguagens de programação:

#               Python ----- C ----- Java ----- PHP

#     Para dar uma quebra de linha (enter), utilize \n. 
#     Para fazer uma tabulação (tab), utilize \t. 
#     Não esqueça de usar também o multiplicador de strings.
# -----------------------------------------------------------------------------------------
#05-  Crie três variáveis distintas. 
#     Uma contendo o nome da sua comida favorita. 
#     Outra contendo o seu ano de nascimento, 
#     e a terceira contendo o resultado da divisão do seu ano de nascimento pela sua idade.
#     Armazene em uma quarta variável do tipo string uma mensagem que contenha todas as informações das variáveis acima.
#     Resolva o exercício da maneira clássica de composição e também da maneira mais moderna.
# -----------------------------------------------------------------------------------------
#06-  Crie uma variável de string que receba o seu nome completo. 
#     Crie uma segunda variável, agora do tipo booleana. 
#     Esta variável deverá receber o resultado da comparação lógica que verifica seo tamanho do seu nome é menor ou igual ao valor 15. 
#     Imprima a variável booleana na tela.
# -----------------------------------------------------------------------------------------
#07-  Desenvolva um algoritmo que solicite ao usuário uma quantidade de dias, de horas, de minutos e de segundos. 
#     Calcule o total de segundos resultante e imprima na tela para o usuário.
# -----------------------------------------------------------------------------------------
#08-  Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele. 
#     Calcule e exiba o valor do desconto e o preço final do produto.   
# -----------------------------------------------------------------------------------------
#09-  Desenvolva um algoritmo que converta uma temperatura em Celsius (C) para Fahrenheit (F). 
# -----------------------------------------------------------------------------------------
# ---- Expressões Algébricas
#     a) Somatorio dos 5 primeiros numeros inteiros e positivos
#     b) a média entre 23,19,31
#     c) o número de vezes que 73 cabe em 403
#     d) a sobra quando 403 é dividido por 73
#     e) 2 elevado a 10 potencia
#     f) o valor absoluto da diferença entre 54 e 57
#     g) o menor valor entre 34,29 e 31
# -----------------------------------------------------------------------------------------
# ----- Atribuição
#      a) atribuir o valor inteiro 3 a variavel 
#      b) abtribuir o valor 4 à variável b
#      c) atribuir a variavél c ao valor da expressão a*a + b*b
# -----------------------------------------------------------------------------------------
# ---- Strings
#      execute as seguintes atribuições: s1 = 'ant' s2 = 'bat' s3 = 'cod'
#      utilizando os operadores + e *, crie as saidas:
#      a) 1 ant 1 bat 1 cod'
#      b) 10 'ant'
#      c) 1 ant 2 bat 3 cod 
#      d) 7 ant bat
#      e) 5 batbatcod 
# -----------------------------------------------------------------------------------------
#10-  Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele. 
#     Calcule e exiba o valor do desconto e o preço final do produto
# -----------------------------------------------------------------------------------------
#11-  Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. 
#     Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado
# -----------------------------------------------------------------------------------------
#12-  Crie uma variavel de string que receba uma frase qualquer. 
#     Crie uma segunda variável, agora contendo a metade da string digitada. 
#     Imprima na tela somente os dois ultimos caracteres da segunda variavel do tipo string






# ------------------------- GABARITO 
l = ('\033[34m''-''\033[m') * 40
#01- 
#     a) 
print(2 + (3*3))
print(l)
#     b) 
print((4*4)//3)
print(l)
#     c) 
print (((9**2) + 2)*6 - 1)
print(l)

#02-
s='evoluir'
print(s + ' é o sentido da vida')
print(l)

#03-
nota =3
#media = 7 
#resultado = nota >= media
resultado = nota >= 7
print(resultado)
print(l)

#04-
t=('-'*5)
print('\t Linguagens de programação:\n\n \t Python',t,'C',t,'Java',t,'PHP')
print(l)

#05-
comida='japonesa'
ano=1998
div=1998//23
mensagem = (f'Minha comida favorita é a {comida}, meu ano de nascimento é {ano} e a divisão dele pela minha idade é {div}')
print(mensagem)
print(l)

#06-
nome = 'Paula '
tamanho = len(nome) <= 15
print(tamanho)
print(l)

#07-
dia= int(input('Número de dias: '))
hora= int(input('Número de horas: '))
min= int(input('Número de minutos: '))
seg= int(input('Número de segundos: '))
total= dia * 24 * 3600 + hora * 3600 + min * 60 + seg
print('O total em segundo é de: {}'.format(total))
print(l)

#08-
preco = float(input('Digite o valor do produto:'))
desconto = float(input('Digite o valor do desconto:'))
final = preco* (desconto/100)
print('O valor do desconto é: R${} e o valor final do produto ficou: R${}'.format (desconto,final))
print(l)

#09-
print('Conversão de Temperatura - Celsius para Fahrenheit\n')
c = float(input('Digite a temperatura em Celsius:'))
conversao = ((c * 1.8) + 32)
print('O valor {}°C em Fahrenheit é de {} graus'.format(c,conversao))
print(l)

# ---- Expressões Algébricas
# a) 
print(1+2+3+4+5)
print(l)
# b) 
print(23+19+31)/3
print(l)
# c) 
print (403//73)
print(l)
# d)
print (403%73)
print(l)
# e) 
print(2**10)
print(l)
#  f) 
print(abs (54-57))
print(l)
# g) 
n1 = 34
n2 = 29
n3 = 31 
menor = 29
if (n2<menor):
    menor = n2
    if (n3<menor):
        menor = n3
print('O menor valor entre 34,29 e 31 é: {}'.format(menor))
print(l)
print(min(34,29,31))
print(l)

# ----- Atribuição
# a) 
a = 3
#  b) 
b=4
# c) 
c = a*a + b*b
print(c)
print(l)

# ----Strings

s1 = 'ant' 
s2 = 'bat' 
s3 = 'cod'
# a) 
print(s1,' ' ,s2,' ',s3)
# b) 
print(s1*10)
# c) 
print(s1,s2*2,s3*3)
# d) 
print(s1,s2 *7)
# e) 
print((s2+s2+s3)*5)
print(l)

#10 - 
preco = float(input('Digite o valor do produto:'))
percentual = float(input('Digite o valor do desconto:'))
desconto = preco* (percentual/100)
final = preco - desconto
print('O desconto é {} % e o valor final do produto ficou: R${}'.format (percentual,final))
print(l)

#11 - 
km = float (input('Quantos km percorridos?'))
dia = int (input('Quantos dias o carro permaneceu alugados?'))
preco = ((60*dia) + (0.15*km))
print('O valor a ser pago é de: R${}'.format(preco))
print(l)

#12 - 
frase = input('Digite uma frase: ')
tam = len(frase)
frase2 = frase[:int(tam/2)]
print(frase2[-2:])


