from sympy import Symbol, lambdify

# def polinomio_de_Newton(valores_x, valores_y):   #Obter bases de Newton recursivamente (não recomendável, já que calcula as mesmas coisas várias vezes e ocupa muita memória da pilha if len(valores_x) == 1:
# return valores_y[0] else: return (polinomio_de_Newton(valores_x[1:], valores_y[1:]) - polinomio_de_Newton(
# valores_x[0:len(valores_x)-1], valores_y[0:len(valores_y)-1]))/(valores_x[len(valores_x)-1] - valores_x[0])

def funcao(funcao_usuario, x='a'):
    if x == 'a':
        x = Symbol('x')
        funcao_usuario = funcao_usuario.replace('x', f'({str(x)})')
        return eval(funcao_usuario)
    funcao_usuario = funcao_usuario.replace('x', f'({str(x)})')
    return eval(funcao_usuario)

def bases_de_Newton(valores_x, valores_y, grau):
    coeficientes = []
    index_coeficientes = 0
    for i in range(1, grau):
        temp = i
        coeficientes.append([])
        aux_int = 1
        for j in range(grau-i):
            if i == 1:
                a = [(valores_y[temp] - valores_y[temp - 1]) / (valores_x[temp] - valores_x[temp - 1]),
                     (valores_x[temp]), (valores_x[temp - 1])]
                coeficientes[index_coeficientes].append(a)
                temp += 1

            else:
                a = [(coeficientes[index_coeficientes-1][aux_int][0] - coeficientes[index_coeficientes-1][aux_int-1][0])/
                     (coeficientes[index_coeficientes-1][aux_int][1] - coeficientes[index_coeficientes-1][aux_int-1][2]),
                     (coeficientes[index_coeficientes-1][aux_int][1]), (coeficientes[index_coeficientes-1][aux_int - 1][2])]
                coeficientes[index_coeficientes].append(a)
                aux_int += 1

        index_coeficientes += 1

    return coeficientes

def obter_polinomio(valores_x, valores_y, diferencas_divididas, grau):
    resultado = ''
    for i in range(grau + 1):
        if i != 0:
            resultado += ' + '
        if i == 0:
            resultado += f'{valores_y[0]}'
        else:
            resultado += f'{round(diferencas_divididas[i - 1][0][0], 7)}'
        for j in range(1, i + 1):
            resultado += f'*(x-({valores_x[j - 1]}))'
    return resultado

x = Symbol('x')
valores_x = [0, 1, 2, 3, 4, 5, 6]
valores_y = [0, 0.8, 0.9, 0.2, -0.7, -0.95, -0.2]

grau = len(valores_x) - 1
grau = 2

diferencas_divididas = bases_de_Newton(valores_x, valores_y, grau+1) # grau + 1

resultado = obter_polinomio(valores_x, valores_y, diferencas_divididas, grau)
# print(resultado)
b = funcao(resultado)
print(f'P{grau}(x) = {b}')
