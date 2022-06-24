#### 1
print("Введите число: ", end='')
a = input()
b = 1000
print("Введите строку: ", end='')
c = input()
print(a, b, c)

#### 2

print('Введите вермя в скундах: ', end='')
s = int(input())
m = s // 60
s -= m * 60
h = m // 60
m -= h*60
print(h, m, s, sep=':')

#### 3

print('Введите число: ', end='')
n = input()
print(int(n) + int(n+n) + int(n + n + n))

#### 4

print('Введите число: ', end='')
n = input()
mx = -1
ct = 0
while ct < len(n):
    if int(n[ct]) > mx:
        mx = int(n[ct])
    ct += 1
print(mx)

#### 5

print('Введите выручку: ', end='')
p = int(input())
print('Введите издержки: ', end='')
n = int(input())
tr = 0
if p > n:
    tr = 1
    print('Вы получаете прибыль')
else:
    print('У вас убыток(')

#### 6

if tr == 1:
    print('Рентабельность', (p - n) / p)
    print('Введите колличество сотрудников: ', end='')
    wor = int(input())
    print('Прибыль на сотрудника: ', (p - n) / wor)

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