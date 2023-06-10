def func2(a,*b):
     global n
     s = sum(b)
     print(s)
     c = a *(n//10)
     n = c[::-1]
     return c
L= [3,2,1]
n = 20
s = func2(L,6,7,8)
print("s=",s,"n=",n)
