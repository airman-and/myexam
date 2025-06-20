class Book:
    title = ''
    pages = 0

    def __init__(self, title='', pages=0):
        self.title = title
        self.pages = pages

    def __str__(self):
        return self.title
    
    def __gt__(self,other):
        return self.pages > other.pages
    
book1 = Book('Magic of Python',600)
book2 = Book('Master of Python', 500)
print(book1 > book2)
