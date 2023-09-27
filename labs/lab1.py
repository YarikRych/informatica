import math
x=int(input())
y=int(input())
z=int(input())
def task1(x,y,z):
    a1=(x*y-(x+y))/(x*y+(x+y))
    a2=(((x+y)/2)**2)/((x+y**2)/2 + ((x-y)/2)**2)
    a=a1*a2
    b=math.log(abs(z-1),3)+x**(1/4)+(abs(y))**1/4
    return a,b

def task2(x):
    a=-5
    b=-2
    c=4
    f=(a*x+b)*c/(x**(4/3))+ x**a
    return f

def task3(x):
    f=((math.tan(x))**3)*(abs(math.log(x**3)))
    return f

l=int(input())
h=int(input())
def task4(l,h):
    s1=(l**2)*(3**(1/2))/4
    r=(l**3)/(4*s1)
    pi=math.pi
    s2=pi*(r**2)
    v=(1/3)*s2*h
    return v

M=int(input())
m=int(input())
u=int(input())
q=int(input())
def task5(M,m,u,q):
    g=9.8
    u1=m*u/M
    s=u1**2/2*q*g
    return s

r=int(input())
h=int(input())
def task6(r,h):
    s=2*r*4*h
    return s

a=int(input())
b=int(input())
def task7(a,b):
    x=(-b)/a
    s=str(x)
    n=s.find('.')
    x=s[0,n]+s[n,n+4]
    return x

r1=int(input())
r2=int(input())
def task8(r1,r2):
    r1=r1/100
    r2=r1-r2
    r2=r2/100
    pi=math.pi
    n=r1/r2
    return n

u=int(input())
t=int(input())
k=int(input())
def task9(u,t,k):
    d=u*t*k/100
    s=str(s)
    n=s.find('.')
    x=s[0,n]+s[n,n+2]
    return x
    




