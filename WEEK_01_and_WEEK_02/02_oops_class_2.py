class Product:
    def __init__(self, name, category, price_dollar):
        self.name = name
        self.category = category
        self.price_dollar = price_dollar

    # Dollar to PKR Conversion
    def dollar_to_pkr(self):
        pkr = self.price_dollar * 285
        print("Product Name :", self.name)
        print("Category     :", self.category)
        print("Price ($)    :", self.price_dollar)
        print("Price (PKR)  :", pkr)


# Creating Objects
P1 = Product("Laptop", "Electronics", 600)
P2 = Product("Mobile", "Electronics", 300)

# Calling Method
P1.dollar_to_pkr()
print()
P2.dollar_to_pkr()