import math
def qvadr(x):
    if math.sqrt(x) == int(math.sqrt(x)):
        return 'Число является квадратом целого числа'
    else:
        return 'Число не является квадратом целого числа'

def pol(x):
    s = str(x)
    if s[0] == s[-1]:
        return 'Число является трехзначным палиндромом'
    else:
        return 'Число не является трехзначным палиндромом'
def task1():
    while True:
        ch = float(input('Введите число:'))
        print(qvadr(ch))
        print(pol(ch))
#done

import numpy as np
import matplotlib.pyplot as plt
def task2():
    def f(x):
        if x >= math.pi:
            return math.tan(x) + math.sin(x)
        else:
            return x ** 2 - math.pi ** 2
    a = float(input('Введите значение a:'))
    b = float(input('Введите значение b:'))
    x = np.linspace(a, b, 100)  # Диапазон значений x от 0 до 2π
    y = [f(i) for i in x]  # Вычисление значений функции f(x) для каждого значения x
    plt.plot(x, y)  # Построение графика
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('График функции f(x)')
    plt.grid(True)
    plt.show()
#2 не сделано
def task3():
    def number_in_new_numeral_system(d, b):
        if b > 36:
            return 'Основание системы счисления должно быть не больше 36ти'
        num = ''
        while d > 0:
            d, r = divmod(d, b)
            if r > 9:
                r = chr(ord('A') + r - 10)
            num = str(r) + num
        return num
    num = int(input("Десятичное число:"))
    base = int(input("Основание от 2 до 36:"))
    ch = number_in_new_numeral_system(num,base)
    #print("Результат: {0:.4f}".format(ch))
    print('Результат: '+ ch)
#done
#4 task
def task4():
    x = int(input("Введите координату x: "))
    y = int(input("Введите координату y: "))
    f = 0
    if -3 <= x <= -2 and ((((x+1)**2 + (y-3)**2) <= 4) or ((y <= x+2) and (y >= -2/3*x-3))):
        f+=1
    elif -2 <= x <= -1 and ((((x+1)**2 + (y-3)**2)<=4 and y>=2*x+7) or (((x+1)**2 + (y-3)**2)<=4 and y<=x+5) or ((y<=x+2) and (y>=-2/3*x-3))):
        f += 1
    elif -1 <= x <= 0 and (((y<=x+5) and (y>=x+1)) or ((y>=-2/3*x-3) and (y<=-3*x-3))):
        f += 1
    elif 0<=x<=1 and (y<=-2*x+5) and (y>=x+1):
        f += 1
    elif 1<=x<=3 and (y>=x+9) and (y<=0,5*x+2.5):
        f += 1

    s = 0
    if 2 <= x <= 4 and (((y <= 0.5*x-5) and (y >= -4)) or ((((x-4)**2 + (y+1)**2) <= 4) and (y <= -1/2*x)) or ((y <= -x+3) and (y >= -3/2*x+4))):
        s += 1
    elif 4 <= x <= 5 and (((y <= -3/2*x+9) and (y >= -5*x+23)) or ((y <= -x+3) and (y >= -4))):
        s += 1
    elif 5 <= x <= 6 and (((y <= -3/2*x+9) and (y >= -4)) or ((y >= -5*x+30) and (y <= -2.5*x +17.5))):
        s += 1
    elif 6 <= x <=7 and (((y <= -2.5*x+17.5) and (y >= x-7)) or ((y <= -3*x+17) and (y >= -4))):
        s += 1
    if f >= 1:
        print('Точка принадлежит первой фигуре')
    else:
        if s >= 1:
            print('Точка принадлежит второй фигуре')
        else:
            print('Точка не принадлежит обоим фигурам')

#4 done

def find_floor(k, c, n):
    floor = 0
    while k > 0:
        k -= n
        floor += 1
        if k > 0:
            k -= c
            floor += 1
        else:
            break
    return floor
def task5():
    ch = int(input("Введите количество квартир на четных этажах: "))
    nech = int(input("Введите количество квартир на нечетных этажах: "))
    kv_number = int(input("Введите номер квартиры: "))
    co = int(input("Введите количество этажей: "))
    if co % 2:
        count_kv = (ch + nech) * (co // 2)
    else:
        count_kv = (ch + nech) * (co // 2) + nech

    if kv_number < 1 or kv_number > count_kv:
        print("Неверный номер квартиры")
    else:
        floor = find_floor(kv_number, ch, nech)
        if floor % 3 == 0:
            fl1 = floor + 1
            fl2 = floor - 1
            print("Лифт не может приехать на этаж, выберите ближайший этаж:", fl1, '/', fl2)
        else:
            print ("Лифт едет на этаж", floor)
#done

#Task 6
def dengi_inflyaciya(stipendia, rashodi, n):
    money = stipendia
    inflyaciya = [0.03, 0.05]
    count = 0
    for month in range(1, n + 1):
        count += 1
        inflyaciya_m = inflyaciya[month % 2]
        rash = rashodi * (1 + inflyaciya_m)
        money -= rash
        if count == n:
            return(abs(money))
        else:
            money += stipendia
def task6():
    stipendia = float(input('Введите стипендию студента: '))
    rashodi = float(input('Введите расходы студента: '))
    n = int(input('Введите количество месяцев: '))
    print(dengi_inflyaciya(stipendia, rashodi, n))
#DONE

#Task 8
def f(k):
    if k == 1:
        return 1
    return f(k-1)*k

def task8():
    n = int(input())
    x = int(input())
    ch = [int(t) for t in range(2, n+1)]
    u = [int(p) for p in range(3, n**2, 2)]
    s = x
    for i in range(0, n-1):
        k = u[i]
        t = ch[i]
        s = s + (f(k-t))*(x**k/f(k))
    print(s)
#done

