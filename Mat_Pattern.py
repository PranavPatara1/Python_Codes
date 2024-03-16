N,M=map(int,input().split())
a = '-'
b = '.|.'
#Top Part
for i in range(N//2):
    print((b*i).rjust((M-3)//2,a)+b+(b*i).ljust((M-3)//2,a))
    
#middle Part
print('WELCOME'.center(M,'-'))
    
#Bottom _Part
for i in range(N//2):
    print((b*((N//2)-i-1)).rjust((M-3)//2,a) +b+ (b*((N//2)-i-1)).ljust((M-3)//2,a))
