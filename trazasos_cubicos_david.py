import numpy as np
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4,5,6]
y = [3,5,6,5,-2,2,13]

n = len(x)
        
listaCoeficientes = []
for i in range(n):
  listaCoefRes = []
  denominador = 1
  for j in range(n):
    if i != j:
      listaCoefJ = []
      if j == 0 or (i == 0 and j == 1):
        listaCoefRes.append(-x[j])
        listaCoefRes.append(1)
      else:
        listaCoefI = listaCoefRes
        listaCoefJ.append(-x[j])
        listaCoefJ.append(1)
        listaCoefRes = []
        for k in range(len(listaCoefI)):
          valAux0 = listaCoefI[k] * listaCoefJ[0]
          valAux1 = listaCoefI[k] * listaCoefJ[1]

          if len(listaCoefRes) <= k:
            listaCoefRes.append(0)
          listaCoefRes[k] += valAux0

          if len(listaCoefRes) <= k + 1:
            listaCoefRes.append(0)
          listaCoefRes[k + 1] += valAux1
          
      denominador *= x[i] - x[j]
    
  for k in range(len(listaCoefRes)):
    listaCoefRes[k] *= (y[i] / denominador)

    if len(listaCoeficientes) <= k:
      listaCoeficientes.append(0)
    listaCoeficientes[k] += listaCoefRes[k]
    
print("f(x) = ", end="")
for i in range(len(listaCoeficientes) - 1, -1, -1):
  if i < len(listaCoeficientes) - 1:
    print(" + ", end="")
  print(listaCoeficientes[i], end="")

  if i > 0:
    print("x", end="")
    if i > 1:
      print("^" + str(i), end="")
print()

def evaluar_polinomio(x_val):
    resultado = 0
    for i in range(len(listaCoeficientes) - 1, -1, -1):
        resultado = resultado * x_val + listaCoeficientes[i]
    return resultado

# Estimar el valor para x = 3.25
x_estimado = 3.25
y_estimado = evaluar_polinomio(x_estimado)
print(f"El valor estimado en x = {x_estimado} es: {y_estimado}")

# Graficar el polinomio y los puntos de datos
x_grafica = np.linspace(min(x), max(x), 100)
y_grafica = [evaluar_polinomio(xi) for xi in x_grafica]

plt.plot(x_grafica, y_grafica, label='Polinomio de Lagrange', color='blue')
plt.scatter(x, y, color='red', zorder=5, label='Puntos de Datos')
plt.plot(x_estimado, y_estimado, 'go', label=f'Estimación en x={x_estimado}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación de Lagrange')
plt.legend()
plt.grid(True)
plt.show()