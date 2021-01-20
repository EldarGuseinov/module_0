import numpy as np


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# используется алгоритм поиска загаданного числа путем сокращения диапазона поиска в 2 раза в каждой итерации цикла 
def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict_num = 50 # Стартовое значение сравнения
    prederict_wiegth = 50 # Число используемое для изменений и перехода внутри цикла 
    while number != predict_num:
        count+=1
        if number > predict_num: 
            predict_num += round(prederict_wiegth/2)
            prederict_wiegth = round(prederict_wiegth/2)
        elif number < predict_num: 
            predict_num -= round(prederict_wiegth/2)
            prederict_wiegth = round(prederict_wiegth/2)
        if prederict_wiegth == 0 :
            if number > predict_num: 
                predict_num += 1
                count+=1
            elif number < predict_num: 
                predict_num -= 1
                count+=1
        #print(f"{predict_num} != {number} % {prederict_wiegth}")
    return(count) # выход из цикла, если угадали
# Проверяем
score_game(game_core_v2)
#game_core_v2(100)

