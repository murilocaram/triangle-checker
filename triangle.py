def validate_sides(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    return a + b > c and a + c > b and b + c > a

def validate_angles(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    return a + b + c == 180

def classify_by_sides(a, b, c):
    if a == b == c:
        return 'Triângulo Equilátero'
    elif a == b or b == c or a == c:
        return 'Triângulo Isósceles'
    else:
        return 'Triângulo Escaleno'

def classify_by_angles(a, b, c):
    angles = sorted([a, b, c])
    if angles[2] == 90:
        return 'Triângulo Retângulo'
    elif angles[2] < 90:
        return 'Triângulo Acutângulo'
    else:
        return 'Triângulo Obtusângulo'