#------------------------------------------#
#Universidad del Valle de Guatemala
#Graficas por computadora
#Alexis Fernando Hengstenberg Chocooj
#Carne: 17699
#polygon
#------------------------------------------#

from sr import *

#extra
#creamos ventana 800*600
glCreateWindow(800,800)
#espacio para pintar dentro de la ventana
glViewPort(0, 0,800, 800)
#color negro
glClearColor(0,0, 0)
#pintamos ventana de color negro
glClear()
#color blanco para vertex
glColor(1, 1, 1)
globj("medieval house.obj")
globjbmp(escala=(0.00004,0.00004,0.00004))
glFinish("cc.bmp")
#fin del prigrama
