# Realize un algoritmo que solicite dos números enteros y los guarde en dos variables.  Luego, el programa debe intercambiar el valor
# de estas dos variables sin utilizar una tercera variable auxiliar. Por ultimo, el programa debe mostrar el contenido de las variables 
# para comprobar que el intercambio se ha realizado correctamente.




































# Solicita dos números enteros
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Intercambia los valores de las variables sin utilizar una tercera variable auxiliar
numero1, numero2 = numero2, numero1

# Muestra el contenido de las variables para comprobar el intercambio
print("El contenido de la variable numero1 es:", numero1)
print("El contenido de la variable numero2 es:", numero2)
