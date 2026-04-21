# simualdor de login
# utilizando o loop for

# definindo variáveis usuario e senha
# atribuindo o valor correto
usuario_correto = "gabrielzinho"
senha_correta = 12345

# máximo de tentativas é 5
for _ in range(5):
    usuario = input("Digite seu usuário: ")
    senha = int(input("Digite sua senha: "))
    if usuario == usuario_correto and senha == senha_correta:
        print("Credenciais válidas")
        break
    else:
        print("Credenciais inválidas, tente novamente")

else:
    print("Número máximo de tentativas excedidas")

print("Foi um sucesso o projeto")
