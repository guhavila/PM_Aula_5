import math

def calcular_c(a, b):
    c = a + b
    return c

def calcular_distancia(x1, y1, x2, y2):
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

def calcular_delta(a, b, c):
    delta = b**2 - 4*a*c
    return delta

def calcular_raizes(a, b, delta):
    if delta > 0:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        return raiz1, raiz2
    elif delta == 0:
        raiz = -b / (2*a)
        return raiz,
    else:
        return None  


a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = calcular_c(a, b)
print(f"O valor de c é: {c}")


x1 = float(input("Digite o valor de x1: "))
y1 = float(input("Digite o valor de y1: "))
x2 = float(input("Digite o valor de x2: "))
y2 = float(input("Digite o valor de y2: "))
distancia = calcular_distancia(x1, y1, x2, y2)
print(f"A distância entre os pontos é: {distancia}")

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
delta = calcular_delta(a, b, c)
print(f"Delta é igual a: {delta}")
raizes = calcular_raizes(a, b, delta)
if raizes:
    if len(raizes) == 1:
        print(f"A única raiz é: {raizes[0]}")
    else:
        print(f"As raízes são: {raizes[0]} e {raizes[1]}")
else:
    print("Não há raízes reais.")
