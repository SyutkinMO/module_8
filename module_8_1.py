# --------------"Try и Except"--------------

def add_everything_up(a, b):
    try:
        result = a + b  # в самой функции сразу прописываем ошибку
    except TypeError as exc:  # сохраняем тип ошибки в переменную exc
        return (str(a) + str(b))  # если ввели строку возвращаем результат в виде сложения строк
    else:
        return round((a + b), 3)  # если ошибки не было возвращаем результат сложения


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
