"""Реализуйте словарь rus_eng другими способами:

1. при помощи defaultdict

2. при помощи оератора [], а не функции update(): my_dict[key] = value"""

from collections import defaultdict


def first_way() -> dict:
    english_to_russian = defaultdict(list)
    english_to_russian['mother'].append('Мама')
    english_to_russian['father'].append('Папа')
    english_to_russian['family'].append('Семья')
    english_to_russian['Ключ без значения']
    print(f"Первый вариант\n{english_to_russian}")
    return english_to_russian


def second_way() -> dict:
    english_to_russian = {}
    english_to_russian['mother'] = 'Мама'
    english_to_russian['father'] = 'Папа'
    english_to_russian['family'] = 'Семья'
    print(f"\n\nВторой вариант\n{english_to_russian}")
    return english_to_russian


first_way()
second_way()


