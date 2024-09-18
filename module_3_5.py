# Задача "Рекурсивное умножение цифр":

def get_multiplied_digits (number):
    str_number = str(number)
    first = int(str_number[0])
    # print (first)
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        first = int(str_number[0])
        return first


result = get_multiplied_digits(40203)
print(f'Произведение цифр равно  - {result}')


