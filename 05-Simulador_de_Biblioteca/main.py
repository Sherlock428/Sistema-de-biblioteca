from library import Library
from user import User
from books import Books
from login import register, login_user, login_library
from library_utility import main_library
from  user_utility import user_main
import os

def all_accounts():
    accounts = [User(id=123, name="Mano", rating=1, library_books=[])]
    account_librarys = [Library(code=1234, name="New biblioteca", all_books=[Books(id=1, title="O melhor de todos", author="Omilior", avaliable=True, delivery_time=None), Books(id=2, title="O Livro 01", author="Manito", avaliable=True, delivery_time=None), Books(id=3, title="Aquele lá", author="Ali", avaliable=True, delivery_time=None), Books(id=4, title="O Livro 02: O Retorno do 01", author="Manito", avaliable=True, delivery_time=None)])]

    return accounts, account_librarys

def main():
    accounts, accounts_adm = all_accounts()
    while True:
        os.system('cls')
        try:
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
                os.system('cls')
                register(accounts)
            elif option == 2:
                os.system('cls')
                login = login_user(accounts)

                if login:
                    user_main(login, accounts_adm[0], accounts)
                
            elif option == 3:
                os.system('cls')
                login = login_library(accounts_adm)

                if login:
                    main_library(login, accounts)
        
        except (ValueError, TypeError):
            print("ERROR: Digite um valor válido")
            input()

main()
