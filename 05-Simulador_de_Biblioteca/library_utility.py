from books import Books
from library import Library
from user import User

def add_book(library):
    try:
        id = len(library.all_books) + 1
        title = input("Digite o Título do livro: ").lower()
        for t in library.all_books:
            while title == t.title:
                print("Nome invalido, livro já foi cadastrado!")
                title = input("Digite o Título do livro")

        author = input("Digite o nome do autor: ").lower()

        new_book = Books(id=id, title=title, author=author, avaliable=True)

        library.all_books.append(new_book)

        print(f"O Livro {title.capitalize()} Foi cadastrado com Sucesso")
    
    except (ValueError, TypeError):
        print("ERROR: Digite um valor válido: ")

def all_books(library):
    
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

    print("+==========Usuarios==========+")
    for user in users:
        books = "\n".join(f"Titulo: {book.title}\nAutor: {book.author}\nStatus: Alugado\n{'-' * 30}" for book in user.library_books)
        print(f"""|ID: [{user.id}]{''.ljust(19)}|
|Nome: {user.name.ljust(21)} |
+======Livros Alugados=======+

{books}""")


def main_library(library, users):
    while True:
        print(f"""
{'=' * 30}
{f'Biblioteca {library.name}'.center(30)}
{'MODO: ADM'.center(30)}
{'=' * 30}

[1] Adicionar Livro
[2] Ver Todos os Livros
[3] Pesquisar Livro
[4] Pesquisar Usuario

[5] Sair
""")
        try:
            option = int(input("Escolha: "))

            if option == 1:
                add_book(library)
            elif option == 2:
                all_books(library)
            elif option == 3:
                search_book(library)
            elif option == 4:
                see_users(users)
        
        except (ValueError, TypeError):
            print("ERROR: Digite um valor válido")