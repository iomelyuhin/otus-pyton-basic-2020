from datetime import datetime

list_of_num = input("Введите целые числа через пробел ").split()

arr_of_numbers = list(map(int, list_of_num))


def timeit(func):
    def wrapper(*args):
        start = datetime.now()
        result = func(*args)
        print("На вычисление ушло: ", datetime.now() - start)
        return result
    return wrapper


@timeit
def power(arr_nums, p=2):
    for num in arr_nums:
        res = num ** p

        if p == 2:
            print("Квадрат числа", num, "равен:", res)
        else:
            print(num, "в степени", p, "равно:", res)
    return res


current_num = power(arr_of_numbers)

user_power = input("В какую степень хочешь возвести свои числа? ")

int_user_power = int(user_power)

power(arr_of_numbers, int_user_power)

userswitchnum = input("Выберите четные(ч) или нечётные(н) числа? ")


def return_numbers(numbers, userswitchnum):
    if userswitchnum == "ч":
        odd = list(filter(lambda x: x % 2 == 0, numbers))
        print("Четные числа из вашего списка: ", odd)
    elif userswitchnum == "н":
        even = list(filter(lambda x: x % 2 != 0, numbers))
        print("Нетные числа из вашего списка: ", even)
    else:
        print('Вы не выбрали тип числа, вот весь список:', numbers)


return_numbers(arr_of_numbers, userswitchnum)

