# Technical Test Solution

## Task Description

This program processes an array of options sequentially, performing specific tasks based on the given values:

1. **Rectangle Area Calculation (Option 1)**

   - The program takes two values from the list as the sides of a rectangle.
   - Computes the area by multiplying `side1` and `side2`.
   - Displays the result in the format: `Área igual a <resultado>`.

2. **Create a One-Dimensional Array (Option 2)**

   - Reads an integer `n` from the list.
   - Validates that `n > 0`. Otherwise, prints `"Tamaño para dimensionar arreglo inválido"`.
   - Creates an array containing numbers from `n` to `1`.
   - Displays only the second half of the array.

3. **Exit the Program (Option 3)**
   - When encountering option **3**, the program terminates.

## Example Execution

For the input:

```python
optionsArray = [1, 2, 5, 2, 1, 2, 9, 7, 3]
```

The expected flow with the above array is:

Área igual a 10
Arreglo de 1 posición creado: 1
Arreglo de 9 posiciones creado: 5 4 3 2 1
7 no existe la opción para este valor: 7
[Termina el programa]

### Program Logic

#### Sequential Processing of the Options Array:

The program reads the optionsArray sequentially:

- Option 1: Takes the next two values as side1 and side2 to calculate the area.
- Option 2: Takes the next value as n and creates an array accordingly.
- Option 3: Terminates execution.

#### Implementation of Option 1 (Rectangle Area):

- Extract side1 and side2 from the sequence.
- Calculate the area by multiplying these two values.
- Print the result in the format: `Area equals <result>`.

#### Implementation of Option 2 (Create One-Dimensional Array):

- Extract the value n and validate that it is greater than 0.
- If n is valid, create an array with numbers from n to 1.
- Determine the middle index (using integer division) and display the elements of the array from that index to the end.
- If n is 0 or negative, display the message: `Invalid size for array dimension`.

#### Implementation of Option 3 (Exit):

- Print `[Ends the program]` and terminate the execution.

#### Invalid Option:

- If a value other than 1, 2, or 3 is encountered, print a message indicating that the option does not exist, for example: `<value> no option exists for this value: <value>`.

### Project Structure

The project consists of a single file:

- **main.py:**  
  Contains the main program flow that processes the options array and consumes the parameters according to the selected option.

### How to Use the Program

#### Requirements

- Python 3.x installed on the system.
