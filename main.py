from config import *
from calculations import *
from formatting import *

def get_drop_rate(message):
    rate = input(message)
    if "/" in rate:
        parts = rate.split("/")
        try:
            parts1 = float(parts[0])
            parts2 = float(parts[1])
        except ValueError:
            return get_drop_rate("Invalid drop rate. Please enter in format(x/y or 0.x):")
        try:
            res = parts1 / parts2
        except ZeroDivisionError:
            return get_drop_rate("Invalid drop rate. Please enter in format(x/y or 0.x):")
    else:
        try:
            res = float(rate)
        except ValueError:
            return get_drop_rate("Invalid drop rate. Please enter in format(x/y or 0.x):")
    if res > 0 and res < 1:
        return res
    return get_drop_rate("Invalid drop rate. Please enter in format(x/y or 0.x):")

def get_time(message):
    time = input(message)
    try:
        res = float(time)
    except ValueError:
        return get_time("Invalid time. Please try again:")
    if res > 0:
        return res
    return get_time("Invalid time. Please try again:")
    
def main():
    drop_rate = get_drop_rate("Enter drop rate(x/y, 0.x):")
    time = get_time("Enter time(s):")

    #Create then format data array with percentages, kills, time(s)
    data = [PERCENTAGES]
    data.append(format_ceil(calc_percentages_attempts(PERCENTAGES, drop_rate)))
    data.append(format_ceil(list(map(lambda x: calc_time(x, time), data[1]))))
    format_data(data)

    #Creates and prints table
    format_table_attempts(data)

main()




