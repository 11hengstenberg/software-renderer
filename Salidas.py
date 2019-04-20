""" universidad del Valle de Guatemala
	Graficas por Computadora
	Alexis Fernando Hengstenberg Chocooj
	Carnet: 17699
	Proyecto
	SoftwareRender
"""

#importamos las librerias.


from SoftwareR import *


#llamamos ala funcion SR
image = SoftwareR()
#inicializamos la funcion
image.glInit()
#Creamos la ventna de un tamaño determiado
image.glCreateWindow(1500, 1500)
#colocamos el color para el fondo del BMP
image.glClearColor(0.3,0.3,1)
#cololaamos la camara en una posicion
image.lookAt((-2,0,5), (0,0,0), (0,1,0))



#ejemplos de camara diferente


#image.lookAt((2,0,5), (0,0,0), (0,1,0))
#image.lookAt((1,0,5), (0,0,0), (0,1,0))
#image.lookAt((3,1,5), (0,0,0), (0,1,0))
#image.lookAt((4,2,3), (0,0,0), (1,1,0))
#image.lookAt((4,4,4), (0,0,0), (0,1,0))



#creamos el lugar donde podemos pintar o dibujar que sea igual o mas pequeño que el glCreateWindow
image.glViewPort(0,0,1500,1500)

#mandamos el archivo de salida con el nombre
#en una carpeta por aparte.
image.setFileName("./Out/ProyectoArco.bmp")




#modelos obj cargados en software Renders


#arco
#es lo principal del mpb y el obj mas grande
#terminado
#imagen.loadOBJ(hubicacion(x,y,z), traslacion(x,y,z),tamanio(x,y,z), rotacion(x,y,z))
image.loadOBJ("./Modelos/arco.obj", translate=(0.8,-1,-1), scale=(0.55,0.55,0.55), rotate=(0,0,0))

#persona
#persona que se encuentra a la par del arco
#terminado
#imagen.loadOBJ(hubicacion(x,y,z), traslacion(x,y,z),tamanio(x,y,z), rotacion(x,y,z))
image.loadOBJ("./Modelos/persona.obj", translate=(0.6,-0.9,0), scale=(0.033,0.033,0.033), rotate=(0,1,0))


#bicicleta
#bicicleta por el arco es el mas complejo
#terminado
#imagen.loadOBJ(hubicacion(x,y,z), traslacion(x,y,z),tamanio(x,y,z), rotacion(x,y,z))
image.loadOBJ("./Modelos/bicicleta.obj", translate=(-0.2,-1,-1), scale=(0.05,0.05,0.05), rotate=(0,0.5,0))


#Arbol 1
#terminado
#segun la camara 1 es el arbol del lado izquierdo
#imagen.loadOBJ(hubicacion(x,y,z), traslacion(x,y,z),tamanio(x,y,z), rotacion(x,y,z))
image.loadOBJ("./Modelos/arbol1.obj", translate=(1,-1,0), scale=(0.2,0.2,0.2), rotate=(0,0,0))

#arbol 2
#arbol derecho segun la camara 1 forma distinta de arbol
#terminado
#imagen.loadOBJ(hubicacion(x,y,z), traslacion(x,y,z),tamanio(x,y,z), rotacion(x,y,z))
image.loadOBJ("./Modelos/arbol2.obj", translate=(-0.8,-1,0), scale=(0.1,0.1,0.1), rotate=(0,0,0))


#avion
#avion que se encuentra en el cielo
#terminado
#imagen.loadOBJ(hubicacion(x,y,z), traslacion(x,y,z),tamanio(x,y,z), rotacion(x,y,z))
image.loadOBJ("./Modelos/airplane.obj", translate=(0,0.6,-1), scale=(0.07,0.07,0.07), rotate=(0,0.5,0))




#finalizamos el programa
image.glFinish()
