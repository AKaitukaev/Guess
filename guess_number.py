from random import randint


computer_value = randint(1,100)
while True:
    operator_value = int(input('Введите ваше число '))
    if computer_value > operator_value:
        print('Ваше число меньше того, что загадано')
    if computer_value < operator_value:
        print('Ваше число больше того, что загадано')
    if computer_value == operator_value:
        print('Отличная интуиция! Вы угадали число :)')
        break
