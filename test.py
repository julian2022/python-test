class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    def borrow(self):
        self.is_borrowed = True
        print(self.title,"is borrowed")
    def return_book(self):
        self.is_borrowed = False
        print(self.title,"is not borrowed")
obj = book("the famous five","gnid blyton")
obj2 = book("alice in the wonderland", "lewis carol")
obj3 = book("the tree and the breeze", "sudha murty")
obj.borrow()
obj.return_book()
obj2.borrow()
obj2.return_book()
obj3.borrow()
obj3.return_book()
