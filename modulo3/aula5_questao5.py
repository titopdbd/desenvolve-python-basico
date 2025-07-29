usuarios = {
    "admin": ("admin123", "Administrador"),
    "usuario1": ("senha123", "Usuário Comum"),
    "visitante1": ("guest2024", "Visitante")
}

while True:
    login = input("Usuário (ou 'sair' para encerrar): ")
    if login.lower() == "sair":
        print("Encerrando o sistema.")
        break

    senha = input("Senha: ")

    if login in usuarios and senha == usuarios[login][0]:
        print("Login bem-sucedido!")
        print(f"Nível de acesso: {usuarios[login][1]}")
    else:
        print("Erro: Usuário ou senha inválidos.")
