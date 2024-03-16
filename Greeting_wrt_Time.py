import time
a = time.strftime('%H:%M:%S')
b = time.strftime('%H')
print("Current Time is : ",a)
if 6 < int(b) < 12:
    print("Good Morning : Subah Ho gai Mamu")
elif 12 < int(b) < 16:
    print("Good Afternoon : Snap Time")
elif 16 < int(b) < 20:
    print("Good Evening : Mooj Ker")
else:
    print("Good Night : Chal Sooja ab")
