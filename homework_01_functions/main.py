print('hi!')
list_of_num = input("Введите целые числа через пробел ").split()

arr_of_numbers = list(map(int, list_of_num))

def power(a, p=2):
    res = a ** p
    if p == 2:
        print("Квадрат числа", a, "равен:", res)
        return res
    else:
        print(a, "в степени", p, "равно:", res)
        return res

current_num = list(map(power, arr_of_numbers))

user_power = input("В какую степень хочешь возвести свои числа? ")
int_user_power = int(user_power)

for num in arr_of_numbers:
    power(num, int_user_power)

#TODO
# - написать функцию, которая на вход принимает список из целых чисел, и возвращает только чётные/нечётные/простые числа (выбор производится передачей дополнительного аргумента)
# - создать декоратор для замера времени выполнения функции
