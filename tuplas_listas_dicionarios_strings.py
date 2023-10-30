 #Tuplas, Listas, Dicionários e Strings
#PRATICANDO - FATIAMENTO
#para mostrar o valor de uma única posição na tupla
p =  ('hamburguer','suco','pizza','pudim')
print(p[2]) #vai mostrar pizza
#mostrar do inicio até o final -1 o ultimo elemento é ignorado
print(p[0:2]) #vai mostrar hamburguer, suco 
#comece na posição 'tal' até o final da tupla
print(p[1:])
#comece do inicio e vá ate tal posição (lembrando q tem q ser um a mais pq ignora o ultimo)
print(p[:2]) #hamburguer e suco
#acessar o ultimo elemento da lista de tras pra frente
print(p[-1])

#PRATICANDO - função len
# para saber quantos elementos existem dentro da tupla
len(p)# resposta 4
#podemos usar dentro de funções
for i in p:
    print(i)



#GUANABARA - TUPLAS
# Tuplas
#01-  Crie um programa que tenha uma tupla totalmente preenchida com um contagem por extenso de 0 até 20
#     seu programa deverá ler um número pelo teclado entre 0 e 20 e mostrá-lo por extenso




# -----------------------------------------------------------------
#02-  Crie uma tupla preenchida com os 20 primeiros colocados da Tabel do Compeonato Brasileiro de Futebol, na ordem de colocação:
#     a) apenas os 5 primeiros colocados
#     b) os ultimos 4 colocados da tabela
#     c) uma lista com os times em ordem alfabetica
#     d) em que posição na tabela está o time da Chapecoense
# -----------------------------------------------------------------
#03-  Crie um programa que vai gerar cinco numeros aleatórios e colocar em uma tupla.
#     depois dsso, mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estão na tupla
# -----------------------------------------------------------------
#04-  Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. 
#     a) quantas vezes apareceu o valor 9
#     b) em que posição foi digitado o primeiro valor 3.
#     c) quais foram os números pares
# -----------------------------------------------------------------
#05-  Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequencia
#     No final, mostre uma listagem de preços, organizando os dados em forma tabular.
# -----------------------------------------------------------------
#06-  Crie um programa que tenha uma tupla com varias palavras. 
#     Depois disso, você deve mostrar, para cada palavra, quais as suas vogais
# -----------------------------------------------------------------