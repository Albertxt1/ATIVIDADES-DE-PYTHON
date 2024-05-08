'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print ('Hello World')
# Exercício 2 - Lanchonete

#Delarando as variáveis
codigo = int(input('Digite o código do produto: '))
quantidade = int(input('Digite a quantidade: '))

if codigo == 100:
    valor_unitario = float (1.20)
    produto = ('Cachorro Quente')
    total = float(valor_unitario*quantidade)
    print('cód:', codigo, 'prod:', produto, 'qdte:', quantidade, 'valor:', valor_unitario, 'total:', total )
elif codigo == 101:
    valor_unitario = float (1.30)
    produto = ('Bauru Simples')
    total = float(valor_unitario*quantidade)
    print('cód:', codigo, 'prod:', produto, 'qdte:', quantidade, 'valor:', valor_unitario, 'total:', total )
elif codigo == 102:
    valor_unitario = float (1.50)
    produto = ('Bauru com Ovo')
    total = float(valor_unitario*quantidade)
    print('cód:', codigo, 'prod:', produto, 'qdte:', quantidade, 'valor:', valor_unitario, 'total:', total )
elif codigo == 103:
    valor_unitario = float (1.20)
    produto = ('Hamburger')
    total = float(valor_unitario*quantidade)
    print('cód:', codigo, 'prod:', produto, 'qdte:', quantidade, 'valor:', valor_unitario, 'total:', total )
elif codigo == 104:
    valor_unitario = float (1.70)    
    produto = ('Cheeseburger')
    total = float(valor_unitario*quantidade)
    print('cód:', codigo, 'prod:', produto, 'qdte:', quantidade, 'valor:', valor_unitario, 'total:', total )
elif codigo == 105:
    valor_unitario = float (2.20)    
    produto = ('Suco')
    total = float(valor_unitario*quantidade)
    print('cód:', codigo, 'prod:', produto, 'qdte:', quantidade, 'valor:', valor_unitario, 'total:', total )
elif codigo == 106:
    valor_unitario = float (1.00)
    produto = ('Refrigerante')
    total = float(valor_unitario*quantidade)
    print('cód:', codigo, 'prod:', produto, 'qdte:', quantidade, 'valor:', valor_unitario, 'total:', total )
else:    
    print('Código Inválido')




