# ✓  Number Base Conversion Tool - Documentation

## Introduction

This Python program is a number base conversion tool that allows users to convert a number from one base to another. It supports conversions between decimal, binary, octal, and hexadecimal bases.

## How to Use

1. Run the program in your preferred Python environment.
2. The program will prompt you to enter a number and its base for conversion.
3. After converting the number to decimal, it will display the result and prompt you to continue converting the decimal number to binary, octal, and hexadecimal bases.

## Program Logic

- The program consists of several functions:

### 1. `main()`

- This is the main function that initiates the number conversion process.
- It clears the output in the IPython notebook and prompts the user to enter a number and its base.
- The user's input is then converted to decimal using the `converterPDec(num, base)` function.
- After converting to decimal, the program proceeds to convert the decimal number to binary, octal, and hexadecimal using the `converterDecPTodos(num)` function.
- Finally, it asks the user if they want to continue the program, and if the answer is "s" (SIM), it runs the `main()` function again to restart the conversion process.

### 2. `converterPDec(num, base)`

- This function converts a number from a specified base to decimal.
- It takes the number (`num`) and its base (`base`) as inputs.
- The function iterates through each digit of the number in reverse order and calculates the equivalent decimal value for each digit.
- It returns the resulting decimal number.

### 3. `converterDecPTodos(num)`

- This function converts a decimal number to binary, octal, and hexadecimal bases.
- It takes the decimal number (`num`) as input.
- The function iterates through each base (2, 8, 16) and performs the conversion.
- It displays the conversion process for each base, showing the division and remainder operations.
- Finally, it prints the converted number in the corresponding base.

### 4. `continuarPrograma()`

- This function asks the user if they want to continue using the program.
- If the user enters 's' (SIM), it calls the `main()` function again to restart the conversion process.
- If the user enters any other character, the function returns, terminating the program.

### 5. `hexNum(hex)` and `numHex(num)`

- These helper functions are used for converting hexadecimal numbers to decimal and vice versa.
- They are utilized in the `converterPDec()` and `converterDecPTodos()` functions for handling hexadecimal digits and values.

## Example Usage

```
Escreva o número para converter
Número: 1010
Escreva a base do número exemplo: decimal -> '10'
base: 2

Conversão para Decimal

0 X 2^0 = 0
1 X 2^1 = 2
0 X 2^2 = 0
1 X 2^3 = 8
Resultado = 10

Convertendo o número em decimal para a base: 2

número -> 10 / 2 | resto = 0
número -> 5 / 2 | resto = 1
número -> 2 / 2 | resto = 0
número -> 1 / 2 | resto = 1
resultado = 1010

Continuar programa? escreva s para SIM
resposta: s
Escreva o número para converter
Número: 255
Escreva a base do número exemplo: decimal -> '10'
base: 10

Conversão para Decimal

5 X 10^0 = 5
5 X 10^1 = 50
2 X 10^2 = 200
Resultado = 255

Convertendo o número em decimal para a base: 2

número -> 255 / 2 | resto = 1
número -> 127 / 2 | resto = 1
número -> 63 / 2 | resto = 1
número -> 31 / 2 | resto = 1
número -> 15 / 2 | resto = 1
número -> 7 / 2 | resto = 1
número -> 3 / 2 | resto = 1
número -> 1 / 2 | resto = 1
resultado = 11111111

Convertendo o número em decimal para a base: 8

número -> 255 / 8 | resto = 7
número -> 31 / 8 | resto = 7
número -> 3 / 8 | resto = 3
número -> 0 / 8 | resto = 3
resultado = 377

Convertendo o número em decimal para a base: 16

número -> 255 / 16 | resto = 15
número -> 15 / 16 | resto = 15
número -> 0 / 16 | resto = 15
resultado = FF

Continuar programa? escreva s para SIM
resposta: n
```

## Note

- The program demonstrates a simple base conversion tool capable of converting numbers from one base to another.
- The input validation is minimal in this implementation, and the user is expected to provide correct inputs (e.g., valid numbers and base values). Error handling for invalid inputs can be added to make the program more robust in a real-world application.
