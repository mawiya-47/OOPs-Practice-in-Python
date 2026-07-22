class Book :
    def __init__ (self ,name,author,publisher,genre,price,language,year,Edition,forsale) :
        self.name = name
        self.author = author
        self.publisher = publisher
        self.genre = genre
        self.price = price
        self.language = language
        self.year = year
        self.Edition = Edition
        self .forsale = forsale
    def forsale(self):
        print (self.for_sale)

# Creater An object
B1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Charles Scribner's Sons", "Novel", 10.99, "English", 1925, "First Edition", True)

B2= Book("To Kill a Mockingbird", "Harper Lee", "J.B. Lippincott & Co.", "Novel", 12.99, "English", 1960, "First Edition", True)
print(B1.name)