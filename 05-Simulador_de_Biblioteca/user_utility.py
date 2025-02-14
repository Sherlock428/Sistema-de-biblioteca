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
        user.library_book.append(book_s)
        book_s.avaliable = False

        print(f"Você alugou o livro {book_s.title}")


def return_book(user):
    print("Devolva o livro")

    for i, book in enumerate(user.library_book, start=1):
        print(f"[{i}] {book.title}")
        
    n = int(input("Escolha o livro que deseja devolverr: "))
    
    if 1 <= n <= len(user.library_book):
        book_r = user.library_book[n - 1]
        book_r.avaliable = True
        user.library_book.pop(n - 1)
        
        print(f"{book_r.title} foi devolvido a biblioteca por {user.name}")
        

def user_main(user, library):
    
    while True:
        print(f"""
{'=' * 30}
{f'Biblioteca {library.name}'.center(30)}
{'=' * 30}

[1] Ver Todos os Livros
[2] Pesquisar Livro
[3] Alugar Livro
[4] Devolver Livro
[5] Livros Alugados
[6] Sair
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
            else:
                print("Saindo...")
                return

        except (ValueError, TypeError):
            print("Digite um valor válido: ")
            input()
            

