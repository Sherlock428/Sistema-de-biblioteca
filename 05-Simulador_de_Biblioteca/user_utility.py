from books import Books
from library import Library
from user import User

def all_books(library):

    for book in library.all_books:
        avaliable = "Disponivel" if book.avaliable else "Alugado"
        print(f"""
ID: [{book.id}]
Título: {book.title}
Autor: {book.author}
Status: {avaliable}""")
    
        return
    print("Nenhum Livro Encontrado")
        
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
        print("Nenhum Livro Disponivel no momento")
        return False
    
    if not found:
        print(f"Nenhum livro encontrado com titulo {search}")
        print('-' * 30)
        return False
    return True

def borrow_book(library, user):
    if not search_livro(library):
        return
    
    n = int(input("Escolha o livro que deseja alugar: "))

    if 1 <= n <= len(library.all_books):
        book_s = library.all_books[n - 1]
        user.library_books.append(book_s)
        book_s.avaliable = False

        print(f"Você alugou o livro {book_s.title}")
    else:
        print(f"Não encontrado")

def return_book(user):
    print("Devolva o livro")

    for i, book in enumerate(user.library_books, start=1):
        print(f"[{i}] {book.title}")
        
    n = int(input("Escolha o livro que deseja devolverr: "))
    
    if 1 <= n <= len(user.library_books):
        book_r = user.library_books[n - 1]
        book_r.avaliable = True
        user.library_books.pop(n - 1)
        
        print(f"{book_r.title} foi devolvido a biblioteca por {user.name}")
        
    else:
        print(f"Livro não encontrado")

def reserved_books(user):
    print("<======>Livros Alugados<======>")
    for book in user.library_books:
        print(f"""{'-' * 30}
ID: [{book.id}]
Título: {book.title}
Autor: {book.author}""")
    

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
            
            name = input("Digite um novo nome")
            for account in accounts:
                while name == account.name:
                    print("ERROR: Nome já está em uso")
                    name = input("Digite um novo nome: ")
            
            print(f"Seu nome foi alterado de {user.name} para {name}")
            user.name = name
        
        elif option == 2:
            code = input("Digite o novo codígo: ")

            while len(code) < 3 or len(code) > 3:
                print("ERROR: Digite um código válido")
                code = input("Digite o novo codígo: ")
            
            print(f"Seu código foi alterado")
            user.id = code
        
        elif option == 3:
            print("Tem certeza que deseja deletar sua conta (s/n): ")
            
            choice = input("S ou N: ").upper()
            while choice not in "SN":
                choice = input("S ou N").upper()

            if choice != "N":
                print("Sua conta foi deletada")
                accounts.remove(user)
                return None
            
    except (ValueError, TypeError):
        print("ERROR: Digite um erro valor válido")

def user_main(user, library, accounts):
    
    while user:
        print(f"""
{'=' * 30}
{f'Biblioteca {library.name}'.center(30)}
{user.name}
{'=' * 30}

[1] Ver Todos os Livros
[2] Pesquisar Livro
[3] Alugar Livro
[4] Devolver Livro
[5] Livros Alugados
[6] Configuração 
""")
        try:

            option = int(input("Escolha: "))

            if option == 1:
                all_books(library)
                input()
            elif option == 2:
                search_livro(library)
                print('-' * 30)
                input()
            elif option == 3:
                borrow_book(library, user)
                input()
            elif option == 4:
                return_book(user)
                input()
            elif option == 5:
                reserved_books(user)
                input()
            elif option == 6:
                user_config(user, accounts)
                if user is None:
                    return
            else:
                print("Saindo...")
                return

        except (ValueError, TypeError):
            print("Digite um valor válido: ")
            input()
            

