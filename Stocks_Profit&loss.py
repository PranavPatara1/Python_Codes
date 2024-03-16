''' This code Just add the stock price from lower to higher and sum up 
Output like :

Enter List Elements : 100 180 240 40 200 600
700   --> take lower value as buy and max value as sell,
Then Day 1 = 100 as buy and sell on day 3 = 240, so 240-100 = 140
And buy on day 4 = 40 and sell on day 6 = 600, so 600 - 40 = 560
Over all profit = 140 + 560 = 700  
'''
# class Stock:
#     def __init__(self,a,p):
#         self.a = a
#         self.p = p
#     def Profit(self):
#         profit = 0
#         for i in range(1, self.p):
#             if self.a[i] > self.a[i-1]:
#                 profit += self.a[i] - self.a[i-1]
#         return profit
    
# if __name__ == '__main__':
#     a = list(map(int, input("Enter List Elements : ").strip().split(" ")))
#     Val = Stock(a, len(a))
#     Value = Val.Profit()
#     print(Value)


''' This code take lower value as buy and higher values as sell :
Output like :

Enter List Elements : 7 5 4 2 1
0  --> Because buy is on last day

Enter List Elements : 7 1 5 3 6 4
5  --> buy on 2 day = 1 and sell on 5 day = 6, then 6-1 = 5
'''
class Stock:
    def __init__(self,a,p):
        self.a = a
        self.p = p
    def Profit(self):
        profit = 0
        pos = 0
        v = self.a[0]
        f = 0
        for i in range(self.p):
            if self.a[i] < v:
                v = self.a[i]
                pos = i
        for i in range(pos,self.p):
            if self.a[i] > f:
                f = self.a[i]
        profit = f - v
        return profit
    
if __name__ == '__main__':
    a = list(map(int, input("Enter List Elements : ").strip().split(" ")))
    Val = Stock(a, len(a))
    Value = Val.Profit()
    print(Value)