'''Игра компьютер угадает число меньше чем за 20 попыток'''

import numpy as np

number = np.random.randint(1, 101)
list_num=list(range(101))
count = 0

while True:
    count+=1
    mean = int((list_num[0]+list_num[-1]) / 2)
    
    if mean > number:
       list_num[-1] = mean
    
    elif mean < number:
         list_num[0] = mean

    else:
         print(f"Компьютер угадал число за {count} попыток. Это число {number}")
         break #конец игры выход из цикла.