from library import Library
from user import User
from books import Books
from login import register, login_user, login_library
from library_utility import main_library
from  user_utility import user_main

def all_accounts():
    accounts = [User(id=123, name="Mano", library_books=[Books(id=1, title="Aquele Livro 01", author='omilior', avaliable=False),Books(id=1, title="Aquele Livro 02", author='mano', avaliable=False)])]
    account_librarys = [Library(code=1234, name="New biblioteca", all_books=[Books(id=1, title="o melhor livro de todos", author='omilior', avaliable=True),Books(id=1, title="O livro 01", author='mano', avaliable=True)])]

    return accounts, account_librarys

def main():
    accounts, accounts_adm = all_accounts()
    print(f"""
{'=' * 30}
{'Bem-Vindo Ao BBTECA'.center(30)}
{'=' * 30}

[1] Criar uma Conta
[2] Logar Usuario
[3] Logar Biblioteca
[4] Sair
""")
    
    option = int(input("Escolha: "))

    if option == 1:
        register(accounts)
    elif option == 2:
        login = login_user(accounts)

        if login:
            user_main(login, accounts_adm[0])
        
    elif option == 3:
        login = login_library(accounts_adm)

        if login:
            main_library(login, accounts)

main()
