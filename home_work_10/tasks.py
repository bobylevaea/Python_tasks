# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего 
# из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без 
# get_dummies? 
  
# import random 
# lst = ['robot'] * 10 
# lst += ['human'] * 10 
# random.shuffle(lst) 
# data = pd.DataFrame({'whoAmI':lst}) 
# data.head() 
  
  
import pandas as pd 
  
import random 
lst = ['robot'] * 10 
lst += ['human'] * 10 
random.shuffle(lst) 
data = pd.DataFrame({'whoAmI':lst}) 
data.head(10) 
  
# Метод get_dummies 
pd.get_dummies(data['whoAmI']).head(10) 
  
# Без метода get_dummies 
pd.DataFrame({'human': data['whoAmI'] == 'human', 
               'robot': data['whoAmI'] == 'robot'}).astype(int).head(10)


# Задано натуральное N. Напишите программу, которая выводит треугольник со сторонами из N нулей, заполненных "x". 
# На горизонтальных линиях символы разделяются одним пробелом. Первый нолик в N-й строке должен быть первым символом в этой строке.
def draw_pattern(n):
    if n == 1:
        print('0')
        return
    
    # Определяем размерность рисунка
    size = n * 2 - 1
    
    # Создаем пустой двумерный массив для рисунка
    pattern = [[' ' for _ in range(size)] for _ in range(size)]
    
    # Заполняем крайний правый столбец
    for i in range(size):
        pattern[i][-1] = '0'
    
    # Заполняем вторые сначала и с конца строки
    pattern[size-2][-3] = '0'
    pattern[1][-3] = '0'
    
    # Заполняем строку под номером n-1
    pattern[n-1][0] = '0'
    for j in range(2, size - 1):
        if j % 2 == 0:
            pattern[n-1][j] = 'x'
        else:
            pattern[n-1][j] = ' '

  
    # Заполняем верхнюю часть треугольника
    a = 1
    b = 2
     
    while n-1-a >= 1:
        for j in range(b-1, size - 1):
            if j % 2 == 0:
                pattern[n-1-a][j] = 'x'
            else:
                pattern[n-1-a][j] = ' '
        pattern[n-1-a][0+b] = '0'
        a += 1
        b += 2 

    # Заполняем нижнюю часть треугольника
    c = 1
    d = 2
    
    while n-1+c <= size-2:
        for j in range(d-1, size - 1):
            if j % 2 == 0:
                pattern[n-1+c][j] = 'x'
            else:
                pattern[n-1+c][j] = ' '
        pattern[n-1+c][0+d] = '0'
        c += 1
        d += 2  
    
    # Выводим рисунок на экран
    for row in pattern:
        print(''.join(row))


draw_pattern(100)
