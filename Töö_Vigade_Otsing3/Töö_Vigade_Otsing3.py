from random import *
s=nol=pos=neg=[]
def vahetus(a: int,b: int):
    """Kui a<b siis vahetame neid
    :param int a: Arv, mis in suurem kui b
    :param int b: Arv, mis on väiksem kui a
    :rtype:int, int
    """
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n: int,loend: list,a: int,b: int):
    """Lisab loendisse a-st b-ni suuruses n
    :param int n: väärtuste arv loendis
    :param list loend: väärtuste loetelu
    :param int a: min
    :param int b: max
    :rtype: None 
    """
    for i in range(n):
        loend.append(randint(a,b))
    

def jagamine(loend: list,p: list,n: int,nol: list):
    """Määrab positiivsed, negatiivsed ja nullväärtused
    :param list loend: väärtuste loetelu
    :param list p: positiivsed väärtused
    :param int n: väärtuste arv loendis
    :param list nol: null väärtused
    :rtype: None
    """
    for el in loend:
        if el>0:
            p.append(el)
        elif el<0:
            n.append(el)
        else:
            nol.append(el)

def keskmine(loend: list,n: int):
    """Määrab keskel
    :param list loend: väärtuste loetelu
    :param int n: väärtuste arv loendis
    :rtype: float
    """
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2)
    return kesk

def lisamine(loend: list,el: int):
    """
    :param list loend: väärtuste loetelu
    :param int el: 
    :rtype: None
    """
    loend.append(el)
    loend.sort()

def arvud_loendis():
    """
    :rtype: None
    """
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>=maxi:
        mini,maxi=vahetus(mini,maxi)
    generaator(n,s,mini,maxi)
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort()
    print("Отсортированный список",s)
    jagamine(s,pos,neg,nol)
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",nol)
    kesk=keskmine(pos,n)
    lisamine(s,kesk)
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg,n)
    lisamine(s,kesk)
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")
    sort(s)
    print(s)
arvud_loendis()

