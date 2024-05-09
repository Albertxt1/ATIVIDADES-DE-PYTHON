
senha=input("Digite sua senha: ")
if login == "userpy" or senha == "senha123":
      print("Seja bem vindo usuário")
else:      
      
     print("Login falhou, verifique seus dados")

	
print ('Nota 1:')
nota1 =input()

print ('Nota2:')
nota2 = input()

soma= int(nota1) + int(nota2)
media = soma / 2

print(media)

if (media >5) :
	print('aprovado' )
else:
	print('reprovado')
