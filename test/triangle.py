def validate_sides(a, b, c):   
    return a + b > c and a + c > b and b + c > a


def validate_angles(a, b, c):
    return a + b + c == 180
    