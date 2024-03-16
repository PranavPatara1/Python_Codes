#Print Fabonacci Series greater than 50 but less than 1000. (Without Using any Recursion and fuction)

# a = 0
# b = 1
# temp = 0
# List = []
# List2 = []
# List.append(a)
# while(b <= 1000):
#     temp = a + b
#     List.append(b)
#     a= b
#     b = temp
# for item in List:
#     if 50 <= item:
#         List2.append(item)
# print(List2)



# With Recurtion and Fuction :
def fabonacci(n):
   '''Take position of fabonacci number series and return exact value on that series position'''
   if n <= 1:
       return n
   else:
       return(fabonacci(n-1) + fabonacci(n-2))

n = 10 #position of series element

# check if the number of terms is valid
if n <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence: ",end=' ')
   for i in range(n):
       print(fabonacci(i),end=' ')