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
        print(self.price)        
