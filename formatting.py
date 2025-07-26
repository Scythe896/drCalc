import math
from config import *

def format_ceil(iterable):
    return list(map(lambda x: math.ceil(x), iterable))

def format_time(time):
    hours = 0
    minutes = 0
    seconds = time
    while seconds >= 60:
        seconds -= 60
        minutes += 1
    while minutes >= 60:
        minutes -= 60
        hours += 1
    res = ""
    if hours > 0:
        res += f"{hours}h "
    if minutes > 0:
        res += f"{minutes}m "
    res += f"{seconds}s"
    return res

def format_line(percentage, kills, time, cell_length):
    percentage = f"{percentage*100}%"
    time = format_time(time)
    line = "|"
    line += f"{percentage:<{cell_length}}|"
    line += f"{kills:<{cell_length}}|"
    line += f"{time:<{cell_length}}|"
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
        print(format_line(breakpoints[i], attempts[i], times[i], cell_length))
    print(ceiling)
    