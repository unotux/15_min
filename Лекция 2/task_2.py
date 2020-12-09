"""Есть список джобов, необходимо несколькими способами избавиться от дублей. Нужно написать как минимум 2 версии
скрипта. Названия джобов в списке. """

import pprint
from collections import defaultdict

pp = pprint.PrettyPrinter(indent=2)

job_list = ['ODD 1 LOAD EXAMPLE', 'DATAVAULT 1 LOAD EXAMPLE', 'DDS 1 LOAD EXAMPLE', 'ODD LOAD ANSWERS',
            'DDS LOAD ANSWERS',
            'USERMART LOAD ANSWERS', 'DATAVAULT 1 LOAD EXAMPLE', 'USERMART LOAD ANSWERS']


def count_doubles(list: list) -> list:
    """Подсчёт дублей для каждого элемента"""
    deduplicate_list = defaultdict(int)
    for i in list:
        deduplicate_list[i] += 1
    print("---------------------До дедубликации----------------")
    pp.pprint(list)
    print("---------------------После дедубликации----------------")
    pp.pprint(deduplicate_list)


def delete_doubles(input_list: list) -> list:
    """Удаление дублей через приведение списка к множеству"""
    print("---------------------До дедубликации----------------")
    pp.pprint(input_list)
    print("---------------------После дедубликации----------------")
    pp.pprint(list(set(input_list)))


delete_doubles(job_list)
count_doubles(job_list)
