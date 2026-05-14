import math
from itertools import count

from main import x


#questiom 1
def quadratic(a,b,c):
    d=b**2-4*a*c
    if d> 0:
        x1=(-b+math.sqrt(d)/(2*a))
        x2=(-b-math.sqrt(d)/(2*a))
        print("there are two real roots")
        print(x1)
        print(x2)
    elif d==0:
        x3=(-b)/(2*a)
        print("there is 1 real root")
        print(x3)
    else:
        print("error")


#question2
num=int(input("what is your number"))
if num>=1000 and num<=9999 and num%2==0 and num%10!=0:
    print("good")
else:
    print("bad")


#question3
def f(x):
    if x==1:
        return 1
    else:
        return x*f(x-1)
x=int(input("what is your number"))
print(f(x))

#question4
AES=int(input("what is you AES grade"))
Maths=int(input("what is you Maths grade"))
Physics=int(input("what is your physics grade"))
Programming=int(input("what is your programming grade"))
gpa=((AES*Maths*Physics*Programming)/(4))
if AES < 0 or AES > 100 or Maths < 0 or Maths > 100 or Physics < 0 or Physics > 100 or Programming < 0 or Programming > 100:
    print("error")
elif AES < 40 or Maths < 40 or Physics < 40 or Programming < 40:
    print("you can not pass because one of your subjects is less than 40")
elif gpa < 60:
    print("you can not pass because your gpa is less than 60")
else:
    print("pass")