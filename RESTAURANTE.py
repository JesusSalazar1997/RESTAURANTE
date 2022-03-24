import os

CARPETA = 'ordenes/'
EXTENSION = '.txt'

#Class 
class Orden:
  def __init__(self, nombre, paquete, paquete1, total):
      self.nombre = nombre
      self.paquete = paquete
      self.paquete1 = paquete1
      self.total = total

paquete1 = 'Hamburguesa', 40
paquete2 = 'Hamburguesa con papas', 100
paquete3 = 'Hamburguesa con papas y refresco', 120
paquete4 = 'Hot Dog', 20
paquete5 = 'Hot Dog con papas', 50
paquete6 = 'Hot Dog con papas y refresco', 80
papas_extras2 = 'Papas extra',40
refresco_extra1 = 'Refresco extra', 50

def app():
    #Crear carpeta restaurante de ordenes
    crear_ordenes()
    #Mostrar menú del restaurante
    mostrar_menu() 

    preguntar = True
    while preguntar:
        opcion = input('Selecciona tu orden: \r\n')
        opcion = int(opcion)
        #Mostrar menú adicional
        mostrar_menuadicional() 
        extra = input('Seleccione: \r\n')
        extra = int(extra)
          #Ejecutar las opciones

        if opcion ==1 and  extra == 1:
          print(f'Tu orden es: {paquete1[0]} con {refresco_extra1[0]} \r\nTotal: {paquete1[1] + refresco_extra1[1]}')
          orden1 = paquete1[0]
          orden2 = refresco_extra1[0]
          total = paquete1[1] + refresco_extra1[1]
          crear_orden(orden1,orden2, total)
          preguntar = False
        elif opcion == 1 and extra == 2:
          print(f'Tu orden es: {paquete1[0]} con {papas_extras2[0]} \r\nTotal: {paquete1[1] + papas_extras2[1]}')
          orden1 = paquete1[0]
          orden2 = papas_extras2[0]
          total = paquete1[1] + papas_extras2[1]
          crear_orden(orden1,orden2, total)
          preguntar = False
        elif opcion == 1 and extra == 0:
          print(f'Tu orden es: {paquete1[0]} \r\nTotal: {paquete1[1]}')
          orden1 = paquete1[0]
          orden2 = 'No aplica'
          total = paquete1[1]
          crear_orden(orden1, orden2, total)
          preguntar = False
        elif opcion == 2 and  extra == 1:
          print(f'Tu orden es: {paquete2[0]} y {refresco_extra1[0]} \r\nTotal: {paquete2[1] + refresco_extra1[1]}')
          orden1 = paquete2[0]
          orden2 = refresco_extra1[0]
          total = paquete2[1] + refresco_extra1[1]
          crear_orden(orden1,orden2, total)
          preguntar = False
        elif opcion == 2 and extra == 2:
          print(f'Tu orden es: {paquete2[0]} y {papas_extras2[0]} \r\nTotal: {paquete2[1] + papas_extras2[1]}')
          orden1 = paquete2[0]
          orden2 = papas_extras2[0]
          total = paquete2[1] + papas_extras2[1]
          crear_orden(orden1,orden2, total)
          preguntar = False
        elif opcion == 2 and extra == 0:
          print(f'Tu orden es: {paquete2[0]} \r\nTotal: {paquete2[1]}')
          orden1 = paquete2[0]
          orden2 = 'No aplica'
          total = paquete2[1]
          crear_orden(orden1, orden2, total) 
          preguntar = False
        elif opcion == 3 and  extra == 1:
          print(f'Tu orden es: {paquete3[0]} y {refresco_extra1[0]} \r\nTotal: {paquete3[1] + refresco_extra1[1]}')
          orden1 = paquete3[0]
          orden2 = refresco_extra1[0]
          total = paquete3[1] + refresco_extra1[1]
          crear_orden(orden1,orden2, total) 
          preguntar = False
        elif opcion == 3 and extra == 2:
          print(f'Tu orden es: {paquete3[0]} y {papas_extras2[0]} \r\nTotal: {paquete3[1] + papas_extras2[1]}')
          orden1 = paquete3[0]
          orden2 = papas_extras2[0]
          total = paquete3[1] + papas_extras2[1]
          crear_orden(orden1,orden2, total) 
          preguntar = False
        elif opcion == 3 and extra == 0:
          print(f'Tu orden es: {paquete3[0]} \r\nTotal: {paquete3[1]}')
          orden1 = paquete3[0]
          orden2 = 'No aplica'
          total = paquete3[1]
          crear_orden(orden1,orden2, total) 
          preguntar = False
        elif opcion == 4 and  extra == 1:
          print(f'Tu orden es: {paquete4[0]} y {refresco_extra1[0]} \r\nTotal: {paquete4[1] + refresco_extra1[1]}')
          orden1 = paquete4[0]
          orden2 = refresco_extra1[0]
          total = paquete4[1] + refresco_extra1[1]
          crear_orden(orden1,orden2, total) 
          preguntar = False
        elif opcion == 4 and extra == 2:
          print(f'Tu orden es: {paquete4[0]} y {papas_extras2[0]} \r\nTotal: {paquete4[1] + papas_extras2[1]}')
          orden1 = paquete4[0]
          orden2 = papas_extras2[0]
          total = paquete4[1] + papas_extras2[1]
          crear_orden(orden1,orden2, total) 
          preguntar = False
        elif opcion == 4 and extra == 0:
          print(f'Tu orden es: {paquete4[0]} \r\nTotal: {paquete4[1]}')
          orden1 = paquete4[0]
          orden2 = 'No aplica'
          total = paquete4[1]
          crear_orden(orden1,orden2, total) 
          preguntar = False
        elif opcion == 5 and  extra == 1:
          print(f'Tu orden es: {paquete5[0]} y {refresco_extra1[0]} \r\nTotal: {paquete5[1] + refresco_extra1[1]}')
          orden1 = paquete5[0]
          orden2 = refresco_extra1[0]
          total = paquete5[1] + refresco_extra1[1]
          crear_orden(orden1,orden2, total)  
          preguntar = False
        elif opcion == 5 and extra == 2:
          print(f'Tu orden es: {paquete5[0]} y {papas_extras2[0]} \r\nTotal: {paquete5[1] + papas_extras2[1]}')
          orden1 = paquete5[0]
          orden2 = papas_extras2[0]
          total = paquete5[1] + papas_extras2[1]
          crear_orden(orden1,orden2, total)   
          preguntar = False
        elif opcion == 5 and extra == 0:
          print(f'Tu orden es: {paquete5[0]} \r\nTotal: {paquete5[1]}')
          orden1 = paquete5[0]
          orden2 = 'No aplica'
          total = paquete5[1]
          crear_orden(orden1,orden2, total) 
          preguntar = False
        elif opcion == 6 and  extra == 1:
          print(f'Tu orden es: {paquete6[0]} y {refresco_extra1[0]} \r\nTotal: {paquete6[1] + refresco_extra1[1]}')
          orden1 = paquete6[0]
          orden2 = refresco_extra1[0]
          total = paquete6[1] + refresco_extra1[1]
          crear_orden(orden1,orden2, total)   
          preguntar = False
        elif opcion == 6 and extra == 2:
          print(f'Tu orden es: {paquete6[0]} y {papas_extras2[0]} \r\nTotal: {paquete6[1] + papas_extras2[1]}')
          orden1 = paquete6[0]
          orden2 = papas_extras2[0]
          total = paquete6[1] + papas_extras2[1]
          crear_orden(orden1,orden2, total)   
          preguntar = False
        elif opcion == 6 and extra == 0:
          print(f'Tu orden es: {paquete6[0]} \r\nTotal: {paquete6[1]}')
          orden1 = paquete6[0]
          orden2 = 'No aplica'
          total = paquete6[1]
          crear_orden(orden1,orden2, total)   
          preguntar = False
        else:
          print('Opción no válida, intente de nuevo')



def  mostrar_menuadicional():
    print('¿Deseas agregar un extra?')
    print('1) Refresco extra $50')
    print('2) Papas extras $40')
    print('0) No deseo agregar extras')

#Mostrar el menú
def mostrar_menu():
    print('Menú:')
    print('1) Hamburguesa $40')
    print('2) Hamburguesa con papas $100')
    print('3) Hamburguesa con papas y refresco $120')
    print('4) Hot Dog  $20')
    print('5) Hot Dog con papas  $50')
    print('6) Hot Dog con papas y refresco $80')

#Crear carpeta restaurante
def crear_ordenes():
    if not os.path.exists(CARPETA):
      os.makedirs(CARPETA)

def existe_orden(nombre):
    return  os.path.isfile(CARPETA + nombre + EXTENSION)


def crear_orden(orden1, orden2, total):
  numero = 1
  nombre = str(numero)
  total = str(total)
  #Revisar que no exista la misma orden
  existe = existe_orden(nombre)
  while existe:
     numero = int(nombre)
     numero += 1
     nombre = str(numero)
     #Revisar que no exista la misma orden
     existe = existe_orden(nombre)
  if not existe:
    with open(CARPETA + nombre + EXTENSION, 'w') as archivo:
      #Instanciar la clase
      orden = Orden(nombre, orden1, orden2, total)
      #Escribir el archivo
      if orden2 == 'No aplica':
        archivo.write('Numero de Orden: ' + orden.nombre + '\r\n')
        archivo.write('Paquete 1: ' + orden.paquete + '\r\n')
        archivo.write('Total: ' + orden.total + '\r\n')
      else:
        archivo.write('Numero de Orden: ' + orden.nombre + '\r\n')
        archivo.write('Paquete 1: ' + orden.paquete + '\r\n')
        archivo.write('Paquete 2: ' + orden.paquete1 + '\r\n')
        archivo.write('Total: ' + orden.total + '\r\n')

       #Mensaje de éxito
      print('\r\nOrden creada corectamente \r\n')
      existe = False



app()