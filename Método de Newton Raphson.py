#Método de Newton Raphson

#librerías
import matplotlib.pyplot as plt
import numpy as np

#Función para ingresar la ecuacion
def fx(x, t1, t2, t3, c1, c2, c3):
    return t1* x ** c1 + t2 * x **c2 + t3 * x ** c3

#Funcion para ingresar la derivada
def dfx(x, et1, et2, et3, ec1, ec2, ec3):
    return et1* x ** ec1 + et2 * x **ec2 + et3 * x ** ec3

#Programa principal
#Ingresar los valores
print("Ingrese los terminos solicitados")
print("Para el término independiente escriba 0 en el exponente")
t1 = float (input ("Primer coeficiente de la funcion: "))
t2 = float (input ("Segundo coeficiente de la funcion: "))
t3 = float (input ("Tercer coeficiente de la funcion: "))
c1 = float (input ("Primer exponente de la funcion: "))
c2 = float (input ("Segundo exponente de la funcion: "))
c3 = float (input ("Tercer exponente de la funcion: "))

et1 = float (input ("Primer coeficiente de la funcion derivada: "))
et2 = float (input ("Segundo coeficiente de la funcion derivada: "))
et3 = float (input ("Tercer coeficiente de la funcion derivada: "))
ec1 = float (input ("Primer exponente de la funcion derivada: "))
ec2 = float (input ("Segundo exponente de la funcion derivada: "))
ec3 = float (input ("Tercer exponente de la funcion derivada: "))

#Grafica inicial
x = np.linspace(-25,25,150)
plt.plot(x,fx(x, t1, t2, t3, c1, c2, c3))
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
#Iteraciones 
print("Ingrese el limite de iteraciones:")
limite = int(input())

#Encabezado
print("{:^5} {:^15} {:^15} {:^15} {:^15} {:^15} ".format("Iteracion", "x0", "xsolucion", "Error", "f(x0)", "f'(x0)"))

#Ciclo para las iteraciones
for k in range(limite):
    x1=xi-fx(xi, t1, t2, t3, c1, c2, c3)/dfx(xi, et1, et2, et3, ec1, ec2, ec3)
    error=abs((x1-xi)/x1)
    print("{:^4d} {:^20.6f} {:^15.6f} {:^15.6f} {:^15.6f} {:^15.6f}".format(k, xi, x1, error, fx(xi, t1, t2, t3, c1, c2, c3), dfx(xi, et1, et2, et3, ec1, ec2, ec3)))
    if error<err_q:
        break
    xi=x1
    
#Grafica final
x = np.linspace(-20,20,100)
plt.plot(x, fx(x, t1, t2, t3, c1, c2, c3))
plt.plot(xi, fx(xi, t1, t2, t3, c1, c2, c3), 'or')
plt.axhline(0, color="green")
plt.axvline(0, color="green")
plt.ylim(-25, 25)
plt.grid()
plt.show()
  
print("\n\nFin del método de Newton Raphson con xsol =", round(x1,4))
print('\n Parcial N°2 \n Metodo Regula-Falsi y Newton Raphson \n Carlos "La pistola" Campbell y Kevin "El bombardero" Caballero')