import numpy as np

#NumPy не просто работает с многомерными массивами, но и делает это быстро.
#как и у Matlab, для NumPy существуют пакеты, расширяющие её функциональность, — например, библиотека SciPy или Matplotlib
#NUMPY заменяет циклы
# NUMPY
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
#сколько измерений
print('Кол-во измерений (переменная a):', a.ndim)
print('Кол-во измерений (переменная b):', b.ndim)
#посчитаем кол-во строк и столбцов
print('Кол-во строк и столбцов по переменной a:', a.shape)
print('Кол-во строк и столбцов по переменной b:',b.shape)
print(a.size)
print(b.size)
#какое кол-во байт в памяти занимает один элемент
print('Кол-во байт для одного элемента параметра a:', a.itemsize)
print('Кол-во байт для одного элемента параметра b:', b.itemsize)
print('Кол-во байт для всех элементов параметра a:', a.nbytes)
print('Кол-во байт для всех элементов параметра b:', b.nbytes)

#заменяем циклы

array1 = [1, 2, 3, 4]
array2 = [5, 6, 7, 8]
# without vectorization
result = []
for i in range(len(array1)):
    result.append(array1[i] + array2[i])
print('without vectorization:', result)

array3 = np.array([1, 2, 3, 4])
array4 = np.array([5, 6, 7, 8])

result1 = np.add(array3, array4).tolist()
print('with vectorization:', result1)




