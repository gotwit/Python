def format24Hr(time: str) -> str:
    if time[-2:] == "AM" and time[:2] == "12":
        return "00" + time[2:-2]
    elif time[-2:] == "AM":
        return time[:-2]
    elif time[-2:] == "PM" and time[:2] == "12":
        return time[:-3]
    elif time[-2:] == "PM":
        return str(int(time[:2]) + 12) + time[2:-3]


print(format24Hr("06:33:00 PM"))

print(format24Hr("08:43:00 AM"))

print(format24Hr("11:00:00 AM"))

print(format24Hr("11:15:00 PM"))

print(format24Hr("12:00:00 AM"))

print(format24Hr("12:15:00 PM"))
