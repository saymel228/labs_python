def calculate_volume(a, b, c):
    """Вычисляет объём параллелепипеда"""
    return a * b * c

def calculate_surface_area(a, b, c):
    """Вычисляет площадь поверхности параллелепипеда"""
    return 2 * (a*b + a*c + b*c)

def get_parameters():
    """Возвращает список параметров для GUI"""
    return ["Длина (a)", "Ширина (b)", "Высота (c)"]