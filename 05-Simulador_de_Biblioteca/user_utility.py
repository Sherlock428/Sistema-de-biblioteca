from datetime import datetime, timedelta
import os 

def all_books(library):
    
    print("========TODOS OS LIVROS========")
    for book in library.all_books:
        avaliable = "Disponivel" if book.avaliable else "Alugado"
        print(f"""
ID: [{book.id}]
Título: {book.title}
Autor: {book.author}
Status: {avaliable}""")
    
        return
    print("=" * 30)
    print("Nenhum Livro Encontrado".center(30))
    print("=" * 30)
    input()

def search_livro(library):
    found = False
    search = input("Digite o Livro que está procurando: ").lower()

    print("\n====>Livros Disponiveis<====\n")
    for i, book in enumerate(library.all_books, start=1):
        if search in book.title or search in book.author:
            avaliable = "Disponivel" if book.avaliable else "Não Disponivel"
            print('-' * 30)
            print(f"ID: [{i}]\nTitulo: {book.title}\nAutor:  {book.author}\nStatus: {avaliable}")
            found = True
        

    if len(library.all_books) <= 0:
        os.system('cls')
        print("-" * 30)
        print("Nenhum Livro Disponivel no momento".center(30))
        print("-" * 30)
        input()
        return False
    
    if not found:
        os.system('cls')
        print('-' * 30)
        print(f"Nenhum livro encontrado com titulo {search}".center(30))
        print('-' * 30)
        input()
        return False
    return True

def borrow_book(library, user):
    
    print("========Alugar Livro========\n")
    if not search_livro(library):
        return
    
    n = int(input("\nEscolha o livro que deseja alugar: "))

    if 1 <= n <= len(library.all_books):
        book_s = library.all_books[n - 1]
        if book_s.avaliable:
            user.library_books.append(book_s)
            book_s.avaliable = False

            date_delivery = datetime.now() + timedelta(days=1) + timedelta(days=user.rating)
            book_s.delivery_time = date_delivery
            formated_date = date_delivery.strftime("%d/%m/%y")
            print(f"Você alugou o livro {book_s.title} até dia {formated_date}")
        else:
            print(f" O Livro {book_s.title} já foi Alugado")
    else:
        print(f"Não encontrado")

def return_book(user):
    print("========Devolva o livro========\n")

    for i, book in enumerate(user.library_books, start=1):
        print(f"[{i}] {book.title}")
        
    n = int(input("\nEscolha o livro que deseja devolver: "))
    
    if 1 <= n <= len(user.library_books):
        book_r = user.library_books[n - 1]
        book_r.avaliable = True
        if datetime.now() > book_r.delivery_time:
            print(f"{user.name} Entregou o livro Atrasado")
            user.rating = max(user.rating, 0)
            user.rating -= 1
        else:
            print(f"{user.name} Entregou o livro no Prazo")
            user.rating = min(user.rating, 5)
            user.rating += 1  
        user.library_books.pop(n - 1)
        
        print(f"{book_r.title} foi devolvido a biblioteca por {user.name}")
        
    else:
        print(f"Livro não encontrado")

def reserved_books(user):
    print("<======>Livros Alugados<======>")
    
    for book in user.library_books:
        formated_date = book.delivery_time.strftime("%d/%m/%y")
        status = "Atrasado" if datetime.now() > book.delivery_time else "Em dia"
        print(f"""{'-' * 30}
ID: [{book.id}]
Título: {book.title}
Autor: {book.author}
Prazo: {formated_date}
Status: {status}""")


    if len(user.library_books) <= 0:
        print("-" * 30)
        print("Nehum Livro Encontrado") 
    print('-' * 30)

def user_config(user, accounts):

    print("""<====>Configuração de Usuario<====>
[1] Trocar Nome de Usuario
[2] Trocar Code
[3] Excluir Conta""")
    
    try: 
        option = int(input("Escolha uma opção: "))

        if option == 1:
            os.system('cls')
            print("========Alterar Nome========\n")
            name = input("Digite um novo nome")
            for account in accounts:
                while name == account.name:
                    print("ERROR: Nome já está em uso")
                    name = input("Digite um novo nome: ")
            
            print(f"Seu nome foi alterado de {user.name} para {name}")
            user.name = name
        
        elif option == 2:
            os.system('cls')
            print('========Alterar Code========\n')
            code = input("Digite o novo codígo: ")

            while len(code) != 3 or not code.isdigit():
                print("ERROR: Digite um código válido")
                code = input("Digite o novo codígo: ")
            
            print(f"Seu código foi alterado")
            user.id = int(code)
        
        elif option == 3:
            os.system('cls')
            print('========Deletar Conta========\n')
            print("Tem certeza que deseja deletar sua conta (s/n): ")
            
            choice = input("S ou N: ").upper()
            while choice not in "SN":
                choice = input("S ou N").upper()

            if choice == "S":
                print("Sua conta foi deletada")
                accounts.remove(user)
                return None
        return user
    except (ValueError, TypeError):
        print("ERROR: Digite um erro valor válido")

def user_main(user, library, accounts):
    
    while True:
        os.system('cls')
        print(f"""
{'=' * 30}
{f'Biblioteca {library.name}'.center(30)}
{'=' * 30}
Usuario: {user.name}
Estrelas: {'☆ ' * user.rating if user.rating != 0 else "0"}
{'-' * 30}
[1] Ver Todos os Livros
[2] Pesquisar Livro
[3] Alugar Livro
[4] Devolver Livro
[5] Livros Alugados
[6] Configuração 

[0] Sair
""")
        try:

            option = int(input("Escolha: "))

            if option == 1:
                os.system('cls')
                all_books(library)
                input()
            elif option == 2:
                os.system('cls')
                print("========Pesquise o livro que está procurando========\n")
                search_livro(library)
                print('-' * 30)
                input()
            elif option == 3:
                os.system('cls')
                borrow_book(library, user)
                input()
            elif option == 4:
                os.system('cls')
                return_book(user)
                input()
            elif option == 5:
                os.system('cls')
                reserved_books(user)
                input()
            elif option == 6:
                os.system('cls')
                user = user_config(user, accounts)
                if not user:
                    print(accounts)
                    return
            else:
                print("Saindo...")
                return

        except Exception as e:
            print(f"Digite um valor válido: {e} ")
            input()
            

