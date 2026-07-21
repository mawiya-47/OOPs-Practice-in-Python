class Book:
    def __init__ (self,name,author,publisher,price,language,year,edition,for_sale):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.price = price
        self.language = language
        self.year= year
        self.edition = edition
        self.for_sale = for_sale
    def forsale (self):
        print(self.for_sale)        

# Creater An object
B1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Charles Scribner's Sons", "Novel", 10.99, "English", 1925, "First Edition", True)

B2= Book("To Kill a Mockingbird", "Harper Lee", "J.B. Lippincott & Co.", "Novel", 12.99, "English", 1960, "First Edition", True)
print(B1.name)


