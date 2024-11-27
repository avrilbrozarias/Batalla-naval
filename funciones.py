import pygame
import random
from config import *

pygame.init()

def inicializar_tablero(dificultad:int)->list:
    '''
    Inicializa una matriz vacia y la retorna.
    '''
    matriz = []
    for _ in range(dificultad):
        fila = [0] * dificultad
        matriz += [fila] 

    return matriz

def mostrar_matriz(matriz:list)->None:
    '''
    Recibe una matriz, la recorre y la muestra.
    No retorna nada
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j],  end=" ")
        print("")

# def dibujar_matriz(dificultad:int, ventana, espaciado:int): #Arreglar
#     pos_inicio = 200
#     pos_y = 55
#     for _ in range(dificultad + 1):
#         pygame.draw.line(ventana, BLANCO, (pos_inicio, 55), (pos_inicio, 555))
#         pos_inicio += espaciado
#     for _ in range(dificultad + 1):
#         pygame.draw.line(ventana, BLANCO, (200, pos_y), (700, pos_y))
#         pos_y += espaciado

def colocar_navio(matriz:list, tipo_navio:str, cantidad:int):
    """
    Recibe una matriz, un tipo de navio (submarino, destructor, crucero o acorazado)
    y la cantidad de navios que se quiere colocar.
    """

    match tipo_navio:
        case "submarino":
            largo = 1
        case "destructor":
            largo = 2
        case "crucero":
            largo = 3
        case "acorazado":
            largo = 4

    contador_colocados = 0

    while contador_colocados < cantidad:

        fila_inicial = random.randint(0, len(matriz) - (largo))
        columna_inicial = random.randint(0, len(matriz[0]) - (largo))
        orientacion = random.choice(["H", "V"])

        if validar_casilleros(matriz, fila_inicial, columna_inicial, largo, orientacion) == True:
            contador_colocados += 1
            for _ in range(largo):

                matriz[fila_inicial][columna_inicial] = largo

                if orientacion == "H":
                    columna_inicial += 1
                else:
                    fila_inicial += 1
    
def validar_casilleros(matriz:list,fila:int, columna:int, largo:int, orientacion:str):
    """
    recibe una matriz, una fila, una columna, el largo del objeto que se quiere colocar
    y la orientacion del objeto (H o V)
    verifica que todos los espacios necesarios sean del valor 0 y devuelve true.
    si algun casillero es distinto a 0 devuelve false.
    """
    bandera_vacio = True
    contador = 0
    if orientacion == "H" and (columna + largo) < len(matriz[0]):
        while contador < largo:
            if matriz[fila][columna] != 0:
                bandera_vacio = False
                break

            columna += 1
            contador += 1

    if orientacion == "V" and (fila + largo) < len(matriz):
        while contador < largo:
            if matriz[fila][columna] != 0:
                bandera_vacio = False
                break

            fila += 1
            contador += 1
    
    return bandera_vacio

# def detectar_click(matriz:list)->list:
#     mouse_pos = []
#     for event in pygame.event.get():
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             for i in range(len(matriz)):
#                 for j in range(len(matriz[0])):
#                     pos_mouse = pygame.mouse.get_pos()
#                     mouse_pos[i][j] = pos_mouse
#     return mouse_pos

def dibujar_tablero(matriz, ventana):
    '''
    Recibe una matriz por parametro y la recorre y crea un rectangulo de color segun corresponda.
    Devuelve una matriz con las ubicaciones de los rectangulos.
    '''

    if len(matriz) == 10:
        tam_celda = 40
    elif len(matriz) == 20:
        tam_celda = 25
    else:
        tam_celda = 15

    ancho_tablero = tam_celda * len(matriz[0])
    mitad_tablero_x = ancho_tablero // 2
    eje_x_centrado = (ANCHO_VENTANA // 2) - mitad_tablero_x
    
    alto_tablero = tam_celda * len(matriz)
    mitad_tablero_y = alto_tablero // 2
    eje_y_centrado = (ALTO_VENTANA // 2) - mitad_tablero_y

    # rect_tablero = pygame.draw.rect(ventana, NEGRO,(eje_x_centrado, eje_y_centrado, ancho_tablero, alto_tablero))

    matriz_rectangulos = inicializar_tablero(dificultad)

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            eje_x = j * tam_celda
            eje_y = i * tam_celda
            if matriz[i][j] == 0:
                color = AZUL
            else:
                color = ROJO
            
            rect = pygame.draw.rect(ventana, color,(eje_x_centrado + eje_x, eje_y_centrado + eje_y, tam_celda, tam_celda))
            
            matriz_rectangulos[i][j] = rect

    return matriz_rectangulos
