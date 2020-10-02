## Cómo importar el top 250 de películas de IMDb. https://www.geeksforgeeks.org/python-imdbpy-getting-top-250-movies/
import imdb 
import random
# Creación instancia
ia = imdb.IMDb() 
# Obtener top 250 de películas
top_250 = ia.get_top250_movies() 

# Seleccionar el nombre de una película aleatoria
def obtener_nombre_pelicula():
  palabra=str(random.choice(top_250))
  palabra= palabra.replace(".","")
  palabra= palabra.replace(":","")
  return palabra.upper()

# List de figuras para el ahorcado
figuras_ahorcado = [
'''
+---+
|
|
|
===
''',
'''
+---+
|   O 
|
|
===
''', 
'''
+---+
|   O 
|   |
|
===
''',
'''
+---+
|   O 
|  /|
|
===
''', 
'''
+---+
|   O 
|  /|\\
|
===
''', 
'''
+---+
|   O 
|  /|\\
|  / 
===
''', 
'''
+---+
|   O 
|  /|\\
|  / \\
===
'''
]

def convertir_frase_barras(frase):
  lista_aux=[]
  for i in frase:
    if i == " ":
      lista_aux.append(i)
    else:
      lista_aux.append("_")
  return lista_aux

def lista_barras_a_texto(lista):
  barras=""
  for j in lista:
    barras += j 
  return barras

def jugar(pelicula):

  barras_lista = convertir_frase_barras(pelicula)
  barras_juego = lista_barras_a_texto(barras_lista)
  lim_intentos = len(figuras_ahorcado)
  print("Vamos a jugar al ahorcado con películas en inglés!")
  print("Puedes ingresar tanto una letra como una palabra y tendrás como máximo {} intentos para adivinar la película".format(lim_intentos))
  print(barras_juego)
  print("\n")
  intento_usuario=0
  lista_ingresado=[]

  while True:
    
    intento=input("Ingresa letra o palabra: ").upper()
    acumula_while=0

    while intento in lista_ingresado:
      print("Ya ingresaste ese valor previamente")
      intento=input("Ingresa letra o palabra: ").upper()
  
    ##Si la palabra ingresada es más grande que la frase, solicita nuevamente los datos
    bandera_1=False
    while (len(intento)> len(pelicula)):
      print("Palabra es más grande que la frase, dato inválido")
      acumula_while += 1
      if acumula_while > 5:
        bandera_1=True
        break
      intento=input("Ingresa letra o palabra: ").upper()

    ##Si la palabra no es alfanúmerica solicita nuevamente los datos
    bandera_2=False
    while not intento.isalnum():
      print("Palabra es más grande que la frase, dato inválido")
      acumula_while += 1
      if acumula_while > 5:
        print("Demasiados datos erróneos")
        bandera_2=True
        break
      intento=input("Ingresa letra o palabra: ").upper()
    ##Si se acumulan más de 5 ingresos erróneos se cierra el programa
    if bandera_1 == True or bandera_2 == True:
      print("Se cierra el programa")
      break

    if len(intento) == 1:
      if intento not in pelicula:
        intento_usuario += 1
        print("La letra no pertenece a la frase")
      else:
        print("La letra pertenece a la frase")
        contar=0
        for k in pelicula:
          if intento == k:
            barras_lista[contar] = intento
          contar +=1

    elif len(intento) > 1:
      if intento not in pelicula:
        intento_usuario += 1
        print("La palabra no pertenece a la frase")
      else:
        print("La palabra pertenece a la frase")
        inicio = pelicula.find(intento)
        for i in range(inicio,len(barras_lista)):
          if barras_lista[i] == " ":
            break
          else:
            barras_lista[i] = pelicula[i]

    ##Si los intentos que tiene el usuario superan el límite el programa se acaba
    if intento_usuario > lim_intentos:
      print("\nHas perdido, la película era: {}". format(pelicula))
      break

    ##Compara el texto impreso por la lista con los datos que han sido adivinados con el nombre de la película, si coinciden, detiene el ciclo y muestra texto de felicitaciones
    barras_juego = lista_barras_a_texto(barras_lista)
    if barras_juego == pelicula:
      print("\nFelicitaciones, adivinaste la película {}".format(pelicula))
      break

    lista_ingresado.append(intento)

    print ("Intentos restantes {}".format(lim_intentos-intento_usuario))
    for i in barras_lista:
      print(i,end="")
    print("\n")

    if intento_usuario > 0:
      print(figuras_ahorcado[intento_usuario-1])
      print("\n"*2)
      
def main():
  while(True):
    nombre_pelicula = obtener_nombre_pelicula()
    jugar(nombre_pelicula)
    pregunta=input("Quiere jugar de nuevo (S/N):").upper()
    if pregunta != "S":
      break

if __name__ == "__main__":
    main()
