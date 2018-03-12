# evaluate Lib

def parse_integer(s):
    i = int(s)
    return i

def parse_float(s):
    f = float(s)
    return f

def evaluate_height(s):
    try:
        h = parse_float(s)
        return 100 <= h <= 300
    except ValueError:
        return False

def evaluate_phone(s):
    try:
        if(len(str(s)) == 10):
            ph = parse_integer(s)
            return ph
        else:
            return False
    except ValueError:
        return False

def evaluate_latitude(s):
    try:
        latitude = parse_float(s)
        return -90 <= latitude <= 90
    except ValueError:
        return False

def evaluate_longitude(s):
    try:
        longitude = parse_float(s)
        return -180 <= longitude <= 180
    except ValueError:
        return False