from caesarcripto import *
frase = input('Escreva a frase: ')
senha = input('Coloque uma senha: ')
frase_c = criptografar(frase, senha)
frase_d = descriptografar(frase_c, senha)
print(frase_c)
print(frase_d)
