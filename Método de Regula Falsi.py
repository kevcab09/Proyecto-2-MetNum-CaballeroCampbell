#Método de Regula Falsi

#Libreria
import matplotlib.pyplot as plt

# Declaramos la función
def f(x):
        return x**3 -5*x -9
      
# Bloque de instrucciónes Regula-Falsi
def falsePosition(x0,x1,e):
    step = 1
    condition = True
    while condition:
        x2 = x0 - (x1-x0) * f(x0)/( f(x1) - f(x0) )
        print('Iteración-%d, x2 = %0.6f y f(x2) = %0.6f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        step = step + 1
        condition = abs(f(x2)) > e

    print('\nLa raiz requerida es: %0.8f' % x2)
#Grafica
x = range (0,15)
plt.plot(x, [f(i) for i in x])
plt.title("Gráfica de la ecuación")
plt.show()

# Captura de datos
x0 = float(input('Primer límite: '))
x1 = float(input('Segundo límite : '))
e = float(input('Indique el error: '))

# Verificación de la validez de los datos introducidos
if f(x0) * f(x1) > 0.0:
    print('Los limites indicados no encierran la raiz')
    print('Intente con otros limites')
else:
    falsePosition(x0,x1,e)

print('\n Parcial N°2 \n Metodo Regula-Falsi y Newton Raphson \n Carlos "La pistola" Campbell y Kevin "El bombardero" Caballero')