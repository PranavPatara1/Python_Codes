list = ['Who is the largest animal : \n1. Lion \n2. Zebra \n3. Girafe \n4. Elephant',
        '\nWho is the largest Water animal : \n1. Shark \n2. Seal \n3. Blue Whale \n4. Sea horse']
list2 = [4,3]
a = 0
name = input("Enter your name :")
print('Hello ',name, 'Welcome to this Game Let\'s Start :')
for i in range(len(list)):
    print(list[i])
    ans = int(input('Enter your option :'))
    if ans == list2[i]:
        print('Congratulations you won, move to the next question')
    else:
        print('Better Luck Next time')
        break