from config import *
from calculations import *
from formatting import *

drop_rate = 1/350
time = 20

def main():
    #Create then format data array with percentages, kills, time(s)
    data = [PERCENTAGES]
    data.append(format_ceil(calc_percentages_attempts(PERCENTAGES, drop_rate)))
    data.append(format_ceil(list(map(lambda x: calc_time(x, time), data[1]))))
    format_data(data)

    print(data[0])
    print(data[1])
    print(data[2])
    format_table_attempts(data)

main()




