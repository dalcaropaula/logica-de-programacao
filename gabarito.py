#prática - RESPOSTAS - Lógica de Programação e Algoritmos
l = ('\033[34m''-''\033[m') * 35

#°°°°°°°°°°°°°°°°°° Variáveis, Entrada e Saída de Dados      °°°°°°°°°°°°°°°°°° 

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

#01 
preco = float(input('Digite o valor do produto:'))
percentual = float(input('Digite o valor do desconto:'))
desconto = preco* (percentual/100)
final = preco - desconto
print('O desconto é {} % e o valor final do produto ficou: R${}'.format (percentual,final))
print(l)

#02 - 
km = float (input('Quantos km percorridos?'))
dia = int (input('Quantos dias o carro permaneceu alugados?'))
preco = ((60*dia) + (0.15*km))
print('O valor a ser pago é de: R${}'.format(preco))
print(l)

#03 - 
frase = input('Digite uma frase: ')
tam = len(frase)
frase2 = frase[:int(tam/2)]
print(frase2[-2:])






# °°°°°°°°°°°°°°°°°°     Condicionais, Operadores e Expressões Lógicas/Booleana     °°°°°°°°°°°°°°°°°°
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

# 01 - 
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
# 02-  
x= float (input('Digite um numero:'))
if(-100 <= x <= -1 and (1<= x <=100)):
    print(f'O número {x} está em um dos intervalos')
else:
    print('O número não está entre o intervalo')
# -----------------------------------------------------------------------------------------
# 03-
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
# 04-
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
# 05- 
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
# 01- 
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
# 02- 
# a) 
1387//19
# b) 
31%2==0
# c) 
34,29,31 > 30
# -----------------------------------------------------------------------------------------
print('03) - Condicional Simples')
# ------ Condicional Simples 
#   03-
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
#   04-
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
#05
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






#°°°°°°°°°°°°°°°°°°     Estruturas de Repetição      °°°°°°°°°°°°°°°°°° 
#01-  
x=1
while(x<=10):
   resp = x*3
   print(resp)
   x+=1
# -----------------------------------------------------------------
#02-  
n=int (input('Digite um numero: '))
x=1
while(x<=10):
   resp = n*x
   print(f'{x}X{n}={resp}')
   x+=1
# -----------------------------------------------------------------
#03-  
# -----------------------------------------------------------------
#04-  
i=int(input('Digite o valor inicial:'))
f=int(input('Digite o valor final:'))
qpo=1
qpa=0
qim=0
sp=0
si=0
s=i
if(i<f):
    while(s<=f):
        if(s>0):
            qpo=qpo + 1
            sp=sp + s
        if (s %2==0):
            qpa=qpa+1
            sp=sp +1
        else:
            qim=qim +1
            si=si+s
        s=s+ 1
    mpo=sp/qpo
    mpa=sp/qpa
    mim=si/qim
    print(f'Qtd valor positivo: {qpo}')
    print(f'Média valores positivos {mpo}')
    print(f'Qtd valor pares {qpa}')
    print(f'Média valores positivos {mpa}')
    print(f'Qtd valor impar {qim}')
    print(f'Média valores impares {mim}')
else:
    print('Encerrando o programa')
# -----------------------------------------------------------------
#05- 
# -----------------------------------------------------------------
#06-  
# a) 
for i in range (10,1001):
     print (i)
# b) 
for i in range (10,0,-1):
     print(i)
print('fogo!')
# -----------------------------------------------------------------
#07- 
numero=int(input('Digite o numero da tabuada que voce quer:'))
final=int(input('Até que numero voce quer que calule a tabuada? '))
for i in range (0,final+1):
    t= i*numero
    print(t)
print(f'O numero escolhido pra tabuada foi: {numero}, até o valor limite de {final}')
# -----------------------------------------------------------------
#08-  
while True:
    id=int (input('Qual sua idade? \n'))
    if (id <=0):
        break
    s=str (input('Qual seu sexo? M ou F \n'))
    if(s=='F'):
        print(f'Boa noite Senhora. Sua idade é {id}')
    elif(s== 'M'):
        print(f'Boa noite Senhor. Sua idade é {id}')
# -----------------------------------------------------------------
#09-  
for c in range (2,100):
    if(c%3==0):
        print(c)
# -----------------------------------------------------------------
#10-  
# -----------------------------------------------------------------
#11-  
# -----------------------------------------------------------------
#12- Realize a sequencia de print com for e while:
# a) 
i=3
while(i<=12):
 print(i)
 i+=1
# b) 
z=0
while(z<9):
   print(z)
   z+=2
# -----------------------------------------------------------------
#13-
while True:
    print(' + adição\n - subtração\n * multiplicação\n / divisão\n sair')
    op = str (input('Qual operação você deseja? '))
    if (op=='sair'):
        print('Encerrando o programa...')
        break
    n1 = float (input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    if  (op=='+'):
        r=n1+n2
        print(f'O resultado da adição é {r}')
    elif (op=='-'):
        r=n1-n2
        print(f'O resultado da subtração é {r}')
    elif (op=='*'):
        r=n1*n2
        print(f'O resultado da multiplicação é {r}')
    elif (op=='/'):
        r=n1/n2
        print(f'O resultado da divisão é {r}')  
# -----------------------------------------------------------------
#14- 
while True:
    if v >= 100:
        cedulas100 = v//100
        v-=cedulas100 *100
        print(f'Cedulas de cem: {cedulas100}')
        if not v:
            break
    if v >= 50:
        cedulas50 = v//50
        v-=cedulas50 *50
        print(f'Cedulas de cinquenta: {cedulas50}')
        if not v:
            break
    if v >= 20:
        cedulas20 = v//20
        v-=cedulas20 *20
        print(f'Cedulas de vinte: {cedulas20}')
        if not v:
            break
    if v >= 10:
        cedulas10 = v//10
        v-=cedulas10 *10
        print(f'Cedulas de dez: {cedulas10}')
        if not v:
            break
    if v >= 5:
        cedulas5 = v//5
        v-=cedulas5 *5
        print(f'Cedulas de cinco: {cedulas5}')
        if not v:
            break
    if v:
        cedulas1=v
        print(f'Cedulas de um: {cedulas1}')
        break
# -----------------------------------------------------------------
#15- 
p=0
i=0
id=0
while (True):
    id=int(input('Qual sua idade?'))
    if (id <3):
        print('Ingresso gratuito')
        p+= 1
        i+=0
        id+=id
    elif(id >=3 and id <=12):
        print('Ingresso R$15')
        p+=1
        i+=15
        id+=id
    elif(id >12):
        print('Ingresso R$30')
        p+=1
        i+=30
        id+=id
    s=str(input('Desejar sair? S/N: '))
    if (s== 'S'):
        break
m= id/p
print(f'Total de ingressos adiquiridos foi de {i}, a média de idade das pessoas é: {m}, total de pessoas que compraram o ingresso {p}') 
# -----------------------------------------------------------------
#01-
media=0
maioridadehomem=0
nomevelho= ''
totmulher20 = 0
for i in range (1,5):
        nome=input('Qual o seu nome? ')
        idade=int (input('Qual a sua idade? '))
        sexo=input('Sexo? M/F: ')
        #calculo da media das idades
        media+= idade/4 # media recebe ela mesma mais a idade dividido por 4 pq to fazendo tudo junto
        #validar maior idade do homem
        if (i==1 and sexo == 'M'):
            maioridadehomem = idade
            nomevelho = idade
        if (sexo == 'M' and idade > maioridadehomem ):
            maioridadehomem = idade
            nomevelho = nome
        #mulheres com menos de 20 anos
        if (sexo == 'F' and idade<20):
            totmulher20+=1

print(f'A média de todas as 4 idades é: {media}')
print(f'O homem mais velho se chama{nomevelho}, e tem a idade: {maioridadehomem}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos ')

print(l)
# -----------------------------------------------------------------
#02-  
maiorpeso=0
menorpeso=0
for c in range (1,6):
    peso=int (input(f'Digite o {c}peso: '))
    if(c<=1):
        maiorpeso = peso
        menorpeso  = peso
    else:
        if (peso>maiorpeso):
            maiorpeso = peso
        if(peso<menorpeso):
            menorpeso = peso
print(f'O maior peso é: {maiorpeso}')
print(f'O menor é peso é : {menorpeso} ')
print(l)
# -----------------------------------------------------------------
#03- 
somamaior=0
somamenor=0
for c in range(0,3):
    ano=int (input('Digite seu ano de nascimento: '))
    if(ano<=2005): #ano menor que 2005 é de maior
        somamaior+=1
    else:
        somamenor+=1
print(f'O numero de maior de idade é: {somamaior}')
print(f'O numero de menor idade é: {somamenor} ')
print(l)
# -----------------------------------------------------------------
#04- 
soma=0
for c in range (0,6):
    n=int (input('Digite um valor: '))
    if (n%2==0):
        soma += n
print(soma)
#c+=1
print(l)
# -----------------------------------------------------------------
#05-
n= int (input('Qual tabuada voce quer saber?'))
for c in range (1,11):
    t = n*c
    c+=1
    print(t)
print(l)  
# -----------------------------------------------------------------
#06-
soma =0
for c in range (1,501,2):
 if (c % 3 == 0):
  soma += c
print(soma)
print(l)
# -----------------------------------------------------------------







#°°°°°°°°°°°°°°°°°°     Funções      °°°°°°°°°°°°°°°°°° 

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
#05- 
# ----------------------------------------------------------------- 
#01-  
# -----------------------------------------------------------------
#02-  
# -----------------------------------------------------------------
#guanabara
#01-  
def area(l,c):
    a= l*c
    print(f'A área do terreno é de: {a}')

area(4,2)
# -----------------------------------------------------------------
#02-  
def escreva(msg):
    tam= len(msg)
    print('-'* tam)
    print(msg)
    print('-'* tam)

escreva('Olá mundo')
escreva('Paula')
# -----------------------------------------------------------------
#03-
def contador(i,f,p):
    for c in range(1,11):
        print(f'De 1 a 10 com passo 1: {c}')
    for x in range(10,-1,-2):
        print(f'De 10 a 0 com passo 2: {x}')
    for u in range (i,f+1,p):
        print(f'De {i} a {f} com passo {p}: {u}')


contador(20,80,1)  
# -----------------------------------------------------------------
#04-  
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
#05-  
# -----------------------------------------------------------------
#06- 
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
#07- 
# -----------------------------------------------------------------
#08-  
# -----------------------------------------------------------------
#09-  
# -----------------------------------------------------------------
#10- 
# -----------------------------------------------------------------
#11- 



#°°°°°°°°°°°°°°°°°°     Tuplas, Listas, Dicionários e Strings      °°°°°°°°°°°°°°°°°°   




