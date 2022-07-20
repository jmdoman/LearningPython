def spd(days):
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    return seconds


total = spd(365)
print(spd(365))
