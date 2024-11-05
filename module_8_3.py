# ---------------Создание исключений---------------


class Car:

    def __init__(self, model, vin_number, numbers):
        """
        Методы __is_valid_vin и __is_valid_numbers вызываются при создании объекта
        (при объявлении атрибутов __vin и __numbers).
        Реализовано через проверку в приватных функциях класса, в случае ошибки
        идёт её перехват в блоке except посредством передачи ошибки через raise
        """
        self.model = model  # Атрибут объекта model - название автомобиля (строка).
        if self.__is_valid_vin(vin_number):
            self.__vin = vin_number  # Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers  # Атрибут __numbers - номера автомобиля (строка).

    def __is_valid_vin(self, vin_number):
        """
        Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность.
        Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
        Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер',
        если передано не целое число. (тип данных проверяется функцией isinstance).
        Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера',
        если переданное число находится не в диапазоне от 1000000 до 9999999 включительно.
        Возвращает True, если исключения не были выброшены.
        :param vin_number:
        :return: True or raise
        """
        if isinstance(vin_number, float):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if 1000000 <= vin_number <= 9999999:
            return True
        else:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')

    def __is_valid_numbers(self, numbers):
        """
        Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность.
        Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
        Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров',
        если передана не строка. (тип данных проверяется функцией isinstance).
        Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера',
        переданная строка должна состоять ровно из 6 символов.
        Возвращает True, если исключения не были выброшены.
        :param numbers:
        :return: True or raise
        """
        if isinstance(numbers, str):
            pass
        else:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return True


class IncorrectVinNumber(Exception):
    """
    Класс исключений IncorrectVinNumber, объект которого обладает атрибутом message - сообщение,
    которое будет выводиться при выбрасывании исключения.
    """

    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    """
    Класс исключений IncorrectCarNumber, объект которого обладает атрибутом message - сообщение,
    которое будет выводиться при выбрасывании исключения.
    """

    def __init__(self, message):
        self.message = message


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
