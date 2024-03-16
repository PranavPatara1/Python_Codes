## 1. This code count the occurance of numbers in the given string fro  0-9 :

# a = input("Enter String :")
# b  ''
# count=0
# for i in range(0,10):
#     for j in a:
#         if str(i)==j:
#             count += 1
#     b += str(count) 
#     count = 0
# print(b)=


## 2. This code give the unique numbers from the given range:
# a = list(map(int,input("Enter range :").strip().split(" ")))
# list1 = []
# for i in range(a[0],(a[1]+1)):
#     b = str(i)
#     c = b[0]
#     d = b[1]
#     if c==d:
#         continue
#     list1.append(i)

# print(list1)


## 3. Clockwise rotate Values in list as per user input :

# a = int(input("Enter list length : "))
# list = []
# for i in range(a):
#     b = int(input())
#     list.append(b)
# c = int(input("Enter element of k :"))
# list1 =[]
# list2 =[]
# for i in range (len(list)):
#     if i > (len(list)-c-1) :
#         list1.append(list[i])
#     else:
#         list2.append(list[i])
# list = list1 + list2
# print(list)

## 4. From List putting all multiple of 10 at end and position of non multiple and multiple mentained as same.

# a = int(input("Enter list length : "))
# list = []
# for i in range(a):
#     b = int(input())
#     list.append(b)
# list1 =[]
# list2=[]
# for i in list:
#     if i%10==0:
#         list1.append(i)
#     else:
#         list2.append(i)
# list = list2 + list1
# print(list)



## 5. Direction finding that our position is same as starting or not.

# a = input("Enter Directions : ")
# N = 0
# W = 0
# E = 0
# S = 0
# for i in a:
#     if i == 'N': N += 1
#     elif i == 'W': W += 1
#     elif i == 'E': E += 1
#     else: S +=1
# if (N==S and E==W):
#     print("Returened Successfully")
# else:
#     print("Not Returened Successfully")


## 6. Give a positive integer number and then sum up the number, if total is 1 then UNO else Not UNO
## Ex -> 51112 = 5 + 1 + 1 + 1 + 2 = 10 = 1 + 0 = 1

# def addition(b):
#     lst = []
#     sum = 0
#     for i in b:
#         lst.append(int(i))
#     for i in lst:
#         sum += i
#     if sum <= 9:
#         return sum
#     else:
#         return addition(str(sum))

# a = int(input("Enter number : "))
# b = str(a)
# c = addition(b)
# if c==1 :
#     print("UNO")
# else:
#     print("Not UNO")


# import matplotlib.pyplot as plt

# price = [2.50, 1.23, 4.02, 3.25, 5.00, 4.40]
# sales_per_day = [34, 62, 49, 22, 13, 19]

# plt.scatter(price, sales_per_day)
# plt.show()

# a = 10
# def fx(a = a, b = a+a):
#     return a + b
# print(fx())


# Reverse name 

# class name:
#     def __init__(self,a):
#         self.a = a
#     def reverse(self):
#         rev_name = ''
#         for i in range(len(self.a)):
#             if self.a[i] == ' ':
#                 rev_name = self.a[i+1:] + self.a[i] + self.a[:i]
#                 return rev_name
#             elif self.a[i] != ' ' and type(self.a[i]) != 'str':
#                 return self.a

# if __name__ == '__main__':
#     a = input("Enter your name : ")
#     Val = name(a)
#     print(Val.reverse())


# This code is for count the words in the multiple strings and arrange the strings as per count in assending order
 
# occ = int(input('Enter number of strings : '))
# a1 = input("Enter Word : ")
# l = []
# l1 = []
# c = 0
# for i in range(occ):
#     b = input("Enter String :")
#     l.append(b)

# for item in l:
#     c = item.count(a1)
#     l1.append(c)

# for i in range(occ*6):
#     for j in range(len(l1)):
#         if  i == l1[j]:
#             print(l[j])


# Below code gives the sum of digonal array values :

# lis = [[1,2,3,4,5,6],[6,7,8,9,2,3],[2,5,7,9,1,2],[10,12,14,16,18,20],[20,22,24,25,27,29],[10,11,12,13,14,15]]
# c = 0
# sol = 0
# for i in range(len(lis)):
#     for j in range(len(lis[i])):
#         if i == j:
#             c = lis[i][j]
#             sol = sol + c
# print(sol)


# Below code take a string and remove vovels if single occured, But if vovel next frequent character is also vovel then it ignores :

# a = input("Enter String : ")
# st = ''
# for i in range(len(a)):
#     if (a[i] != 'a' and a[i] !='e' and a[i] !='i' and a[i] !='o' and a[i] !='u') and i != len(a)-1:
#         st = st + a[i]
#     elif (a[i-1] == 'a' or a[i-1] == 'e' or a[i-1] == 'i' or a[i-1] == 'o' or a[i-1] == 'u') and (a[i] == 'a' or a[i] =='e' or a[i] =='i' or a[i] =='o' or a[i] =='u'):
#         st = st + a[i-1] + a[i]
# print(st)


# Below code takes numbers and give only prime numbers list :

# a = int(input("Enter Total Numbers : "))
# lis = [] 
# lisp = []
# for i in range (a):
#     b = int(input("Enter value : "))
#     lis.append(b)
# for i in lis:
#     if i == 2 or i == 3 or i == 5 or i == 7:
#         lisp.append(i)
#     elif i%2 != 0 and i%5 != 0 and i%3 != 0 and i%7 != 0 and i!=1:
#         lisp.append(i)
# print(lisp)



# Below code showing difference between strptime() and strftime() 

# from datetime import datetime
  
# a = datetime.now()                # Type is "datetime"
# b = datetime.strftime(a,'%Y')     # It changes datetime type to "String" and we get only thse data what we want by giving formats. 
# c = datetime.strptime(b,'%Y')     # This change Type back to "datetime" && format must be equal to format present in "b".
# print(a)
# print(b)
# print(c)


# Below code finds he input is pallindrom or not :

# import time
# initial = time.time()
# a = int(input())
# b = str(a)
# c = ''
# for i in range(len(b)):
#     c = c + b[len(b)-i-1]
# if b == c:
#     print("Its a pallindrom")
# else:
#     print("Its not a pallindrom")
# print("Total time taken by code : ",(time.time() - initial), " Seconds")


# Below cade take input and break into 3 strings and check all strings are making pallindrom or not :

# import sys

# def is_pallindrom(s):
#     if len(s)==1:
#         return True
#     s1=s[::-1]
#     return s1==s

# a = input()
# l = len(a)
# for i in range(1,l-1) :
#     s1 = a[:i]
#     if is_pallindrom(s1):
#         for j in range(1,l-1):
#             s2 = a[i:i+j]
#             s3 = a[i+j:]
#             if is_pallindrom(s2) and is_pallindrom(s3):
#                 print(s1)
#                 print(s2)
#                 print(s3)
#                 sys.exit()
# print("impossible")



# Below code take values larger and smaller, then interchange larger values and compare with smaller value, if greater then give value :

# a = int(input())
# b = int(input())
# c = str(a)
# d = len(c)
# if d == 3:
#     e = c[1] + c[::2]
#     if int(e) > b :
#         print(e)
#     else:
#         print(-1)
# elif d == 6:
#     e = c[1] + c[:3:2] + c[4] + c[3::2]
#     if int(e) > b:
#         print(e)
#     else:
#         print(-1)



# Below Code Gives HCF of two numbers :

# a = int(input())
# b = int(input())
# HCF = 0
# if a>b:
#     small = b
# else:
#     small = a
# for i in range(1,small):
#     if (a%i == 0) and (b%i == 0):
#         HCF = i

# if HCF > 1:
#     print("HCF is : ",HCF)
# elif a == 1 and b == 1:
#     HCF = 1
#     print("HCF is : ",HCF)
# else:
#     print("HCF is Not Possible.")




# Below Code Gives LCM of two numbers :

# a = int(input())
# b = int(input())
# if a>b:
#     larger = a
# else:
#     larger = b
# while True:
#     if (larger%a == 0) and (larger%b == 0):
#         LCM = larger
#         break
#     larger +=1
# print("HCF is : ",LCM)



# a = int(input("Enter list length : "))
# lst = []
# lst1 = []
# lst2 = []
# for i in range(a):
#     b = int(input("Enter value : "))
#     lst.append(b)
# for i in range(len(lst)):
#     if i%2==0:
#         lst1.append(lst[i])
#     else:
#         lst2.append(lst[i])
# lst1.sort(reverse=True)
# lst2.sort(reverse=True)
# c = lst1[1] + lst2[1]
# print(c)


# A = 1
# B = 10
# C = 100
# D = 1000
# E = 10000
# F = 100000
# G = 1000000



# Sum = 0
# b = input()
# for i in b:
#     if i == 'A':
#         Sum = Sum + 1
#     elif i == 'B':
#         Sum = Sum + 10
#     elif i == 'C':
#         Sum = Sum + 100
#     elif i == 'D':
#         Sum = Sum + 1000
#     elif i == 'E':
#         Sum = Sum + 10000
#     elif i == 'F':
#         Sum = Sum + 100000
#     elif i == 'G':
#         Sum = Sum + 1000000
# print(Sum)

    
def find(list):
    for i in range(len(list)):
        
        
        return (list[i])        

l = []
n = int(input("Enter list Holding values : "))
for i in range (n):
    a = int(input("Enter "+str(int(i+1))+ " value : "))
    l.append(a)

ans = find(l)
print(ans)

