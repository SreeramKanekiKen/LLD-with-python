class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def show_books(self):
        print(f"Books in {self.name}")
        for book in self.books:
            print(f"- {book.title}")
            
class Book:
    def __init__(self, title):
        self.title = title
        self.libraries = []
        
    def add_library(self, library):
        self.libraries.append(library)
        
    def show_libraries(self):
        print(f"Libraries holding {self.title}")
        for library in self.libraries:
            print(f"- {library.name}")
        
if __name__ == "__main__":
    lib1 = Library("City Library")
    lib2 = Library("University Library")
    
    book1 = Book("1984")
    book2 = Book("To Kill a Mockingbird")
    
    lib1.add_book(book1)
    lib1.add_book(book2)    
    
    lib2.add_book(book1)
    
    lib1.show_books()
    
    print("------------------------------------")
    
    book1.add_library(lib1)
    book1.add_library(lib2)
    book1.show_libraries()
    
    