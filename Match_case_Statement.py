x = int(input())
match x:
    case 0:
        print(x, "is zero")
    case 1:
        print(x, "is one")
    case _ if x!= 10:
        print(x, "is not 10")
    case _ if x!= 20:
        print(x, "is not 20")
    case _:
        print("Null")
    