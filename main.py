from config import *
from calculations import *
from formatting import *

drop_rate = 0.01
time = 10

def main():
    attempts = format_ceil(calc_breakpoints_attempts(bp_percentages, drop_rate))
    times = format_ceil(list(map(lambda x: calc_time(x, time), attempts)))
    print(bp_percentages)
    print(attempts)
    print(times)
    format_table_attempts(bp_percentages, attempts, times)

main()




