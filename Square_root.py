#Square root program...
def sqrt(a):
    for i in range(0,1000):
        if i*i == a:
            return i
        elif i*i > a:
            s = a - (i-1)*(i-1)
            su = s/(i-1)
            g = i-1
            ans = g + (su/2)
            return ans        
            
if __name__ == '__main__':
    i = float(input())
    print(sqrt(i))


            


