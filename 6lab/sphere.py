import math

def calculate_volume(r):
    """Вычисляет объём шара"""
    return (4/3) * math.pi * r**3

def calculate_surface_area(r):
    """Вычисляет площадь поверхности шара"""
    return 4 * math.pi * r**2

def get_parameters():
    """Возвращает список параметров для GUI"""
    return ["Радиус (r)"]