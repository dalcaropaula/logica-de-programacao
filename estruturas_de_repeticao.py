#°°°°°°°°°°°°°°°°°°    Estruturas de Repetição      °°°°°°°°°°°°°°°°°° 
#01-  Escreva na tela os 10 primeiros valores múltiplos de 3.
# -----------------------------------------------------------------
#02-  Crie um programa que calcule a tabuada de um número escolhido pelo
#     usuário. Imprima na tela a tabuada desse número de 1 a 10. Ao realizar a
#     impressão na tela, mostre os valores formatados conforme a seguir.
#     Exemplo com a tabuada do 5: 1x5=5, 2x5=10, 3x5=15...
# -----------------------------------------------------------------
#03-  Escreva um algoritmo que leia dois valores e imprima na tela o resultado
#     da multiplicação de ambos. Entretanto, para calcular a multiplicação, utilize
#     somente operações de soma e subtração. 
#     Lembrando que uma multiplicação pode ser considerada como um
#     somatório sucessivo. Utilize essa lógica para construir seu algoritmo.
# -----------------------------------------------------------------
#04-  Escreva um algoritmo que obtenha do usuário um valor inicial e um valor
#     final. Para este intervalo especificado pelo usuário, calcule e mostre na tela (Puga, p. 70):
#     a) A quantidade de números inteiros e positivos;
#     b) A quantidade de números pares;
#     c) A quantidade de números ímpares;
#     d) A respectiva média de cada um dos itens anteriores.
#     Será necessário criar uma variável distinta para cada somatório, para
#     cada quantidade e para cada média solicitada.
# -----------------------------------------------------------------
#05-  Escreva um algoritmo que leia números inteiros via teclado. Somente
#     valores positivos devem ser aceitos pelo programa (Menezes; Nilo, p. 91).
#     O programa deve receber números até que o usuário digite zero. Ao final
#     da execução, informe a média dos valores digitados. Realize a implementação
#     com as instruções break e continue e trabalhe com operações lógicas Truthy e
#     Falsey. Não esqueça de empregar também operadores especiais de atribuição.
# -----------------------------------------------------------------
#06-   Vamos refazer os exercícios de while, mas agora com for.
#      a) Crie um algoritmo para exibir na tela números de 10 a 1.000
#      b) Crie um algoritmo para exibir na tela uma contagem regressiva do lançamento
#      de um foguete, iniciando em 10 até 0 e escrevendo após o 0, a palavra fogo!
# -----------------------------------------------------------------
#07-  Escreva um algoritmo que calcule e exiba a tabuada de um número
#     escolhido e digitado pelo usuário. A tabuada deve ser calculada até um
#     determinado número n, também fornecido pelo usuário. 
#     Implemente o laço usando for. 
# -----------------------------------------------------------------
#08-  Escreva um algoritmo que repetidamente pergunte ao usuário qual sua
#     idade e seu sexo (M ou F). Para cada resposta o programa deve responder
#     imprimir a mensagem: “Boa noite, Senhor. Sua idade é <IDADE>” no caso
#     gênero de masculino e “Boa noite, Senhora. Sua idade é <IDADE>” no caso de
#     gênero feminino.
#     O programa deve encerrar quando o usuário digitar uma idade negativa.
# -----------------------------------------------------------------
#09-  Escreva um algoritmo que encontre todos os números primos de 2 até 99.Imprima na tela todos eles.
# -----------------------------------------------------------------
#10-  Escreva um algoritmo que imprima na tela as horas no formato H:M:S
#     dentro de um intervalo definido pelo usuário. O usuário deverá delimitar o
#     intervalo de horas que deseja imprimir (por exemplo, das 7h até as 14h).
#     Valide os dados de entrada para que seu programa só aceite valores
#     válidos para hora (de 0 até 23h) e que a hora inicial digitada não seja maior que
#     a final. Caso isso aconteça, o usuário deverá digitar o intervalo novamente.
# -----------------------------------------------------------------
#11-  Escreva um algoritmo que obtenha do usuário uma frase de tamanho
#     entre 10 e 30 caracteres (faça a validação desse dado).
#     Após a frase ter sido digitada corretamente, faça a impressão dela na tela
#     da maneira exata como foi digitada e, em seguida, remova os espaços da frase
#     e imprima novamente, sem espaços.
# -----------------------------------------------------------------
#12- Realize a sequencia de print com for e while:
#    a) inteiros de 3 até 12, com 12 incluso
#    b) inteiros de 0 até 9, excluindo 9, com passo de 2
# -----------------------------------------------------------------
#13-  Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuario qual operação ele deseja:
#     + adição
#     - subtração
#     * multiplicação
#     / divisão
#     sair
#     repita até que a opção saída seja escolhida. 
# -----------------------------------------------------------------
#14-   Escreva um algoritmo que leia um valor e que imprima a quantidade de cédulas necessárias 
#      para pagar esse mesmo valor.
#      Para simplificar, vamos trabalhar apenas com valores inteiros e com cédulas de:
#      R$1OO, 50,20,10,5,1
# -----------------------------------------------------------------
#15-  Um cinema cobra preços diferentes para os ingressos de acordo com a idade de uma pessoa.
#     Se a pessoa tiver menos de 3 anos de idade: ingresso gratuito
#     entre 3 e 12 anos: ingresso R$ 15
#     mais de 12 anos: ingresso R$30 
#     Escreva um laço em que voce pergunte a idade aos usuarios e entao, informe o preço do ingresso
#     Encerre o laço usando um break quando o usuario digitar sair
#     Após encerrar o laço, apresente na tela o total de pessoas que compraram ingressos, o total
#     de dinheiro arrecadado e a media de idade das pessoas 
# -----------------------------------------------------------------
#16- Faça um programa que leia de 4 pessoas: nome, idade e sexo, o programa precisa realizar:
#    a media das idades
#    mostrar qual o nome do homem mais velho
#    mostrar quantas mulheres com menos de 20 anos
# -----------------------------------------------------------------
#17- Faça um programa que leia o peso de 5 pessoas, mostre qual o maior e o menor peso. 
# -----------------------------------------------------------------
#18- Crie um programa que leia o ano do nascimento de 7 pessoas no final mostra quantas são de maior e quantas de menor
# -----------------------------------------------------------------
#19- Faça um programa que leia 6 numeros inteiros e mostre apenas a soma dos que forem par
# -----------------------------------------------------------------
#20- Faça um programa que mostre a tabuada de um numero que o usuario escolher  
# -----------------------------------------------------------------
#21- Faça um programa que calcule a soma entre todos os numeros impares que são multiplos de 3 de 1 a 500
# -----------------------------------------------------------------





# ------------------------- GABARITO 
l = ('\033[34m''-''\033[m') * 40

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
#12- 
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
#16-
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
#17-  
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
#18- 
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
#19- 
soma=0
for c in range (0,6):
    n=int (input('Digite um valor: '))
    if (n%2==0):
        soma += n
print(soma)
#c+=1
print(l)
# -----------------------------------------------------------------
#20-
n= int (input('Qual tabuada voce quer saber?'))
for c in range (1,11):
    t = n*c
    c+=1
    print(t)
print(l)  
# -----------------------------------------------------------------
#21-
soma =0
for c in range (1,501,2):
 if (c % 3 == 0):
  soma += c
print(soma)
print(l)
# -----------------------------------------------------------------


