# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for numeral in range(2, n + 1):
        for prime in prime_numbers:
            if numeral % prime == 0:
                break
        else:
            prime_numbers.append(numeral)
    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:
    def __init__(self, n):
        self.prime_numbers = []
        self.n = n
        self.i = 0

    def __iter__(self):
        self.i = 1
        return self

    def get_prime_numbers(self):
        self.i += 1
        for prime in self.prime_numbers:
            if self.i % prime == 0:
                return False
        return True

    def __next__(self):
        while self.i < self.n:
            if self.get_prime_numbers():
                self.prime_numbers.append(self.i)
                return self.i
        else:
            raise StopIteration()


def main():
    prime_number_iterator = PrimeNumbers(n=10000)
    for number in prime_number_iterator:
        print(number)


if __name__ == "__main__":
    main()


#  после подтверждения части 1 преподователем, можно делать

# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик

# Генератор простых чисел
def prime_numbers_generator(n):
    for generated_number in range(2, n + 1):
        for number_substitution in range(2, generated_number):
            if generated_number % number_substitution == 0:
                break

        else:
            yield generated_number


for prime_numbers in prime_numbers_generator(n=10000):
    print(prime_numbers)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True

# Генератор счастливого числа
def lucky_number(n):
    for numeric in range(n):
        numbers_to_string = str(numeric)
        number_two_halves = len(numbers_to_string) // 2
        if sum(map(int, list(numbers_to_string[:number_two_halves]))) \
                == sum(map(int, list(numbers_to_string[-number_two_halves:]))):
            # Условие:если сумма двух равных по длине половинок  числа равны,то возвращаем - numeric
            yield numeric


for lucky_numbers in lucky_number(10000):
    print(lucky_numbers)


# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# Вычисление палиндромных чисел
def func_palindrome(n):
    for numeric in range(n + 1):
        numbers_to_string = str(numeric)
        number_two_halves = len(numbers_to_string) // 2
        if number_two_halves >= 1 and (numbers_to_string[:number_two_halves]) == (
                numbers_to_string[-number_two_halves:][::-1]):
            # Условие:если две равные по длине половинки числа  равны,то возвращаем - numeric
            yield numeric


for number_palindrome in func_palindrome(10000):
    print(number_palindrome)


# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.

# Первый способ. Передача функция-фильтров в качестве аргументов в функцию "get_prime_numbers"
# Фильтр проверки числа на палиндром
def palindrome(n):
    numbers_to_string = str(n)
    num_len = len(numbers_to_string) // 2
    if num_len >= 1 and numbers_to_string[:num_len] == numbers_to_string[-num_len:][::-1]:
        print('***************************')
        print('Простое число-палиндром')
        return True


# Фильтр проверки числа на 'счастливое'
def lucky_number(n):
    numbers_to_string = str(n)
    len_numbers_to_string = len(numbers_to_string) // 2
    if sum(map(int, list(numbers_to_string[:len_numbers_to_string]))) \
            == sum(map(int, list(numbers_to_string[-len_numbers_to_string:]))):
        print('***************************')
        print('Простое,счастливое число')
        return True


# Генератор простых чисел
def get_prime_numbers(n, *funcs):
    for get_number in range(2, n + 1):
        for range_get_number in range(2, get_number):
            if get_number % range_get_number == 0:
                break
        else:
            # отсеивание простых чисел через функции-фильтры
            if funcs:
                for func in funcs:
                    if func(get_number):
                        yield get_number

            else:
                # если отсутствуют функции-фильтры возвращается простое число"""
                yield get_number
                print('Простое число')


for data_output in get_prime_numbers(10000, lucky_number, palindrome):
    print(data_output)


# 2 способ.Передача функций-фильтров списком в качестве аргументов в функцию "get_prime_numbers"
# Фильтр 'palindrome' для проверки числа на палиндром
def palindrome(n):
    numbers_to_string = str(n)
    num_len = len(numbers_to_string) // 2
    if num_len >= 1 and numbers_to_string[:num_len] == numbers_to_string[-num_len:][::-1]:
        print('***************************')
        print('Простое число-палиндром')
        return True


# Фильтр проверки числа на 'счастливое
def lucky_number(n):
    numbers_to_string = str(n)
    len_numbers_to_string = len(numbers_to_string) // 2
    if sum(map(int, list(numbers_to_string[:len_numbers_to_string]))) \
            == sum(map(int, list(numbers_to_string[-len_numbers_to_string:]))):
        print('***************************')
        print('Простое,счастливое число')
        return True


# Генератор простых чисел
def get_prime_numbers(n, funcs):
    for get_number in range(2, n + 1):
        for range_get_number in range(2, get_number):
            if get_number % range_get_number == 0:
                break
        else:
            # отсеивание простых чисел через функции-фильтры
            if funcs:
                for func in funcs:
                    if func(get_number):
                        yield get_number


filter_function = [lucky_number, palindrome]
for data_output in get_prime_numbers(10000, filter_function):
    print(data_output)

# Зачёт!
