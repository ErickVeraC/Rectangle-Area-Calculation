def calculate_rectangle_area(lado1, lado2):
    return lado1 * lado2

def create_array(n):
    if n <= 0:
        raise ValueError("Tamaño para dimensionar arreglo inválido")
    return list(range(n, 0, -1))

def display_array_elements(array):
    midpoint = len(array) // 2
    return array[midpoint:]