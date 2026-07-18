def ppdif(x, b):
    y = x
    digit_count = 0
    while y > 0:
        digit_count = digit_count + 1
        y = y // b
    total = 0
    while x > 0:
        total = total + pow(x % b, digit_count)
        x = x // b
    return total

def ppdif_cycle(x, b):
    seen = []
    while x not in seen:
        seen.append(x)
        x = ppdif(x, b)
    cycle = []
    while x not in cycle:
        cycle.append(x)
        x = ppdif(x, b)
    return cycle

def nar(number):
    b = 10
    x = number
    seen = []
    while x not in seen:
        seen.append(x)
        x = ppdif(x, b)
    return seen
