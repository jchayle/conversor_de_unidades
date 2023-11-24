#Autor:ricardo chayle
#Fecha:22/11/2023
#Descripcion: Este Modulo sirve para convertri tiempo
def segundo_minuto(tiempo):
    return(tiempo /60)

if __name__ == "__main__":
    segundo=float(input("ingrese el tiempo a convertir"))
    print(segundo_minuto(segundo))