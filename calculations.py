import math

def calc_chance(drop_rate, attempts):
    return 1-(1-drop_rate)**attempts

def calc_attempts(drop_rate, percentage):
    return math.log(1-percentage)/math.log(1-drop_rate)

def calc_time(attempts, time):
    return attempts * time

def calc_breakpoints_attempts(breakpoints, drop_rate):
    return list(map(lambda x: calc_attempts(drop_rate, x), breakpoints))