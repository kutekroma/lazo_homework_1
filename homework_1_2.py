# 2. Пользователь вводит число. Выведите на экран десятичное, двоичное,
# восьмеричное и шестнадцатеричное представление этого числа с помощью
# функций bin(), oct(), hex().

# Выполнил Лазо Александр

import numbers

if __name__ == '__main__':
    try:
        number = float(input("Введите число: "))
        #проверяем, что введеное число целое или вещественное
        if (isinstance(number, numbers.Number)):
            print(f"Десятичное представление числа {number} это {int(number)}")
            print(f"Двоичное представление числа {number} это {bin(int(number))}")
            print(f"Восьмеричное представление числа {number} это {oct(int(number))}")
            print(f"Шестнадцатеричное представление числа {number} это {hex(int(number))}")
    # обрабатываем ввод не числа, а другого символа
    except ValueError:
        print(f"Вы ввели не числовое значение. Введите число, пожалуйста")