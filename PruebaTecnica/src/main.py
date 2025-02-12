from utils import calculate_rectangle_area, create_array, display_array_elements

def main():
    arregloOpciones = [1, 2, 5, 2, 1, 2, 9, 7, 3]
    
    for option in arregloOpciones:
        if option == 3:
            print("[Termina el programa]")
            break
        elif option == 1 or option == 2:
            lado1 = 5  # Example fixed value for lado1
            lado2 = 2  # Example fixed value for lado2
            area = calculate_rectangle_area(lado1, lado2)
            print(f"Área igual a {area}")
        elif option > 2:
            array = create_array(option)
            if array is not None:
                display_array_elements(array)
            else:
                print(f"{option} no existe la opción para este valor: {option}")

if __name__ == "__main__":
    main()