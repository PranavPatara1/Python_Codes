class Mul:
    def __init__(self,a):
        self.a = a
    def multiply(self):
        b = str(a)
        s = 1
        for i in b:
            s *= int(i)
        print(s)

if __name__ == '__main__':
    a = int(input("Enter Value : "))
    Val = Mul(a)
    Val.multiply()

