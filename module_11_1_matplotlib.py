
import matplotlib.pyplot as plt
import numpy as np

#Matplotlib используют для визуализации данных любой сложности.
#Библиотека позволяет строить разные варианты графиков:
#линейные, трёхмерные, диаграммы рассеяния и другие, а также комбинировать их.
#линейный график
x = [1, 2, 2.5, 3, 4, 5, 6, 7, 7.5, 8, 9]
y = [21, 24, 28, 28, 25, 24, 25, 28, 28, 24, 21]
#строим график
plt.plot(x, y)
plt.xlabel('Ось х') #Подпись для оси х
plt.ylabel('Ось y') #Подпись для оси y

bbox_properties=dict(
    boxstyle="roundtooth, pad=0.3",
    ec="lightcoral",
    fc="w",
    ls="-",
    lw=1
)
plt.title('Линейный график', fontsize=15, bbox=bbox_properties,
          color = 'rebeccapurple', fontstyle="italic",fontweight="bold")#Название
#mec - контур markera
#ms - markersize

plt.plot(x, y, color='mediumpurple', marker='o', ms=7,  mec='mediumblue')
plt.grid()
plt.show()

#numpy.arange(start, stop, step)
#В NumPy функция . cos() вычисляет косинус каждого элемента массива
x = np.arange(0.0, 7, 0.03)
y = np.cos(x*np.pi)
plt.xlabel('Ось х', fontsize=10) #Подпись для оси х
plt.ylabel('Ось y', fontsize=10) #Подпись для оси y
bbox_properties=dict(
    boxstyle="sawtooth, pad=0.3",
    ec="yellowgreen",
    fc="lemonchiffon",
    ls="-",
    lw=2
)
plt.title('График с заливкой', fontsize=15, bbox=bbox_properties,
          color = 'darkgreen', fontstyle="italic",fontweight="bold") #Название
plt.plot(x, y, c="firebrick")
plt.fill_between(x, y, where=y>=0, color="yellowgreen")
plt.fill_between(x, y, where=y<=0, color="darkseagreen")

plt.show()