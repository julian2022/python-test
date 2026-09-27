class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed =  False
    def borrow(self):
        if self.is_borrowed:
           self.is_borrowed = True
           print(self.title,"by",self.author,"is successfully borrowed")
        else:
            print(self.title,"by",self.author,"is already borrowed")
    def return_book(self):
        if self.is_borrowed:
           self.is_borrowed = False
           print(self.title,"by",self.author,"is successfully returned")
        else:
           print(self.title,"by",self.author,"is not returned")
    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)

obj = Book("the famous five","gnid blyton")
obj2 = Book("alice in the wonderland", "lewis carol")
obj3 = Book("the tree and the breeze", "sudha murty")
obj.display()
obj.borrow()
obj2.display()
obj2.borrow()
obj3.display()
obj3.borrow()

