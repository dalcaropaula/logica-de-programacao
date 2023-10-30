#teoria - Lógica de Programação e Algoritmos
l = ('\033[34m''-''\033[m') * 40

#°°°°°°°°°°°°°°°°°° Variáveis, Entrada e Saída de Dados      °°°°°°°°°°°°°°°°°° 
# SAÍDA DE DADOS
#------------------- TIPOS DE VARIÁVEL EM PYTHON
# ----- NUMÉRICOS: armazena números
#     int  - inteiro
#     float - decimal
#----------------------------------------------------------------------------
# ---- STRINGS: armazena caracteres, textos, pontuação
#     -pode-se acessar o indice de uma frase
#     -pode-se juntar/somar strings - concatenação
#     -pode-se juntar diferentes variáveis e strings - composição
# --- utilizar composição: para inserir um valor numerico dentro de uma string utilizar {} no local da substituição 
#     e ao final inserir o metodo .format (variavel)
#     -pode-se contar o tamanho de uma string usando a função length
#     -para calcular o valor minimo usar min : (min(89,600))
#     -para calcular valor absoluto: (abs (23-56))
#------------------------------------------------------------------------------
# ----- LÓGICOS: verdadeiro ou falso, sim ou não, 0 ou 1
#          OPERADORES LÓGICOS
#                 and    dois valores verdadeiros
#                  or    pelo menos um valor verdadeiro
#                 not    retorna o oposto do valor
#                nand    um dos valores precisa ser falso
#                 nor    um dos valores precisa ser falso 
#                 xor    os dois valores precisam ser ou verdadeiro ou falso
#                xnor    os dois valores precisam ser iguais
#          OPERADORES DE COMPARAÇÃO - faz comparação entre valores
#                    == igualdade
#                    >  maior que
#                    <  menor que
#                    >=  maior ou igual
#                    <=  menor ou igual
#                    !=  diferente
#          OPERADORES DE ARITMÉTICOS 
#                    + adição
#                    - subtração
#                    * multiplicação
#                    / divisão
#                    // divisão interna
#                    %  módulo
#                    ** exponenciação
#------------------------------------------------------------------------------

# testando a utilização de variavel
nota = 8.5
disciplina = 'Matematica'

print(nota) # retorna 8.5
print ( disciplina) #retorna Matematica
print('A disciplina é:' , disciplina, ' e a nota é:', nota) # retorna A disciplina é: Matematica  e a nota é: 8.5


# PRATICANDO variavel com OPERADORES LÓGICOS

# 3 variaveis: x,y e resposta.
# x vai receber o valor de 1 
# y vai receber o valor de 5 
# resposta será o resultado

x = 1
y = 5

#usando o operador de igualdade ==  
resposta = x == y
print(resposta)  # retorna false
print (l) # espaçamento

#usando o operador de diferença != 
resposta = x != y
print(resposta) # retorna true
print (l) # espaçamento

#usando o operador de maior que
resposta = x > y
print(resposta) # retorna false
print (l) # espaçamento

#usando operador menor que
resposta = x < y 
print(resposta) #retorna true
print (l) # espaçamento

#usando operador maior ou igual que
resposta = x >= y
print(resposta) # retorna false
print (l) # espaçamento

#usando operador menor ou igual que
resposta = x <= y
print(resposta) # retorna true
print (l) # espaçamento
#----------------------------------------------------------------------------

# PRATICANDO como acessar o indice de uma frase (mostrar o caractere que eu quiser)
# 1 variavel que será a frase
frase = 'Será que vou gostar de Python?'
print(frase)
print('O indice 3 representa a letra:', frase[3]) #retorna á
print('O indice 11 representa a letra:', frase[11]) #retorna u
print (l) 

# PRATICANDO concatenação simples
#  1 variavel que receba texto
# operação com essa variavel + outro texto
z = 'Meu nome é '
z = z + 'Paula'
print (z) # retorna Meu nome é Paula
print (l) 

#PRATICANDO concatenação com a multiplicação
# resposta
resultado = 'Bem' + '-' * 5 + 'Vindo'  
print(resultado) # retorna Bem ----- Vindo
print (l) 

#PRATICANDO concatenação com composição 
nota = 6
disciplina = ('matematica')
print ('Voce tirou {} na disciplina de {} '.format(nota, disciplina)) # retorna Voce tirou 6 na disciplina de matematica
print (l) 

# PRATICANDO tamanho da frase
frase = 'Meu cachorro se chama Frederico'
tamanho = len(frase)
print(tamanho) # retorna 31
print(l) 







# °°°°°°°°°°°°°°°°°°    Condicionais, Operadores e Expressões Lógicas/Booleana     °°°°°°°°°°°°°°°°°°
# ---- CONDICIONAL SIMPLES: apenas UM bloco de instruções que é executado se uma condição for VERDADEIRA 
# ---- CONDICIONAL COMPOSTA: + de um bloco de instruções que é executado se uma condição for VERDADEIRA 
# ---- CONDICIONAL ANINHADA: quando existe mais de uma condição, uma dentro da outra
# ---- CONDICIONAL DE MULTIPLA ESCOLHA ELIF: substitui o a repetição de if..else
#------------------------------------------------------------------------------
# ---- UTILIZANDO OS OPERADORES LÓGICOS/BOOLEANOS
#      not - negação, inverte o valor do res. se o valor do resultado é false, ele inverte p/ true  
#      and - conjunção, o resultado só aparecerá true se uma todas as entradas for true
#      or - disjunção, se apenas uma entrada já for true, a saida vai ser true
#------------------------------------------------------------------------------

# PRATICANDO condicional simples:
# Desenvolva um programa que lê dois valores numéricos inteiros e compara se 
# o primeiro é maior do que o segundo, utilizando uma condicional simples.
# Caso seja, ele imprime na tela a mensagem informando que o primeiro valor
# é maior do que o segundo. 

n1 = int (input('Digite o primeiro valor: '))
n2 = int (input('Digite o segundo valor: '))
if (n1 > n2):
    print('O primeiro valor digitado é maior que o segundo')
#else:
#    print('nada')
print(l)

# PRATICANDO condicional composta :
# Desenvolva um programa que lê um valor inteiro e descobre se ele é par ou impar
n3 = int (input('Digite o primeiro valor: '))

if (n3%2==0): # "se o resto da divisão for 0"
    print('O número digitado é par')
else:
    print('O número digitado é impar')
print(l)

# PRATICANDO oper.lógicos/booleanos: not
a = False
b = True
print(not a)
print(not b)
print(l)

# PRATICANDO oper.lógicos/booleanos: and 
a = False
b = False
print(a and b ) # false
print(l)
a = False
b = True
print(a and b ) # false
print(l)
a = True
b = True
print(a and b ) # true
print(l)

# PRATICANDO oper.lógicos/booleanos: or 
x = True
y = False
print(a or b ) # true
print(l)

# PRATICANDO expressão lógicos/booleanos:
# tem que retornar false, x é maior que um? sim, mas tem o not, entao não
x=10
y=1
resp = not x>y 
print(resp)#false
print(l)

# PRATICANDO expressão lógicos/booleanos:
# se 10 for maior que 1 e 5.5 for igual a 1, saida true
x=10
y=1
z=5.5
res = x> y and z==y 
print(res)# falserint(l)

# PRATICANDO expressão lógicos/booleanos:
# se 10 for maior que 1 e 1 for igual a 1, saida true
x=10
y=1
z=1
res = x> y and z==y 
print(res)# true
print(l)





#°°°°°°°°°°°°°°°°°°    Estruturas de Repetição      °°°°°°°°°°°°°°°°°°
#    Enquanto uma condição logica não for satisfeita, 
#    um bloco de instruções (com várias instruções ou apenas uma) será realizado continuamente.
#    Atenção na identação! 
#----------------------------------------------------------------------------
# ---- FOR:   estrutura de repetição com variavel de controle
#             é utilizada quando já se sabe a condição de parada (n° de vezes do laço)
# ---- WHILE: estrutura de repetição com teste lógico
#             não precisa saber onde termina o programa 
#             ele verifica varias condições para completar o loop
#            -para que o laço seja infinito: While (True)
#----------------------------------------------------------------------------
# ---- VARIÁVEIS:            
#        CONTADORA:
#             recebe ele mesmo + 1, ou valor constante
#             normalmente inicia em 0 e é incrementado em 1
#             cont += 1 
#             definir antes do laço
#        ACUMULADORA:
#             recebe ele mesmo + uma variável
#             realiza somatórios
#             um incremento pode ser um acumulador
#             utilizada em for e while
#             definir antes do laço
#----------------------------------------------------------------------------
#    OPERADORES DE ATRIBUIÇÃO
#             x=x+1  -> x+=1
#             x=x-1  -> x-=1
#             x=x*1  -> x*=1
#             x=x/1  -> x/=1
#             x=x**1 -> x**=1
#             x=x//1 -> x//=1
#----------------------------------------------------------------------------
# ---- INSTRUÇÃO BREAK:
#             interrompe um loop e encerra ele
# ---- INSTRUÇÃO CONTINUE:
#            interrompe apenas a iteração, loop atual
#            retorna para o inicio do laço a qualquer momento, 
#            independente da condição da variavel de controle
#----------------------------------------------------------------------------
# -- Incremento: muda o valor da mesma variável
# -- Flag:    significa condição de parada
#----------------------------------------------------------------------------

# -- EXEMPLOS QUE UTILIZAM LAÇO DE REPETIÇÃO
#Caso eu queira perguntar ao usuário o valor final da minha contagem,posso colocar essa variavel da pergunta dentro do laço de repetição 
#01- Quero que o usuário defina valor inicial e final para o prog. contar
ni=int (input('Qual o valor inicial da contagem: '))
nf= int (input('Qual o valor final da contagem: '))

for c in range (ni,nf+1):
     print(c)
print(l)

#Caso eu queira fazer um numero exato de perguntas ao usuario: ex- 3 perguntas
for c in range (0,3):
     pergunta = int(input('Digite um valor: '))
print('fim')
print(l)

#Caso eu queria fazer um numero exato de pergunta E UM SOMATÓRIO desses resultados
somatorio = 0 # inicia no valor 0 
for c in range (0,3):
     pergunta = int(input('Digite um valor: '))
     somatorio = somatorio + pergunta # a minha soma é igual a ela mesma mais o valor digitado
print(f'O somatorio foi: {somatorio}')
print(l)
# ou
soma=0
for c in range(0,3):
     n=int(input('Digite o valor: '))
     soma += n
print(f'O somatorio foi: {soma}')
print(l) 

#Caso eu queira validar um dado: (se o usuário digitar errado, por exemplo)
#01- Faça um programa que aceite apenas os valor M ou F, se estiver errado, peça para digitar novamente.
s=str (input('Digite seu sexo M ou F:'))
while(s !='M'and s!='F'):#enquanto sexo  for diferente de  M e F
  s=input('Invalido, digite o sexo novamento M ou F:')# leia de novo
print('Sexo registrado com sucesso')# registrou na variavel externa
print(l)
#02- Crie um algoritmo que receba um valor do tipo inteiro via teclado, o programa só deve aceitar, obrigatoriamente, valores inteiros e positivos
# qualquer valor negativo, ou igual a zero, deve ser rejeitado pelo programa e um novo valor solicitado.
x= int (input('Digite um valor maior que zero'))
while (x <= 0):
     x= int (input('Digite um valor maior que zero'))
print('Voce digitou certo')
print(l)

# PRATICANDO variável contadora e incremento
#01- Contar 5 numeros com inicio em 1
x=1
while(x<=5): #enquanto for menor igual, isso define o limite pois queremos só até o 5
    print(x) 
    x = x +1 # isso é o incremento de contagem de 1 em 1. caso não tenha, x sempre vai valer 1 
             # e vai ficar imprimindo pra sempre, precisa de um fim
print(l)
#02- Contar 10 numeros com inicio em 1, mas de dois em dois
x=1
while(x<=10):
    print(x)
    x = x + 2
print(l)

# PRATICANDO operador especial de atribuição +=
soma =0 #pergunta das notas
acumulador = 1 #faz a contagem
while (acumulador <= 5):
        nota = float (input(f'Qual o valor da sua {acumulador}ª nota? ')) #variavel da pergunta
        soma += nota # já faz a soma das 5 notas
        acumulador += 1 # incremento
media = soma / acumulador #calculo da média que é a var de soma / 5 ou acumulador 
print(f'A média final é {media}')
print(l)

# PRATICANDO instrução BREAK
# escreva um algoritmo que fique recebendo frases ou palavras digitadas pelo usuario, encerre quando a palavra
# sair for digitada 
print('Digite algo e quando quiser sair, digite sair')

while True:
    x=input('digite: ')
 #   print(x)
    if(x=='sair'):
        print('Encerrando programa')
        break
print(l)

# -- PRATICANDO instrução CONTINUE
# escreva um algoritmo que realize um login em um sistema, usuario tem que informar nome e senha
# nome e senha precisam ser diferentes de alguma condição
while True:
    nome =input('Digite seu usuario: ')
    if (nome != 'oi'): #se o nome diferente de oi ele vai repetir a instrução ate digitar oi 
        continue #continue a sequencia
    # proximo bloco de instrução
    senha =int (input('Digite sua senha: ')) 
    if(senha !=0): # se a senha diferente de 0
        break # encerra o laço
    print('Acesso liberado') #liberar
print(l)

#-- PRATICANDO variável acumuladora 
# calcule a media dos pares de 1 ate 100
soma = 0 
qtd = 0
for x in range (1,101):
    if (x%2==0):
        soma += x
        qtd += 1
media = soma / qtd
print(f'A media dos pares de 1 ate 100 é {media}')
print(l)

# PRATICANDO variavel iteradora
# Escreva um algoritmo que imprima na tela somente valores dentro de um intervalo especificado pelo usuario e que sejam numeros pares 
i=int (input('Qual o valor inicial:')) #inicio
f=int (input('Qual o valor final:')) #final
x = i #variavel iteradora: joga o valor de inicio em uma outra variavel pra conseguir usar no while

while (x <=f): #condição
    if (x%2 ==0): #verificação
        print(x)
    x = x + 1 #incremento
print(l)

# -- PRATICANDO acumulador 
# Escreva um algoritmo que calcule a sua média de notas em determinada disciplina.
# Vamos assumir que a média final é dada pela média aritmética de cinco notas digitadas

soma =0 #pergunta das notas
acumulador = 1 #faz a contagem
while (acumulador <= 5):
        nota = float (input(f'Qual o valor da sua {acumulador}ª nota? ')) #variavel da pergunta
        soma = soma + nota # já faz a soma das 5 notas
        acumulador = acumulador + 1 # incremento
media = soma / acumulador #calculo da média que é a var de soma / 5 ou acumulador 
print(f'A média final é {media}')
print(l)




#°°°°°°°°°°°°°°°°°°    Funções       °°°°°°°°°°°°°°°°°°
# ---- FUNÇÕES: são rotinas, uma função que você faz constantemente 
#               def nomedafuncao(parametro)
#               blocos de códigos que são chamados pelo nome e assim, executados
#               se utiliza parâmentros ()
#               exemplo: print, input, float, range,len
# -----------------------------------------------------------------
# ---- INTERACTIVE HELP: é uma ajuda interativa que pode ser chamada por: help(), 
#                        depois de entrar escolha o que precisa saber
#                        help (print) por exemplo
# -----------------------------------------------------------------
# ---- DOCSTRINGS: string de documentação
#                  para criar uma, colocar logo em baixo da criação da função com aspas duplas 3x , exemplo:
#                      def contador(i,f,p):
#                          """
#                          descrição
#                          """
#                 chamar o comando help. help(contador)
# -----------------------------------------------------------------
# ---- ESCOPO DE VARIÁVEL: é o local onde a minha variavel vai ou não existir
#                  GLOBAL: quando a variavel é declarada fora da função
#                  LOCAL: quando a variavel é declarada apenas dentro da função 
#                  para usar global dentro da função: global nomevariavel  
# -----------------------------------------------------------------
# ---- RETORNO: return
#               precisa criar uma variavel para receber esse retorno  
# -----------------------------------------------------------------
# ---- LAMBDA: função mais simples
#              escrita em uma unica linha de codigo 
# -----------------------------------------------------------------
# ---- TRATAMENTO DE EXCEÇÕES:
#                   erro de sintaxe: quando digita errado ou esquece de algum detalhe
#                   erro de exceções: sintaxe correta porém acontece algum erro inesperado na execução
# -----------------------------------------------------------------
# ---- EMPACOTAMENTO: quando não se sabe o numero dos parâmetros, utilizar a função num
#                     def nomedafuncao(*num)
# -----------------------------------------------------------------

# PRATICANDO criar e chamar um docstring
def contagem(i,f,p):
      """
      faz uma contagem
      """

help(contagem)

# PRATICANDO empacotamento (quando nao se sabe a quantidade de parametros)
def contador(*num):#recebe uma quantidade de parametros nao definidos
   print(num)

contador(2,3,4) 
contador(4,5,6,7,8,9) # mesma função mas com outra quantidade de paramentro

# PRATICANDO usar variavel global dentro da função
def teste(b):
      global a
      a=8
      b+=4
      c+2
      print(f'A dentro vale{a}')
      print(f'B dentro vale{b}')
      print(f'C dentro vale{c}')

a=5
teste(a)
print(f'A fora vale{a}')


# PRATICANDO utilizar o retorno
#01-
def somar(a=0,b=0,c=0):
    s=a+b+c
    #print(f'A soma vale {s}')
    return s


resposta= somar(3,2,4)
print(resposta)
#02-
# retorno
def soma (x=0,y=0,z=0):
    res=x+y+z
    return res
#para mostrar a resposta podemos:
#1- criar uma variavel só pra resposta
resposta = soma(1,2,3)
#2- fazer tudo em um print
print(soma(1,2,3))

# PRATICANDO função com tratamento de exceção 
def div ():
    try:
        num1=int(input('Por favor, digite um número:'))
        num2=int(input('Por favor, digite um número:'))
        res = num1/num2
    except ZeroDivisionError:
        print('Erro de divisão por 0')
    except:
        print('Algo de errado aconteceu..')
    else:
        return res
    finally:
        print('Executará sempre')

# PRATICANDO função lambda
res= lambda x: x*x
print(res(3))


#°°°°°°°°°°°°°°°°°°     AULA 06 - Tuplas, Listas, Dicionários e Strings      °°°°°°°°°°°°°°°°°°  
# --- Tuplas(): é uma variável composta que é IMUTAVEL 
# --- Lista []:
# --- Dicionário {}: 


#PRATICANDO - FATIAMENTO
#para mostrar o valor de uma única posição na tupla
lanche = [ham,suco,pizza,pudim]
print(lanche[2]) #vai mostrar a pizza
#mostrar do inicio até o final -1 o ultimo elemento é ignorado
print(lanche[0:2]) #vai mostrar ham e suco