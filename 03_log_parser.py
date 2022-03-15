# -*- coding: utf-8 -*-
from pathlib import Path


# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

def log_parser():
    temporary_variable = 'Log Parser'
    count = ''
    my_path = str(Path("events.txt"))
    with open(my_path, 'r', encoding='utf8') as f:
        result = (date[1:17] for date in f if 'NOK' in date)
        for group_time in result:
            if group_time == temporary_variable:
                count += 1

            else:
                yield temporary_variable, count
                temporary_variable = group_time
                count = 1
        else:
            yield temporary_variable, count


def main():
    parser = log_parser()
    for group_time, event_count in parser:
        print(f'[{group_time}] {event_count}')


if __name__ == "__main__":
    main()

# Зачёт!
