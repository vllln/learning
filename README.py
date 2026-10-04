<h1>БАЗА<h1>

# остаток от деления
print(10 % 3) # выведет 1
print(10 % 2) # вывдете 0

# символы строки
txt = 'abcde'
print(txt[1]) #выведет b
print(txt[-1]) #выведет d

# экранирование
tst = "abcd\"fr\'23"
print(tst)

# длина строки
print(len('Python')) # выведет 6

# многострочные строки
print('''
1
2
3
''')

# преобразование к строке
tst1 = 'abc'
tst2 = 1
tst3 = tst1 + str(tst2)
print(tst3)

tst = 456
s = str(tst)  # превратили в строку "456"
# Просто берём буквы по очереди (0, 1, 2), делаем числами и складываем:
print(int(s[0]) + int(s[1]) + int(s[2]))


<h1>Список<h1>

# введение
lst = []
# or
lst = list('1')
print(lst)
# or
lst = list('1234')
print(lst) # ['1', '2', '3', '4']

# разбиение строки в список
txt = '1-2-3-4'
print(txt.split('-')) # ['1', '2', '3', '4']

txt = '1-2-3-4'
print(txt.split()) # ['1-2-3-4']

# получение отдельного элемента списка
lst = ['a', 'b', 'c', 'd', 'e']
print(lst[0]) # 'a'
print(lst[3]) # 'd'
print(lst[-1]) # 'e'

# длина списка
lst = [1, 2, 3]
print(len(lst)) # 3

# изменение элементов списка
lst = [1, 2, 3]
lst[0] = '!'
print(lst) # ['!', 2, 3]

# добавление элементов в конец списка
lst = ['a', 'b', 'c']
lst.append('d')
print(lst) # ['a', 'b', 'c', 'd']

# добавление по позиции
lst = ['a', 'b', 'c', 'd']
lst.insert(1, '2')
print(lst) # ['a', '2', 'b', 'c', 'd']

# объединение списков с помощью extend
lst1 = [1, 2, 3]
lst2 = [3, 4, 5]

lst1.extend(lst2)
print(lst1) # [1, 2, 3, 4, 5, 6]

# объединение списков
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

res = lst1 + lst2
print(res) # [1, 2, 3, 4, 5, 6]

# добавление в список
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst1 += lst2
print(lst1) # [1, 2, 3, 4, 5, 6]

# удаление элементов операторов del
lst = [1, 2, 3]
del lst[0]
print(lst) # [2, 3]

# удаление по значению
lst = [1, 2, 3]
lst.remove(1)
print(lst) # [2, 3]

# получение и удаление элемента
lst = [1, 2, 3]
print(lst.pop(0)) # 1

# or
lst = [1, 2, 3]
print(lst.pop()) # 3
print(lst) # [1, 2]

# удаление всех элементов
lst = [1, 2, 3]
lst.clear()
print(lst) # []

# поиск индекса по его значению
lst = [1, 2, 3]
print(lst.index(1)) # 0

# задаем начало и конец поиска
lst = [1, 2, 3, 1, 4]
print(lst.index(1, 2, 4)) # 3

# проверка наличия элемента в списке
lst = [1, 2, 3]
res = 1 in lst
print(res) # True

# подсчет элементов в списке
# чтобы найти кол-во совпадений элемента в списке, мы используем count
lst = [1, 2, 1, 3]
print(lst.count(1)) # 2

# обратный порядок 
lst = [1, 2, 3]
lst.reverse()
print(lst) # [3, 2, 1]

# сортировка элементов в исходном списке
# если sort() - по возрастанию, если sort(reverse=True) - по убыванию
lst = [3, 2, 1]
lst.sort()
print(lst) # [1, 2, 3]

lst = [1, 2, 3]
lst.sort(reverse=True)
print(lst) # [3, 2, 1]

# сортировка элементов в копии списка
lst = [3, 2, 1]
res = sorted(lst)

print(res) # [1, 2, 3]

# слияние списка в строку
lst = ['1', '2', '3']
res = '/'.join(lst)
print(res) # '1/2/3'

# кортежи
tpl = ('a', 'b', 'c')
# or
tpl = 'a', 'b', 'c'

# для чего? ЗАЩИТА от изменений

tpl = tuple('abcde')
print(tpl) # ('a', 'b', 'c', 'd', 'e')

# кортеж из одного элемента
tpl = ('a',) # ОБЯЗАТЕЛЬНО ,

# отдельный элемент кортежа
tpl = ('a', 'b', 'c')
print(tpl[0]) # 'a'

# изменение элемента кортежа
tpl = ('a', 'b', 'c')
# tpl[0] = '!'  # ОШИБКА, т.к. кортежи изменять НЕЛЬЗЯtpl[0] = '!'


# длина кортежа
tpl = ('a', 'b', 'c')
print(len(tpl)) # 3

# объединение кортежей
tpl1 = ('a', 'b', 'c')
tpl2 = ('d', 'e')
res = tpl + tpl2
print(res) # ('a', 'b', 'c', 'd', 'e')

# умножение кортежей
tpl = ('a', 'b')
res = tpl * 2
print(res) # ('a', 'b', 'a', 'b')

# наличие элемента в кортеже
tpl = ('a', 'b', 'c')
res = 'a' in tpl
print(res) # True

# распаковка кортежей
tpl = ('a', 'b', 'c')
txt1, txt2, txt3, txt4 = tpl
print(txt1) # 'a'
print(txt2) # 'b'
print(txt3) # 'c'

# преобразование в кортеж
txt = 'abcde'
tpl = tuple(txt)
print(tpl) #('a', 'b', 'c', 'd', 'e')

# преобразование кортежа в список
tpl = ('a', 'b', 'c')
res = list(tpl)
print(res) # ['a', 'b', 'c']

# слияние кортежа в строку
tpl = ('a', 'b', 'c')
txt = '-'.join(tpl)
print(txt) # 'a-b-c'


# string[begin:end:step]

txt = 'abcde'
print(txt[1:3]) #'bc'
# срез от позиции
print(txt[2:]) # 'cde'
# срез до позиции
print(txt[:3]) # 'abc'

# срез с отрицательными позициями
txt = '123456789'
print(txt[2:-1]) #'345678'
# шаг выборки
print(txt[1:9:2]) # '2468'
# срез только с шагом
print(txt[::2]) # '12579'
# весь срез
print(txt[:]) # '123456789'
# переворот последовательности
print(txt[::-1])
# удаление элементов с помощью срезов
lst = [1, 2, 3, 4, 5, 6]
del lst[1:4]

print(lst)
# удаление всего с помощью срезов
del txt[::1]
print(txt)

# СЛОВАРИ - тип хранения в виде ключ-значение
dct = {}
# or
dct = {
    'a': 1,
    'b': 2,
    'c': 3
}
# можно создать с применением функции dict
dct = dict()
print(dct) # {}

dct = dict(a='1', b ='2')
print(dct) # {'a': '1', 'b': '2'}
# но числа нельяз заносить как dict(1: 'a', 2: 'b')

# значение элемента
dct = {
    'a': 1,
    'b': 2,
    'c': 3
}

print(dct['a']) # 'a'

# изменение значения
dct['a'] = '!'
print(dct) # {'a': '!', 'b': 2, 'c': 3 }

# добавление элемента
dct['x'] = '!'
print(dct) # {'a': 1, 'b': 2, 'c': 3, 'x': '!'}

# лина словаря
print(len(dct)) # 3

# объединение словарей
dct1 = {
    'a': 1,
    'b': 2,
    'c': 3
}
dct2 = {
    'd': 4,
    'e': 5
}
dct1.update(dct2)
print(dct)

# удаление п ключу
del dct['a']
print(dct) # {'b': 2, 'c': 3}

# извлечение по ключу
print(dct.pop('a')) # 1 + этот элемент изчезнет