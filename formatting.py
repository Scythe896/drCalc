import math
from config import *

def format_ceil(iterable):
    return list(map(lambda x: math.ceil(x), iterable))

def empty_space(item, cell_length):
    return " " * (cell_length - len(item))

def format_line(item1, item2, item3, cell_length):
    line = "|"
    line += f"{item1}{empty_space(item1, cell_length)}|"
    line += f"{item2}{empty_space(item2, cell_length)}|"
    line += f"{item3}{empty_space(item3, cell_length)}|"
    return line

def get_max_length(list1, list2, list3):
    max_list1_length = max(list(map(lambda x: len(str(x)), list1)))
    max_list2_length = max(list(map(lambda x: len(str(x)), list2)))
    max_list3_length = max(list(map(lambda x: len(str(x)), list3)))
    return max([max_list1_length, max_list2_length, max_list3_length])

def format_table_attempts(breakpoints, attempts, times):
    cell_length = get_max_length(breakpoints, attempts, times) + 3
    ceiling = "-" * cell_length * 3 + "-" * 4
    print(ceiling)
    for i in range(0, len(breakpoints)):
        print(format_line(str(breakpoints[i]), str(attempts[i]), str(times[i]), cell_length))
        print(ceiling)
    