from user import User
from library import Library

accounts = []
accounts_adm = [Library(code=1234, name="New biblioteca", all_books=[])]
def register(accounts):
        try:
            print("<======>Register<======>\n")

            name = input("Digite seu nome de usuario: ")
            for account in accounts:
                    while account.name == name:
                        print("ERROR: Escolha um nome que não tá em uso")
                        name = input("Digite um nome de usuario: ")
            id = input("Digite um código númerico: ")
            while len(id) < 3 or not id.isdigit():
                print("Código precisa ser de 3 Dígito")
                id = input("Digite um código númerico de 3 digito: ")
            id_2 = int(id)
            new_user = User(id=id_2, name=name, rating=0, library_books=[])
            accounts.append(new_user)

            print(f"Sua conta foi linçença na biblioteca foi feita com sucesso: ")
            input()
        except (ValueError, TypeError):
            print("ERROR Digite um valor válido")
            input("")

def login_user(accounts):

    try:
        print("<========>Login<========>\n")
        name = input("Digite o seu nome de usuario: ")
        id = int(input("Digite seu code de usuario: "))

        for a in accounts:
            if name == a.name and id == a.id:
                print(f"Seja bem-vindo: {a.name}")
                return a
        
        print("Usuario não encontrado")

    except (ValueError, TypeError):
        print("ERROR: Digite um valor válido")
    input("")

def login_library(accounts_adm):
    try:
        print("<======>Login ADM<======>\n")

        name = input("Libraryname: ")
        code = int(input("Code: "))

        for account in accounts_adm:
            if account.name == name and account.code == code:
                print(f"Entrando no sistema da biblioteca: {account.name}")
                return account
    
    except (ValueError, TypeError):
        print("ERROR:Digite um valor válido: ")
        input()
