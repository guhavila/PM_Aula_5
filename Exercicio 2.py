import math
import numpy as np
import scipy.optimize as opt

def calcular_posicao(angulo1, angulo2, comprimento1, comprimento2):
    x = comprimento1 * math.cos(angulo1) + comprimento2 * math.cos(angulo1 + angulo2)
    y = comprimento1 * math.sin(angulo1) + comprimento2 * math.sin(angulo1 + angulo2)
    return x, y

def calcular_angulos(posicao_x, posicao_y, comprimento1, comprimento2):
    def objetivo(angulos):
        x_calculado, y_calculado = calcular_posicao(angulos[0], angulos[1], comprimento1, comprimento2)
        return (posicao_x - x_calculado)**2 + (posicao_y - y_calculado)**2
    
    angulos_iniciais = [0, 0]  
    resultado = opt.minimize(objetivo, angulos_iniciais, method='SLSQP')
    return resultado.x[0], resultado.x[1]

def gerar_variacao_de_angulos(angulos_iniciais, angulos_finais, num_pontos=100):
    angulos_variados = []
    for i in range(num_pontos):
        angulo1 = np.interp(i, [0, num_pontos - 1], [angulos_iniciais[0], angulos_finais[0]])
        angulo2 = np.interp(i, [0, num_pontos - 1], [angulos_iniciais[1], angulos_finais[1]])
        angulos_variados.append((angulo1, angulo2))
    return angulos_variados

angulo1 = math.radians(30)  
angulo2 = math.radians(45)
comprimento1 = 2.0
comprimento2 = 1.5
posicao = calcular_posicao(angulo1, angulo2, comprimento1, comprimento2)
print(f"A posição de A é: {posicao}")

posicao_x = 2.5
posicao_y = 1.5
angulos_calculados = calcular_angulos(posicao_x, posicao_y, comprimento1, comprimento2)
print(f"Os ângulos correspondentes são: {math.degrees(angulos_calculados[0])} graus, {math.degrees(angulos_calculados[1])} graus")

angulos_iniciais = [math.radians(30), math.radians(45)]
angulos_finais = [math.radians(60), math.radians(60)]
variacao_de_angulos = gerar_variacao_de_angulos(angulos_iniciais, angulos_finais)
print("Variação de ângulos:")
for angulo in variacao_de_angulos:
    print(f"Angulo1: {math.degrees(angulo[0])} graus, Angulo2: {math.degrees(angulo[1])} graus")
