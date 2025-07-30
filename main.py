from config import *
from calculations import *
from formatting import *

def get_drop_rate(message):
    rate = input(message)
    if "/" in rate:
        temp = rate.split("/")
        if parts_is_float(temp) and temp[1] != "0" and temp[0] != "0":
            return float(temp[0]) / float(temp[1])
    elif "." in rate:
        temp = rate.split(".")
        if parts_is_float(temp) and temp[0] == "0" and temp[1] != "0":
            return float(rate)
    return get_drop_rate("Invalid drop rate. Please enter in format(x/y or 0.x):")

def get_time(message):
    time = input(message)
    if "." in time:
        temp = time.split(".")
        if parts_is_float(temp):
            return float(time)
    if parts_is_float(temp):
        return float(time)
    return get_time("Invalid time. Please try again:")

def parts_is_float(input):
    try:
        float(input[0])
        float(input[1])
    except ValueError:
        return False
    return True
    
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




