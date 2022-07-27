'''1. Создайте программу для игры с конфетами человек
против человека.
Условие задачи: На столе лежит 2021 конфета.
Играют два игрока делая ход друг после друга. Первый
ход определяется жеребьёвкой. За один ход можно
забрать не более чем 28 конфет. Все конфеты оппонента
достаются сделавшему последний ход. Сколько конфет
нужно взять первому игроку, чтобы забрать все конфеты
у своего конкурента?
a) Добавьте игру против бота
b) (доп) Подумайте как наделить бота ""интеллектом""
'''

from random import randint

def input_name(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, value):
    print(f"Ходил {name}, он взял {k}. Осталось на столе {value} конфет.")

kol_pl= int(input("Введите колиество игроков (1 или 2), если выбран 1 игрок - за второго игрока сыграет компьютер: ")) 
if kol_pl==1:
    player1 = "Бот Виталий"
    player2 = input("Введите Ваше Имя:")
    value = int(input("Введите количество конфет на столе: "))
    flag = randint(0,1)
    if flag:
        print(f"Первый ходит {player1}")
    else:
        print(f"Первый ходит {player2}")

    while value > 28:
        if flag:
            k = randint(1,28)
            value -= k
            flag = False
            p_print(player1, k, value)
        else:
            k = input_name(player2)
            value -= k
            flag = True
            p_print(player2, k, value)

    if flag:
        print(f"Выиграл {player1}")
    else:
        print(f"Выиграл {player2}")
else:
    if kol_pl==2:
        player1 = input("Введите имя первого игрока: ")
        player2 = input("Введите имя второго игрока: ")
        value = int(input("Введите количество конфет на столе: "))
        flag = randint(0,1)
        if flag:
            print(f"Первый ходит {player1}")
        else:
            print(f"Первый ходит {player2}")

        while value > 28:
            if flag:
                k = input_name(player1)
                value -= k
                flag = False
                p_print(player1, k, value)
            else:
                k = input_name(player2)
                value -= k
                flag = True
                p_print(player2, k, value)

        if flag:
            print(f"Выиграл {player1}")
        else:
            print(f"Выиграл {player2}")
    else: 
        print("Вы ввели некорректное число игроков")