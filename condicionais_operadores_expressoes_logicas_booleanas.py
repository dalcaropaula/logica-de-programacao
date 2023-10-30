# °°°°°°°°°°°°°°°°°°     Condicionais, Operadores e Expressões Lógicas/Booleana     °°°°°°°°°°°°°°°°°°
#01-    Um aluno, para passar de ano, precisa ser aprovado em todas as materias que esta cursando
#     assuma que a media para aprovação é a partir de 7 e que o aluno curso 3 materias somente.
#     escreva um algoritmo que leia a nota final do aluno em cada materia e informe na tela se ele passou ou nao

# -----------------------------------------------------------------------------------------
#02-    Escreva um algoritmo em python em que o usuario escolhe se quer comprar maças,laranjas ou bananas
#     deverá ser apresentado na tela um menu com as opções: 1- maça, 2-laranja, 3- banana
#     após escolhida a fruta, deve-se digitar quantas unidades se quer comprar.
#     o algoritmo deve calcular o preço total a pagar pelo produto escolhido e mostra-lo na tela.
#     maça - R$2.30
#     laranja - R$ 3.60
#     banana - R$ 1.85

# -----------------------------------------------------------------------------------------
#03-   Caso o nome digitado seja Paula, escreva isso na tela.
#    Caso o usuario digite qualquer outr nome, verifique sua idade. 
#    Se for menor que 18: informe que é de menor.
#    Se for maior que 100 anos, informe que essa pessoa possivelmente nao existe.
# -----------------------------------------------------------------------------------------
#04-  Suponha que: 
#     variaveis numericas: A=1, B=2, C=3, X=20, Y=10 e Z= -1 
#     variáveis booleanas: V1 = True e V2 = False ,
#     variaveis string: Nome = ‘Pedro’, Rua = ‘Pedrinho’
#     Encontre o resultado das expressões lógicas abaixo:
#     a) A + C / B
#     b) C / B / A
#     c) -X ** B
#     d) (-20)**2
#     e) V1 or V2
#     f) V1 and not V2
#     g) V2 and not V1
#     h) not Nome == Rua
#     i) V1 and not V2 or V2 and not True
#     j) X > Y and C <= B
#     k) C – 3 * A < X + 2 * Z
# -----------------------------------------------------------------------------------------
#05-  Escreva um algoritmo que lê um valor inteiro qualquer(x). 
#     Após, verifique se este valor está contido dentro dos seguintes intervalos: 
#     -100 <= x <= -1 e 1 <= x <= 100. 
#     Imprima na tela uma mensagem caso ele esteja em um dos intervalos.
# -----------------------------------------------------------------------------------------
#06-  Faça um algoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário. 
#     Verifique se os valores formam um triângulo e classifique como:
#     a) Equilátero (três lados iguais);
#     b) Isósceles (dois lados iguais);
#     c) Escaleno (três lados diferentes).
#     Lembre-se de que, para formar um triangulo, nenhum dos lados pode ser igual a zero e um lado não pode ser maior do que a soma dos outros dois.
# -----------------------------------------------------------------------------------------
#07-  Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele deseja realizar: 
#     adição (+), subtração (-), multiplicação (*) ou divisão (/). 
#     Exiba na tela o resultado da operação desejada.
# -----------------------------------------------------------------------------------------
#08-  Uma loja de departamentos está oferecendo diferentes formas de pagamento, conforme opções listadas a seguir. 
#     Se a escolha for por pagamento parcelado, calcule também o valor de cada parcela. 
#     Ao final, apresente o valor total da compra e o valor das parcelas:
#     Pagamento à vista – conceder desconto de 5%; 
#     Pagamento em 3x – o valor não sofre alterações;
#     Pagamento em 5x – acréscimo de 2%;
#     Pagamento em 10x – acréscimo 8%.
#     Faça um algoritmo que leia o valor total de uma compra e calcule o valor do pagamento final de acordo com a opção escolhida.
# -----------------------------------------------------------------------------------------
# ------- Expressões booleanas
#09-  Escreva as seguintes expressões booleanas
#     a) o somatorio de 2 com 2 é menos que 4
#     b) o valor 7//3 é igual a 1+1
#     c) a soma de 3 elevado ao quadrado com 4 elevado ao quadrado é igual a 25
#     d) a soma de 2,4 e 6 é maior do que 12
# -----------------------------------------------------------------------------------------
#10-  Escreva as seguintes expressoes boleanas:
#     a) 1387 é divisivel por 19
#     b) 31 é par
#     c) o menor valor entre : 34,29 e 31 é menor que 30
# -----------------------------------------------------------------------------------------
# ------ Condicional Simples 
#11-
#    a) se idade é maior que 60, escreva "voce tem direito aos beneficios"
#    b) se dano é maior do que 10 e escudo é igual a 0, escreva 'voce esta morto'
#    c) se pelo menos uma das variaveis booleanas norte, sul, leste e oeste resultarem em True, escreva"voce escapou"
# -----------------------------------------------------------------------------------------    
# ----- Condicional Composta
#12-
#    a) se ano é divisivel por 4, escreva: "Pode ser um ano bissexto". Caso contrario, "definitivamente não é um ano bissexto"
#    b) se ambas as variaveis booleanas cima e baixo forem true, escreva "decida-se", caso contrario, "voce escolheu um caminho"
# -----------------------------------------------------------------------------------------
#13-  Escreva um programa que calcule o preço a pagar pelo fornecimento de energia eletrica. Pergunte a quantidade de kWh consumida e o tipo de instalação : 
#     R- residencia, I - industria, C- comercios
#     Calcule o preço de acordo com a tabela:
#     residencial: até 500 kwh - 0.40
#                  acima de 500 kwh - 0,65
#     comercial:   até 1000 - 0,55
#                  acima de 1000 -0,60
#     industrial:  até 5000 - 0,55
#                  acima de 5000 - 0,60







# ------------------------- GABARITO 
l = ('\033[34m''-''\033[m') * 40
#01-
l = float (input('Qual sua nota em Lógica?'))
d = float (input('Qual sua nota em Design?'))
p = float (input('Qual sua nota em Programação?'))

if(l>=7 and d>=7 and p>=7):
    print('Parabens, você passou de ano!')
else:
 print('Você não passou de ano')
 #media = ((l+d+p)/3)
#if(media>=7):
   # print(f'Sua nota final é {media}. Parabens, você passou de ano!')
#else:
 #   print(f'Sua nota final é {media}, você não passou de ano')
print(l)
# -----------------------------------------------------------------------------------------
#02-
print(' \t---- Bem-Vindo a Frutaria da Paula ---- \n \tDigite a opção de fruta que deseja comprar: \n \t---- 1- Maça por R$2,30 un ----\n \t---- 2- Laranja por R$3,60 un ----\n \t---- 3- Banana por R$1,85 un ----\n' )
print(l)
op = int (input('Digite a sua opção:'))
print(l)
qtd = int (input(f'Você digitou {op}, agora escolha quantas unidades deseja'))
print(l)
if(op==1):
    valor=qtd*2.30
    print(f'O preço total a pagar é de R${valor}')
elif(op==2):
    valor=qtd*3.60
    print(f'O preço total a pagar é de R${valor}')
elif(op==3):
    valor=qtd*1.85
    print(f'O preço total a pagar é de R${valor}')
else:
    print('Você não digitou corretamente, tente novamente')
print(l)

# -----------------------------------------------------------------------------------------
#03-
n=input('Digite seu nome')
i= int(input('Digite sua idade:'))
if(n == 'Paula'):
    print(n)
    print('Operação encerrada')   
elif (i<18):
    print('De acordo com a sua idade, você é de menor')
elif (i>100):
    print('Você provavelmente não existe')
else:
    print('Operação encerrada')
print(l)

# 04 - 
print('a)',(1+3)/2)
print('b)',3/2/1)
print('c)',-20**2) 
print('d)',(-20)**2)

v1=True
v2=False
print('e)',v1 or v2)

v1=True
v2=False
print('f)',v1 and v2)

v1=True
v2=False
print('g)',v1 and not v2)

Nome = 'Pedro'
Rua = 'Pedrinho'
print('h)', not Nome == Rua) #true

v1=True
v2=False
print('i)',v1 and not v2 or v2 and not True)

x=20
y=10
c=3
b=2
print ('j)', x>y and c<=b)

c=3
a=1
x=20
z= -1
print ('k)', c-3*a < x + 2 * z)

# -----------------------------------------------------------------------------------------
# 05-  
x= float (input('Digite um numero:'))
if(-100 <= x <= -1 and (1<= x <=100)):
    print(f'O número {x} está em um dos intervalos')
else:
    print('O número não está entre o intervalo')
# -----------------------------------------------------------------------------------------
# 06-
print('03)')
a= int (input('Digite o primeiro lado:'))
b= int (input('Digite o segundo lado:'))
c= int (input('Digite o terceiro lado:'))
if(a and b and c > 0):
   if (a+b>c and a+c>b and b+c>a):
      if(a==b==c):
         print('Esse triangulo é equilátero')
      elif(a==b or a==c or b==c):
         print('Esse triangulo é isósceles')
      elif(a!=b or a!=c or b!=c):
         print('Esse triangulo é escaleno')
   else:
      print('Esse não é um triângulo')
else:
    print('Esse não é um triângulo')
# -----------------------------------------------------------------------------------------
# 07-
print('04)')
print('\t ---- Qual operação deseja realizar? \n'
      '\t --- Digite + para Adição --- \n'
      '\t --- Digite - para Subtração --- \n'
      '\t --- Digite * para Multiplicação --- \n'
      '\t --- Digite / para Divisão --- \n \t')
op=input('Digite a operação desejada:')

if(op=='-' or op=='+' or op=='*' or op=='/'):
   n1= int(input('Digite o primeiro numero:'))
   n2= int(input('Digite o segundo numero:'))
   if(op == '+'):
      print('Voce escolheu soma, o restultado é:', n1+n2)
   elif(op == '-'):
      print('Voce escolheu subtração, o resultado é:', n1-n2)
   elif(op =='*'):
      print('Voce escolheu multiplicação, o resultado é:', n1*n2)
   elif(op=='/'):
      print('Voce escolheu divisão, o resultado é:', n1/n2)
   else:
      print('Encerrando o programa')   
else: 
    print('Operação Inválida, encerrado o programa')
# -----------------------------------------------------------------------------------------
# 08- 
print('05)')
valororiginal=int (input('Qual o valor total da compra?'))
print('\t Tipo de pagamento:\n'
        '\t A -> à vista - desconto de 5%\n' 
        '\t B -> em 3x - sem desconto\n' 
        '\t C -> em 5x - acréscimo de 2% \n'
        '\t D -> em 10x - acréscimo de 8%')
tp = input('Qual o tipo de pagamento?')

if(tp=='A' or tp=='B' or tp=='C' or tp=='D'):#condição caso erro de gramatica
   if(tp=='A'): #pagamento a vista
      valordesconto=valororiginal*0.95
      print(f'O pagamento selecionado é à vista. Você terá 5% de desconto. O Valor total da compra é R${valororiginal}'
           f' e o valor final de acordo com a opção escolhida é R${valordesconto}')
   elif (tp=='B'): # pagamento sem desconto, MOSTRAR VALOR DE CADA PARCELA 3
      valordesconto=valororiginal/3
      print(f'O pagamento selecionado é em 3x. Você não terá desconto. O Valor total da compra é R${valororiginal}'
           f' e o valor de cada parcela é 3x de R${valordesconto}')   
   elif(tp=='C'):# pagamento com acrescimo de 2%, MOSTRAR VALOR DE CADA PARCELA 5
    valordesconto=valororiginal*1.02
    valorparcela=valordesconto/5
    print(f'O pagamento selecionado é em 5x. Você terá um acrescimo de 2%. O Valor total da compra é R${valororiginal}'
           f' e o valor final de acordo com a opção escolhida é R${valordesconto} e o valor de cada parcela é 5x de R${valorparcela}') 
   elif(tp=='D'): # pagamento com acrescimo de 8%, MOSTRAR VALOR DE CADA PARCELA 10
    valordesconto=valororiginal*1.08
    valorparcela=valordesconto/10
    print(f'O pagamento selecionado é em 10x. Você terá um acrescimo de 8%. O Valor total da compra é R${valororiginal}'
           f' e o valor final de acordo com a opção escolhida é R${valordesconto} e o valor de cada parcela é 10x de R${valorparcela}')
else:
   print('Digite uma operação válida')
print(l)

# -----------------------------------------------------------------------------------------

# ------- Expressões booleanas
print('Expressões booleanas')
print('01)')
# 09- 
# a) 
2+2>4 #false
# b) 
7//3 == 1+1 #true
# c) 
3**2 + 4**2 == 25 #true
# d) 
2+4+6 > 12 #false
# -----------------------------------------------------------------------------------------
print('02)')
# 10- 
# a) 
1387//19
# b) 
31%2==0
# c) 
34,29,31 > 30
# -----------------------------------------------------------------------------------------
print('03) - Condicional Simples')
# ------ Condicional Simples 
#   11-
# a) 
i= int (input('Qual sua idade?'))
if (i>60):
  print ('Você tem direito aos benefícios')
else:
 print('Sua idade não é maior que 60, você não tem direito aos benefícios')
# b) 
d= int (input('Qual foi a porcentagem de dano?'))
e= int (input('Qual foi a porcentagem de escudo?'))
if (d>10 and e==0):
  print ('Você está morto')
else:
    print('Você esta vivo')
# c) 
n=True
s=True
l=False
o=True
if(n or s or l or o == True):
    print ('Você escapou')
else:
    print('Você não escapou')
# -----------------------------------------------------------------------------------------    
print('04) - Condicional Composta')
# ----- Condicional Composta
#   12-
# a) 
a=int (input('Insira o ano:'))
if (a%4 == 0 ):
  print ('Pode ser um ano bissexto')
else:
    print('Definitivamente não é um ano bissexto')
# b) 
c=True
b=False
if (c and b == True):
  print ('Decida-se')
else:
    print('Você escolheu um caminho ')
# -----------------------------------------------------------------------------------------
print('05)')
#13
print('\t TABELA DOS TIPOS DE INTALAÇÕES \n' 
      '\t R - Residêncial \n' 
      '\t C - Comercial\n '
      '\t I - Industrial \n ')
tipo=input('Digite o tipo de instalação: ')

if(tipo =='R'or tipo =='C'or tipo =='I'): #condição se escrever errado o tipo de instalação
   consumo= int (input('Qual o valor do consumo em kWh?'))
   if (tipo == 'R'):
      if (consumo<= 500):
        valortotal = 0.4
        resultado=consumo*valortotal
        print(f'O valor a pagar é de: R$ {resultado}')
      else:
         valortotal = 0.65
         resultado=consumo*valortotal
         print(f'O valor a pagar é de: R$ {resultado}')
   elif (tipo == 'C'):
      if (consumo <= 1000):
         valortotal =0.55
         resultado=consumo*valortotal
         print(f'O valor a pagar é de: R$ {resultado}')
      else:
         valortotal=0.6
         resultado=consumo*valortotal
         print(f'O valor a pagar é de: R$ {resultado}')
   elif (tipo == 'I'):
      if(consumo<=5000):
         valortotal=0.55
         resultado=consumo*valortotal
         print(f'O valor a pagar é de: R$ {resultado}')
      else:
       valortotal=0.6
       resultado=consumo*valortotal
       print(f'O valor a pagar é de: R$ {resultado}')       
else:       
  print('Tipo de instalação inválida')

print(l)


