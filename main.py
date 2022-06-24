#### 1
a = input("Введите число: ")
b = 1000
c = input("Введите строку: ")
print(a, b, c)

#### 2

s = int(input('Введите вермя в скундах: '))
m = s // 60
s -= m * 60
h = m // 60
m -= h*60
print(h if h > 10 else '0' + str(h), m if m > 10 else '0' + str(m), s if s > 10 else '0' + str(s), sep=':')

#### 3

n = input('Введите число: ')
print(int(n) + int(n+n) + int(n + n + n))

#### 4

n = input('Введите число: ')
mx = -1
ct = 0
while ct < len(n):
    if int(n[ct]) > mx:
        mx = int(n[ct])
    ct += 1
print(mx)

#### 5

p = int(input('Введите выручку: '))
n = int(input('Введите издержки: '))
tr = 0
if p > n:
    tr = 1
    print('Вы получаете прибыль')
else:
    print('У вас убыток(')

#### 6

if tr == 1:
    ern = p - n
    print('Рентабельность', ern / p)
    wor = int(input('Введите колличество сотрудников: '))
    print('Прибыль на сотрудника: ', ern / wor)

#### 7

a = int(input())
b = int(input())

ct = 1
print(f'{ct}-й день: {a}')
while a < b:
    a *= 1.1
    ct += 1
    print(f'{ct}-й день: {a}')
print(f'Ответ на {ct} день')