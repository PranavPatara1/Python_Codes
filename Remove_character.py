# Removing 7 and 56 from the user provided string.

class A:
    def __init__(self, a):
        self.a = a
    def remove(self):
        b = ''
        for i in range(len(self.a)) :
            if self.a[i] == '7':
                continue
            elif self.a[i] == '5' and i+1 == len(self.a):
                b += self.a[i]
            elif self.a[i] == '5' and self.a[i+1] == '6':
                continue
            elif self.a[i] == '6' and  self.a[i-1] =='5':
                continue
            else:
                b += self.a[i]
        return b

if __name__ == '__main__':
    a = input("Enter String : ")
    Val = A(a)
    print(Val.remove())