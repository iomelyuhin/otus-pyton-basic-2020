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
    all_numbers = []

    for num in arr_nums:
        res = num ** p

        if p == 2:
            print("Квадрат числа", num, "равен:", res)
        else:
            print(num, "в степени", p, "равно:", res)

        all_numbers.append(res)

    return all_numbers


current_num = power(arr_of_numbers)

user_power = input("В какую степень хочешь возвести свои числа? ")

int_user_power = int(user_power)

# power(arr_of_numbers, int_user_power)

print('Функция power возвращает:', power(arr_of_numbers, int_user_power))


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


def fib(n):
    fib_list = []
    fib1, fib2 = 0, 1

    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        fib_list.append(fib1)
    return fib_list


res_fib = fib(int(input('Введите количество чисел в списке фибоначи: ')))

print(res_fib)









