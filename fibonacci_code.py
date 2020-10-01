##Algoritmo recursivo

def fibonacci_recursivo(k):
  if(k == 0 or k == 1):
    return k;
  else:
    return fibonacci_recursivo(k-1) + fibonacci_recursivo(k-2)

print(fibonacci_recursivo(40))

##Algoritmo Fast doubling - https://www.nayuki.io/page/fast-fibonacci-algorithms
def fibonacci(n):
	if n < 0:
		raise ValueError("Negative arguments not implemented")
	return _fib(n)[0]

# (Private) Devuelve la tupla (F(n), F(n+1)).
def _fib(n):
	if n == 0:
		return (0, 1)
	else:
		a, b = _fib(n // 2)
		c = a * (b * 2 - a)
		d = a * a + b * b
		if n % 2 == 0:
			return (c, d)
		else:
			return (d, c + d)

print(fibonacci(40))

## Generar listas con los tiempos de ejecución para el rango n=(0,30)
import time
lista_recursiva=[]
lista_fast=[]
x_val=range(2,30)
for i in x_val:
  start_time=time.time()
  x=i
  f=fibonacci_recursivo(x)
  y=(time.time() - start_time)
  lista_recursiva.append(y)

for i in x_val:
  start_time=time.time()
  x=i
  f=fibonacci(x)
  y=(time.time() - start_time)
  lista_fast.append(y)
  
 ## Generar la gráfica a partir de las listas creadas
 
import matplotlib.pyplot as plt
x_labels = x_val
plt.plot(lista_fast,color='green',label="fast")
plt.plot(lista_recursiva,color='blue',label="recursivo")
plt.title("Tiempo de ejecución(s)")
plt.xlabel("n")
plt.legend()
plt.show()

## Generar gráfica para los primeros 5 valores de la serie
x_labels = x_val
plt.plot(lista_fast[0:6],color='green',label="fast")
plt.plot(lista_recursiva[0:6],color='blue',label="recursivo")
plt.title("Tiempo de ejecución(s)")
plt.xlabel("n")
plt.legend()
plt.show()
