class Page:
    def __init__(self, pageNo, content):
        self.pageNo = pageNo
        self.content = content
    
    def show(self):
        print(f"Page {self.pageNo} has the content: {self.content}")
        
class Book:
    def __init__(self, title, totalPages):
        self.title = title
        self.pages = []
        self.totalPages = totalPages
        
    def add_page(self, pageNo, content):
        if (pageNo <= self.totalPages):
            page = Page(pageNo, content)
            self.pages.append(page)
        else:
            print("Cannot addd more pages")
            
    def show_book(self):
        print(f"Book Title: {self.title}")
        for page in self.pages:
            page.show()
            
if __name__ == "__main__":
    book = Book("Python OOPs", 3)
    book.add_page(1, "This is page 1")
    book.add_page(2, "This is page 2")      
    book.add_page(3, "This is page 3")
    
    book.show_book();
    
    del book
    