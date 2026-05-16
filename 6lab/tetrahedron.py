import math

def calculate_volume(a):
    """Вычисляет объём правильного тетраэдра"""
    return (a**3) * math.sqrt(2) / 12

def calculate_surface_area(a):
    """Вычисляет площадь поверхности правильного тетраэдра"""
    return math.sqrt(3) * a**2

def get_parameters():
    """Возвращает список параметров для GUI"""
    return ["Длина ребра (a)"]