from books import Books
import os

def add_book(library):
    try:
        
        id = len(library.all_books) + 1
        title = input("Digite o Título do livro: ").lower()
        for t in library.all_books:
            while title == t.title or title is '':
                os.system('cls')
                print("Nome invalido, livro já foi cadastrado!" or "Nome Invalido" if title is None else "Nome Invalido")
                title = input("Digite o Título do livro: ")

        author = input("Digite o nome do autor: ").lower()

        new_book = Books(id=id, title=title, author=author, avaliable=True)

        library.all_books.append(new_book)

        print(f"O Livro {title.capitalize()} Foi cadastrado com Sucesso")
    
    except (ValueError, TypeError):
        print("ERROR: Digite um valor válido: ")

def all_books(library):
    print("========TODOS OS LIVROS========\n")
    for book in library.all_books:
        avaliable = "Disponivel" if book.avaliable else "Não Disponivel"
        print(f"""
{'-' * 30}
ID: [{book.id}]
Titulo: {book.title}
Autor: {book.author}
Status: {avaliable}""")
    print('-' * 30)



def search_book(library):
    
    search = input("Digite o Título do Livro ou Autor: ")

    for book in library.all_books:
        avaliable = "Disponivel" if book.avaliable else "Não Disponivel"
        if book.title == search or book.author == search:
            print(f"""
{'-' * 30}
ID: [{book.id}]
Título: {book.title}
Autor: {book.author.capitalize()}
Status: {avaliable}""")
    print('-' * 30)

def see_users(users):

    
    for user in users:
        books = "\n".join(f"Titulo: {book.title}\nAutor: {book.author}\nStatus: Alugado\n{'-' * 30}" for book in user.library_books)
        print(f"""+==========Usuario===========+
|ID: [{user.id}]{''.ljust(19)}|
|Nome: {user.name.ljust(21)} |
+======Livros Alugados=======+

{books if books else "Nenhum livro Encontrado"}""")

def config_library(library):
    print("""========CONFIGURAÇÃO BIBLIOTECA=======

[1] Alterar Nome
[2] Alterar Code
[3] Sair""")

    try:
        option = int(input("Escolha: "))

        if option == 1:
            os.system('cls')
            print("========Alterar Nome========\n")
            name = input("Digite um novo nome para biblioteca: ")

            print(f"Você alterou o nome de {library.name} para {name}")
            library.name = name
            input()
        
        elif option == 2:
            os.system('cls')
            print("========Alterar Code========\n")
            code = input("Digite um novo Code: ")

            while len(code) != 4  or not code.isdigit():
                print("Dígite um código com 4 Dígitos")
                code = int(input("Digite um "))

            library.code = int(code)
        else:
            os.system('cls')
            print("Saindo...")
            input()
            return
    except (ValueError, TypeError):
        print("ERROR: Digite um valor válido: ")
        input()
def main_library(library, users):
    while True:
        os.system('cls')
        print(f"""
{'=' * 30}
{f'Biblioteca {library.name}'.center(30)}
{'MODO: ADM'.center(30)}
{'=' * 30}

[1] Adicionar Livro
[2] Ver Todos os Livros
[3] Pesquisar Livro
[4] Pesquisar Usuario
[5] Configurações da Biblioteca

[0] Sair
""")
        try:
            option = int(input("Escolha: "))

            if option == 1:
                os.system('cls')
                print("========ADICIONAR LIVRO========\n")
                add_book(library)
                input()
            elif option == 2:
                os.system('cls')
                all_books(library)
                input()
            elif option == 3:
                os.system('cls')
                print("========PESQUISAR LIVRO========")
                search_book(library)
                input()
            elif option == 4:
                os.system('cls')
                see_users(users)
                input()
        
        except (ValueError, TypeError):
            print("ERROR: Digite um valor válido")
            input()