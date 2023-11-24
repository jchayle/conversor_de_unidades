#Autor:ricardo chayle 
#Fecha:24/11/2023
#Descripcion: Este Modulo es el menu de conversion de unidades

import Temperatura as temp 
import masa as mas
import tiempo as timp
import temperatura as temp
def main():
    while True:
        opcion = input("Bienvenido, que unidades desea convertir?: \n" 
                "0. Salir del programa\n"
                "1. Celsius a Farenheit\n"
                "2. Kilogramos a gramos\n"
                "3. segundo a minuto\n")
        try:
            opcion = int(opcion)
            if opcion == 0:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            elif opcion == 1:
                celsius= float(input("Ingrese los grados a convertir \n"))
                print(temp.celsius_fahrenheit(celsius))
            elif opcion == 2:
                gramos=float(input("ingrese peso a convertir \n"))
                print(mas.gramos_kilogramos(gramos))
            elif opcion == 3:
                segundo=float(input("ingrese el tiempo a convertir"))
                print(timp.segundo_minuto(segundo))
        
        except ValueError:
            print("Solo puede ingresar valores numéricos.")

main()