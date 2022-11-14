### Este es el menu de opciones ###
menu = """
Bienvenido al menu
[1] Suma
[2] Producto entre "n" numero
[3] Divicion
[4] Calcula el factorial
[5] Impresion de las tablas de multiplicar
[6] Calculo del cuadrado y del cubo
[7] Promedio
[8] Maximos y Minimos
"""
print (menu)
opcion = input("Digita una opcion: ")
if opcion == "1":
    pass
elif opcion == "2":
    pass
elif opcion == "3":
    pass
elif opcion == "4":
  num = int(input("Ingresa un numero: " ))
  def factorial(num):
        if (num == 0):
            return 1
        else:
            return num * factorial(num - 1)
            print("El factorial de :" + str(num) + ": es: " +  str(factorial(num)))
            
elif opcion == "5":
    N1 = input("Primer valor: ")
    N1 = int(N1)
    for T in range(1,11):
        resultado = N1 * T
        print(N1, " x ", T, " =", resultado )
elif opcion == "6":
    num = int(input("Ingresa un numero  : "))
    if num >=1 and num<=999:
        numero = str(num)
        suma = int(numero[0]) + int (numero[1]) + int(numero[2])
        cuadrado = suma * suma
        cubo = suma * suma * suma
        print("El cuadrado es: ",cuadrado)
        print("El cubo del numero es:  ", cubo )

elif opcion == "7":

    print("Coloque valores a promediar \n")
    suma = 0
    contador = -1
    while True:
        valor = int(input())
        suma += valor
        contador += 1
        
        
        if valor == -1:
            print("END")
            break
    #print(f"suma = {suma}")
    print(f"total entradas = {contador}")
    suma = suma + 1
    promedio = suma / contador
    print ("Promedio es igual a: ", promedio)

elif opcion == "8":
    x = int(input("ingrese la cantidad de elementos: "))
    contador = 0
    lista=[]
    for i in range(x):
        contador += 1
        lista.append(int(input("Ingrese numeros: ")))
        def mayor(lista):
            max = lista[0];
            for x in lista:
                if x > max:
                    max = x
                    return max
        def menor(lista):
            min = lista[0];
            for x in lista:
                if x < min:
                    min = x
                    return min
                    print ("El número mayor es: ", max(lista))
                    print ("El número menos es: ", min(lista))
                    print(f"total entradas = {contador}")

else:
    print("Debes ingresar un numero")
