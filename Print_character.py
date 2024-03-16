num = int(input())
a = 'H'
for i in range(num):
    print((a*i).rjust(num-1)+a+(a*i).ljust(num-1))
    
for i in range(num+1):
    print((a*num).center(num*2)+(a*num).center(num*6))
    
for i in range((num+1)//2):
    print((a*num*5).center(num*6))
    
for i in range(num+1):
    print((a*num).center(num*2)+(a*num).center(num*6))
    
for i in range(num):
    print((a*(num-i-1)).rjust(num*5-1)+a+(a*(num-i-1)).ljust(num-1))
    