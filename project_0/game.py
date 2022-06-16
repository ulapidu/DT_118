import numpy as np
number = np.random.randint(1, 1001) # загадываем число
count=0
while True:
    count+=1
    predict_number=int(input('Угадайте число от 1 до 1001!'))
    
    if predict_number > number:
        print('Введите число по-меньше!')
    elif predict_number < number:
        print('Введите число по-больше!')
    else:
        print(f"Вы угадали число: {number}, за {count} попыток")
        break
    