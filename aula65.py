"""
Introdução às funções (def) em Python
Funções são trechos de códigos usados para replicar
determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) e retornar um valor
especifico.
Por padrão, funções Python retornam None (nada).
"""

"""Como funciona:"""
# def nome_da_funcao(parametros):
#     instrução 1
#     instrução 2
#     ...
#     return valor (opicional)

def funcao():
    print('Hello World')
funcao()
funcao()    
funcao() 
funcao()

#Aqui, defini uma função chamada 'funcao' e inseri dentro do corpo da função
# a instrução de print('Hello world'). Para executa-lá, apenas digito
# o nome dela com () ao final. EX: funcao(). Posso também executar essa função
# quantas vezes forem necessárias. No exemplo acima, executei quatro vezes
# logo, será exibido "Hello World" quatro vezes

print()

print('Hello World')
print('Hello World')
print('Hello World')
print('Hello World')
print()

"""Este é apenas um exemplo que mostra porque as funções são tão úteis.
Eu até poderia exibir o print("Hello World") quatro vezes ao longo do meu
código. Porém, se eu quisesse mudar a mensagem depois, teria que alterar
linha por linha. Utilizando uma função, eu só preciso modificar em um lugar."""

"""Define uma função chamada 'saudacao' que recebe dois parâmetros:
mensagem e nome"""
def saudacao(mensagem, nome):
    # O corpo da função: imprime os dois valores recebidos no console
    print(mensagem, nome)

# Chamadas da função passando diferentes argumentos
saudacao('Olá', 'Pietro')   # Saída: Olá Pietro
saudacao('Oi', 'Pietro')    # Saída: Oi Pietro
saudacao('Hello', 'Felipe') # Saída: Hello Felipe
#saudacao()                 # Saída: Type Error no Terminal.
print()

"""Nesse caso, só é possível imprimir as funções caso seja passado um valor
para cada parâmetro, como os parênteses estão vazios, ocorre um erro."""


"""Valores Padrão"""
#Nesse exemplo, irei definir valores padrões para cada parâmetro.
def saudacao(mensagem='Olá', nome='Usuário'):
    print(mensagem, nome)
#Defini como valor padrão para o parâmetro 'mensagem' a str = 'Olá'
# e para o parâmetro 'nome' a str = 'Usuário'

saudacao('Olá', 'Pietro')   # Saída: Olá Pietro
saudacao('Oi', 'Pietro')    # Saída: Oi Pietro
saudacao('Hello', 'Felipe') # Saída: Hello Felipe
saudacao()                  # Saída: Olá Usuário
