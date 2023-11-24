#Autor:ricardo chayle
#Fecha:22/11/2023
#Descripcion: Este Modulo sirve para convertir peso
def gramos_kilogramos (peso):
    return (peso *1000)

if __name__ == "__main__":
    gramos=float(input("ingrese peso a convertir \n"))
    print(gramos_kilogramos(gramos))