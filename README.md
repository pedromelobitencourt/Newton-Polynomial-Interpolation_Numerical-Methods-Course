# Newton Polynomial Interpolation

This repository contains a Python implementation of the Newton polynomial interpolation method. The code allows you to fit a polynomial to provided data points and evaluate it at specific 'x' values.

## Usage

You can use this code to perform Newton polynomial interpolation with your own data sets. Here are the basic steps:

1. **Define Your Data**: Provide the data points you want to interpolate by setting the `valores_x` and `valores_y` lists in the code.

2. **Set the Polynomial Degree**: You can specify the degree of the interpolating polynomial by setting the `grau` variable.

3. **Run the Code**: Execute the provided Python code, and it will calculate the Newton polynomial interpolant and evaluate it at a specific 'x' value.

4. **Evaluate the Interpolating Polynomial**: The `funcao()` function allows you to evaluate the interpolating polynomial at specific 'x' values. You can customize the expression for evaluation.

## Key Functions

- `funcao(funcao_usuario, x='a')`: Allows the user to define and evaluate a mathematical function in terms of 'x'. This function takes a string representing the function and a value of 'x' for evaluation.

- `bases_de_Newton(valores_x, valores_y, grau)`: Computes the Newton divided differences for the provided data up to a specified degree and stores them in a coefficient list.

- `obter_polinomio(valores_x, valores_y, diferencas_divididas, grau)`: Constructs the Newton interpolating polynomial from the calculated divided differences and the specified degree. The resulting polynomial is returned as a string.

## Example

In the provided code example, sample data is defined, and a Newton interpolating polynomial is calculated and evaluated at a specific 'x' value. You can replace these data points with your own values and adjust the degree as needed.

```python
x = Symbol('x')
valores_x = [0, 1, 2, 3, 4, 5, 6]
valores_y = [0, 0.8, 0.9, 0.2, -0.7, -0.95, -0.2]
grau = 2

diferencas_divididas = bases_de_Newton(valores_x, valores_y, grau+1)
resultado = obter_polinomio(valores_x, valores_y, diferencas_divididas, grau)
b = funcao(resultado)
print(f'P{grau}(x) = {b}')
