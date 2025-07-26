from config import *
from calculations import *
from formatting import *

drop_rate = 1/350
time = 20

def main():
    data = [bp_percentages]
    data.append(format_ceil(calc_breakpoints_attempts(bp_percentages, drop_rate)))
    data.append(format_ceil(list(map(lambda x: calc_time(x, time), data[1]))))
    print(data[0])
    print(data[1])
    print(data[2])
    format_table_attempts(bp_percentages, data[1], data[2])

main()




