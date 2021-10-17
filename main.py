from caesarcripto import *
frase = input('Escreva a frase: ')
senha = input('Coloque uma senha: ')
a = input('''Deseja fazer uma criptografia ou descriptografia:
(1) Criptografia
(2) Descriptografia
''')
frase_c = criptografar(frase, senha, a)

print(frase_c)

