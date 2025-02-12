def main():
    opciones = [1, 2, 5, 2, 1, 2, 9, 7, 3]
    i = 0  

    while i < len(opciones):
        opcion = opciones[i]
        i += 1

        if opcion == 3:
            print("[Termina el programa]")
            break

        elif opcion == 1:
            if i + 1 < len(opciones):
                lado1, lado2 = opciones[i], opciones[i + 1]
                i += 2 
                
                if lado1 > 0 and lado2 > 0:
                    print(f"Área igual a {lado1 * lado2}")
                else:
                    print("Valores inválidos para el cálculo del área.")
            else:
                print("No se proporcionaron suficientes valores para calcular el área.")
                break

        elif opcion == 2:
            if i < len(opciones):
                n = opciones[i]
                i += 1 

                if n <= 0:
                    print("Tamaño para dimensionar arreglo inválido")
                else:
                    arreglo = list(range(n, 0, -1))
                    mitad = len(arreglo) // 2
                    print(f"Arreglo de {n} posiciones creado:", " ".join(map(str, arreglo[mitad:])))
            else:
                print("No se proporcionó el tamaño para dimensionar el arreglo.")
                break

        else:
            print(f"{opcion} no existe la opción para este valor: {opcion}")

if __name__ == "__main__":
    main()
