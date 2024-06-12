import numpy as np
def main():
    sum= int()
    suma= int()
    cont= int()
    prom= float()

    e= np.array([16,22,18,17,26,15,23,20])

    for i in range (0, len(e), 1):
        if(e[i] >= 18) and (e[i] <=22):
            suma= suma + e[i]
            cont=(cont+1)
        else:
            sum= sum + e[i]            

    prom=(suma//cont)

    print("Los elementos del arreglo son:")
    for i in range (1,8):
        print(e[i])

    print ("La cantidad de Estudiantes en el rango (18 , 20 ) es :" , cont)
    print ("La Suma de las Edades de los Estudiantes en el rango (18 , 20 ) es:", suma)
    print("El Promedio de las edades de los Estudiantes en el rango (18, 20 ) es :", prom)
    print ("La Suma de las Edades de los Estudiantes FUERA de el rango (18 , 20 ) es :", sum)
main()