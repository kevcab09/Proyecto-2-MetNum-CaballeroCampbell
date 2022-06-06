#Método de Newton Raphson

#librerías
import matplotlib.pyplot as plt
import numpy as np

#Función que calcula el valor de la expresion
def fx(x):
    f = x**3 - 2*x -5
    return f

#Función que calcula el valor de la derivada
def Dfx(x):
    deriv_f = 3*x**2 - 2 
    if deriv_f == 0:
        print("Cuidado: La derivada de la funcion es igual a: 0")
        exit()
    return deriv_f

#Programa principal

x = np.linspace(-25,25,150)
plt.plot(x, fx(x))
plt.axhline(0, color = "green")
plt.axvline(0, color = "green")
plt.ylim(-25, 25)
plt.title("Gráfica de la ecuación")
plt.grid()
plt.show()

#Valor inicial
print("Valor inicial:")
xi = float(input())

#Error que queremos
print("Ingrese el error tolerado:")
err_q = float(input())

#Error relativo porcentual
err_r = 100.0

#Primera iteración
#Llama  a la función que calcula el valor de f(x)
fxi = fx(xi)

#Llama a la función que calcula el valor de la derivada de f(x)
Dfxi = Dfx(xi)

#Calcula el siguiente estimado de la solución
xsol = xi - fxi / Dfxi

#Operaciones
#Contador de iteraciones
niter = 1
#Impresión en pantalla
print("{:^5} {:^15} {:^15} {:^15} {:^15} {:^15} ".format("Iter", "xi", "f(xi)", "f'(xi)", "xsol", "err_r"))
print("{:^4d} {:^15.4f} {:^15.4f} {:^15.4f} {:^15.6f} {:^15.4f}".format(niter, xi, fxi, Dfxi, xsol, err_r))
#Ciclo while hasta obtener una solución con el error menor al error pedido
while(err_r >= err_q):
#Respalda el valor actual de la solución
    xi = xsol
#Llama  a la función que calcula el valor de f(x)
    fxi = fx(xi)
#Llama a la función que calcula el valor de la derivada de f(x)
    Dfxi = Dfx(xi)
#Calcula el siguiente estimado de la solución
    xsol = xi - fxi / Dfxi

#Número de iteraciones
    niter = niter + 1
#Calcular el error relativo porcentual
    err_r = abs((xsol - xi) / xsol) * 100

#Variables de las iteraciones
    print("{:^4d} {:^15.4f} {:^15.4f} {:^15.4f} {:^15.6f} {:^15.4f}".format(niter, xi, fxi, Dfxi, xsol, err_r))

print("\n\nFin del método de Newton Raphson con xsol =", round(xsol,4))

print('\n Parcial N°2 \n Metodo Regula-Falsi y Newton Raphson \n Carlos "La pistola" Campbell y Kevin "El bombardero" Caballero')