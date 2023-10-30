#°°°°°°°°°°°°°°°°°°     Funções      °°°°°°°°°°°°°°°°°° 

#01- Crie uma borda ao redor de uma palavra. A rotina deve receber como parametro a palavra destacada. 
#    o tamanho da caixa deve se ajustar de acordo com o tamanho da palavra
# -----------------------------------------------------------------
#02- Escreva uma rotina que recebe três valores como parâmetro e coloque-os em ordem crescente. 
#    Imprima na tela os três valores.
# -----------------------------------------------------------------
#03- Escreva uma função que valida uma string.
#    essa função recebe como parametro a string, o numero mininimo e maximo de caractere
#    retorne verdadeiro se o tamanho estiver entre os valores min e max
#    ou retorne falso caso contrario 
# -----------------------------------------------------------------     
#04-  Faça uma função que recebe dois valores inteiros e positivos como parâmetro. 
#     Calcule a soma dos n valores inteiro existentes entre eles, inclusive estes números
# ----------------------------------------------------------------- 
#05-  Escreve uma função que calcule o fatorial de um número recebido como parâmetro e retorne o seu resultado
#     Faça uma validação dos dados por meio de uma outra função, peritindo que somente positivos sejam aceitos
#     Crie o help da função 
# -----------------------------------------------------------------
#06-  Escreva um algoritmo que permita cadastrar jogos informando o nome e a qual videogame ele pertence
#     crie um menu de opções contendo: cadastrar novo item, listar tudo que foi cadastrado, sair
#     crie uma funçao para cada item do menu
#     armazene todos os dados em arquivos de texto que deve ser salvo em disco 
# -----------------------------------------------------------------
#guanabara
#07-  Faça um programa que tenha uma função area(), que receba as dimensões de um terreno
#     retangular(largura e comprimento) e mostre a area do terreno
# -----------------------------------------------------------------
#08-  Faça um programa que tenha uma função escreva(), que receba um texto de qualquer parametro
#     e mostre uma mensagemm com tamanho adaptavel.
# -----------------------------------------------------------------
#09-  Faça um programa que tenha uma função contador(), que receba três parâmetros:
#     inicio, fim, passo. 
#     e realize três contagens atravez dessa função:
#     a) de 1 ate 10, de 1 em 1
#     b) de 10 até 0, de 2 em 2
#     c) uma contagem personalizada
# -----------------------------------------------------------------
#10-  Faça um programa que tenha uma função maior(), que receba varios parametros com valore inteiros
#     o programa precisa mostrar qual deles é o maior
# -----------------------------------------------------------------
#11-  Faça um programa que tenha uma lista chamada numeros e duas funções: sortea(), somaPar().
#     a primeira função vai sortear 5 numeros e coloca-los dentro da lista
#     a segnda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior
# -----------------------------------------------------------------
#12- Crie um programa que tenha uma função voto() que vai receber como parametro o ano de nascimento
#    retornando um valor literal indicando se uma pessoa tem voto: NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições
# -----------------------------------------------------------------
#13- Crie um programa que trenha uma função fatorial() que receba dois paramentros:
#    o primeiro que indique o numero a calcular 
#    o segundo chamado show, que será um valor logico indicando se será mostrado ou nao na tela o processo
#    de calculo fatorial
# -----------------------------------------------------------------
#14-  Faça um programa que tenha uma função ficha(), que receba dois parâmetros opcionais: 
#     nome do jogador e quantos gols ele marcou
#     O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente
# -----------------------------------------------------------------
#15-  Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input()
#     porem a validação é para aceitar apenas um valor numérico
# -----------------------------------------------------------------
#16-  Faça um programa que tenha uma função notas(), que pode receber varias notas de alunos e vai retornar um
#     dicionario com as seguintes informações:
#     - qtd de notas
#     - maior nota
#     - menor nota
#     - media da turma
#     - a situação (opcional)
#     adicione docstrings à função
# -----------------------------------------------------------------
#17- Faça um mini-sistema que utilize o Interactive Help. O usuário vai digitar o comando e o manual vai aparecer
#    quando o usuário digitar a palavra 'FIM' o programa se encerrará.
# -----------------------------------------------------------------


# ------------------------- GABARITO 
l = ('\033[34m''-''\033[m') * 40
#01- 
def borda(s1):
  tam=len(s1)
  print('+','-'*tam,'+')
  print('|',s1,'|')
  print('+','-'*tam,'+')
   
borda('paula')
borda('oi')
# -----------------------------------------------------------------
#02- 
# -----------------------------------------------------------------
#03- 
def valida(pergunta,min,max):
  p=input(pergunta)#ler a palavra que eu quero
  tam=len(p)# verifico o tamanho dela
  while((tam<min)or (tam>max)): #verifica as condições pro tamanho
    p=input(p)
    tam=len(p)
  return p 
x=valida('Paula',10,30)
print(x)
# -----------------------------------------------------------------     
#04- 
# ----------------------------------------------------------------- 
#05-  
# -----------------------------------------------------------------
#06-  
# -----------------------------------------------------------------
#guanabara
#07-  
def area(l,c):
    a= l*c
    print(f'A área do terreno é de: {a}')

area(4,2)
# -----------------------------------------------------------------
#08-  
def escreva(msg):
    tam= len(msg)
    print('-'* tam)
    print(msg)
    print('-'* tam)

escreva('Olá mundo')
escreva('Paula')
# -----------------------------------------------------------------
#09-
def contador(i,f,p):
    for c in range(1,11):
        print(f'De 1 a 10 com passo 1: {c}')
    for x in range(10,-1,-2):
        print(f'De 10 a 0 com passo 2: {x}')
    for u in range (i,f+1,p):
        print(f'De {i} a {f} com passo {p}: {u}')


contador(20,80,1)  
# -----------------------------------------------------------------
#10-  
def maior(*num):
    contador =maior = 0
    print('Analisando...')
    for valor in num:
        #print(valor)
        if contador ==0:
            maior=valor
        else:
            if valor > maior:
                maior=valor
        contador +=1
    print(f'o maior valor informado foi {maior}')


maior(2,9,4,5,7,1)
# -----------------------------------------------------------------
#11-  
# -----------------------------------------------------------------
#12- 
def voto(ano):
    id= 2023-ano
    if(id>16 and id<18):
        print('Seu voto é OPCIONAL')
    elif (id>70):
        print('Seu voto é OPCIONAL')
    elif(id>18 and id <70):
        print('Seu voto é OBRIGATÓRIO')
    elif (id<16):
        print('Seu voto é NEGADO')

voto(1938)
voto(1998)
voto(2010)
# -----------------------------------------------------------------
#13- 
# -----------------------------------------------------------------
#14-  
# -----------------------------------------------------------------
#15-  
# -----------------------------------------------------------------
#16- 
# -----------------------------------------------------------------
#17- 