class A:
    def __init__(self):
        self.name = "Class A"
    def show(self):
        print("This is Class A")

class B(A):
    def __init__(self):
        super().__init__()
        self.name = "Class B"
    def show(self):
        print("This is Class B")
        super().show()
   
class C(A):
    def __init__(self):
        super().__init__()
        self.name = "Class C"
    def show(self):
        print("This is Class C")
        super().show()

class D(B, C):
    def __init__(self):
        super().__init__()
        self.name = "Class D"
    def show(self):
        print("This is Class D")
        super().show()

class E(C):
    def __init__(self):
        super().__init__()
        self.name = "Class E"
    def show(self):
        print("This is Class E")
        super().show()

class F(D, E):
    def __init__(self):
        super().__init__()
        self.name = "Class F"
    def show(self):
        print("This is Class F")
        super().show()

class G(E):
    def __init__(self):
        super().__init__()
        self.name = "Class G"
    def show(self):
        print("This is Class G")
        super().show()

class X(F, G):
    def __init__(self):
        super().__init__()
        self.name = "Class X"
    def show(self):
        print("This is Class X")
        super().show()

obj = X()
obj.show()  