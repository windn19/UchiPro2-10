# создание массива
array = []

# заполнение с конца
array.append(1)
array.append(2)
array.append(3)
print(array)

# дополнение с начала
array.insert(0, 'new')
print(array)
print(array.index(3))

# удаление элемента
array.pop()
del array[0]
print(array)