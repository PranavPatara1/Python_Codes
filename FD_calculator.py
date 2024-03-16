def Calc():
    print("Enter Ammount :",end = '')
    a = []
    Z = []
    A = int(input())
    print("How many years you take FD :",end = '')
    Y = int(input())
    S = 0 
    F = 0
    T = 0
    for i in range(Y*12):
        S = T + A
        I = (S/100)*(6/12)
        T += I
    for j in range(Y*12):
        F += A
    Total = F + T
    return Total


if __name__ == "__main__" :
    print("\t\t\t*******Welcome to My Bank*******")
    print("Currently Interest Rate is 6%")
    print("Do you wanna Calculate : \nY\nN")
    b = input()
    if b == "Y":
        print("Total amount after completing FD is : ",Calc())
    else:
        print("If by mistake you exit the window and want to go back : \nY\nN")
        c = input()
        if c == "Y":
            print("Total amount after completing FD is : ",Calc())
        else : 
            print("Thankyou for using this Calculator...\nHave a good day")


