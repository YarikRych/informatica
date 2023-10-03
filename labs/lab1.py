import math

def task1():
    x=float(input('Введите переменную x:'))
    y=float(input('Введите переменную y:'))
    z=float(input('Введите переменную z:'))
    a1=(x*y-(x+y))/(x*y+(x+y))
    a2=(((x+y)/2)**2)/((x+y**2)/2 + ((x-y)/2)**2)
    a=a1*a2
    b=math.log(abs(z-1),3)+z**(1/4)+(abs(y))**(1/4)
    print("a = {0:.4f}".format(a))
    print("b = {0:.4f}".format(b))
task1()
def task2():
    x=float(input('Введите переменную x:'))
    a=-5
    b=-2
    c=4
    f=(a*x+b)*c/(x**(4/3))+ x**a
    print("f = {0:.4f}".format(f))

def task3():
    x=float(input('Введите переменную x:'))
    f=((math.tan(x))**3)*(abs(math.log(x**3)))
    print("f = {0:.4f}".format(f))

def task4():
    l=float(input('Введите длину AB:'))
    h=float(input('Введите высоту h:'))
    s1=(l**2)*(3**(1/2))/4
    r=(l**3)/(4*s1)
    pi=math.pi
    s2=pi*(r**2)
    v=(1/3)*s2*h
    print("v = {0:.4f}".format(v))

def task5():
    M=float(input('Введите массу конькобежца:'))
    m=float(input('Введите массу шайбы:'))
    u=float(input('Введите скорость шайбы:'))
    q=float(input('Введите коэффициент трения:'))
    g=9.8
    u1=m*u/M
    s=u1**2/2*q*g
    print("s = {0:.4f}".format(s))

def task6():
    r=float(input('Введите радиус основания:'))
    h=float(input('Введите высоту цилиндра:'))
    s=2*r*4*h
    print("s = {0:.4f}".format(s))

def task7():
    a=float(input('Введите переменную a(не равна 0,a>-100 или a=-100):'))
    b=float(input('Введите переменную b(b<100 или b=100):'))
    x=(-b)/a
    x=round(x,4)
    print("x = {0:.4f}".format(x))

def task8():
    r1=float(input('Введите радиус:'))
    r2=float(input('Введите знаение, насколько ближе:'))
    r2=r1-r2
    n=r1/r2
    print("n = {0:.4f}".format(n))

def task9():
    u=float(input('Введите цену 1 юаня в тенге:'))
    t=float(input('Введите количество юаней:'))
    k=float(input('Введите процент комисии:'))
    d=u*t*(1-(k/100))
    d=round(d,2)
    print("d = {0:.4f}".format(d))







