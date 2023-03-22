# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5


from random import randint

N = int(input("Укажите длину массива: "))

array = []
i = 0

while i < N:
    array.append(randint(0,10))
    i+=1
print(array)    

X = int(input("Укажите число Х: "))
nearestValue = array[0]
# Вариант1
for element in array:
    if abs(X - element) < abs(X - nearestValue):
        nearestValue = element
print(nearestValue) #если ближайших чисел несколько, то выводиться будет последнее найденное


