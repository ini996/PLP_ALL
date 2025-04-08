def largePower (base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False


def div10 (num):
    result = num%10
    if result == 0:
        return True
    else:
        return False
    
