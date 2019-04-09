#------------------------------------------#
#Universidad del Valle de Guatemala
#Graficas por computadora
#Alexis Fernando Hengstenberg Chocooj
#Carne: 17699
#tarea 1
#------------------------------------------#

#-----------Libreria----------#
import struct
import random
import math
#-----------------------------#

#--------Matrices y operaciones--------#

#-------------Variables--------------#
tImagen=None
viewPortX=None
viewPortY=None
viewPortWidth=None
viewPortHeight=None
colormtl=[]
nombremtl=[]
coordenadas=[]
caraT=[]
caraTN=[]
normales=[]
caraifn=[]
#-----------------funciones-----------------#
def char(c):
	return struct.pack("=c",c.encode('ascii'))
def word(c):
	return struct.pack("=h",c)
def dword(c):
	return struct.pack("=l",c)
def color(r,g,b):
	return bytes([b,g,r])

def glPolygon(vertexList):

	for i in range(len(vertexList)):
		if i == len(vertexList)-1:
			st = vertexList[i]
			fi = vertexList[0]
		else:
			st = vertexList[i]
			fi = vertexList[i+1]
		glLine(st[0], st[1], fi[0], fi[1])

	#tamanio de la imagen
def glCreateWindow(width,height):
	global tImagen
	tImagen=Bitmap(width,height)

	#ventaja dibujable.
def glViewPort(x,y,width,height):
	#para poder utilizarlas en todas las clases
	global viewPortX
	global viewPortY
	global viewPortHeight
	global viewPortWidth
	#igualar variables
	viewPortX = x
	viewPortY = y
	viewPortHeight = height
	viewPortWidth = width

	#llenar todo de un solo color
def glClear():
	global tImagen
	tImagen.clear()

	#cambiar el color del glclear
def glClearColor(r,g,b):
	global tImagen
	nR= int(math.ceil(r * 255))
	nG= int(math.ceil(g * 255))
	nB= int(math.ceil(b* 255))
	tImagen.clear_color = color(nR, nG, nB)

	#cambiar color con el que funciona el vertex
def glColor(r,g,b):
	global tImagen
	nR= int(r*255)
	nG= int(g*255)
	nB= int(b*255)
	tImagen.vertex_color = color(nR, nG, nB)
	return color(nR,nG,nB)
	#colocar el punto
def glVertex(x,y):
	global tImagen
	global viewPortX
	global viewPortY
	global viewPortHeight
	global viewPortWidth
	xFinal= int((x+1) * viewPortWidth * 0.5 + viewPortX)
	yFinal= int((y+1) * viewPortHeight * 0.5 + viewPortY)
	tImagen.point(xFinal,yFinal,tImagen.vertex_color)

#lineas
def glLine (x1, y1, x2, y2):
		global viewPortHeight
		global viewPortWidth
		global viewPortX
		global viewPortY

		x1 = int(viewPortWidth * (x1+1) * (1/2) +viewPortX)
		y1 = int(viewPortHeight * (y1+1) * (1/2) + viewPortY)
		x2 = int(viewPortWidth * (x2+1) * (1/2) + viewPortX)
		y2 = int(viewPortHeight * (y2+1) * (1/2) + viewPortY)

		dy = abs(y2 - y1)
		dx = abs(x2 - x1)
		steep = dy > dx
		if steep:
			x1, y1 = y1, x1
			x2, y2 = y2, x2
		if (x1 > x2):
			x1, x2 = x2, x1
			y1, y2 = y2, y1
		dy = abs(y2 - y1)
		dx = abs(x2 - x1)
		offset = 0
		threshold = dx
		y = y1
		for x in range(x1, x2 + 1):
			if steep:
				tImagen.point(y, x, tImagen.vertex_color)
			else:
				tImagen.point(x, y, tImagen.vertex_color)

			offset += dy * 2
			if offset >= threshold:
				y +=1 if y1 < y2 else -1
				threshold += 2 * dx


def glPolygonFull(vertexList):

	#inicio en X
	comienzoX = sorted(vertexList, key=lambda tup: tup[0])[0][0]
	#final X
	finalX = sorted(vertexList, key=lambda tup: tup[0], reverse = True)[0][0]
	#inicio Y
	comienzoY = sorted(vertexList, key=lambda tup: tup[1])[0][1]
	#final en T
	finalY = sorted(vertexList, key=lambda tup: tup[1], reverse=True)[0][1]
	#operaciones con las x y Y
	#inicio en X
	#convertir en int
	comienzoX = int(viewPortWidth * (comienzoX+1) * (1/2) + viewPortX)
	#final en X
	#convertir en int
	finalX = int(viewPortWidth * (finalX+1) * (1/2) + viewPortX)
	#inicio en Y
	#convertir en int
	comienzoY = int(viewPortWidth * (comienzoY+1) * (1/2) + viewPortX)
	#final en Y
	#convertir en int
	finalY = int(viewPortWidth * (finalY+1) * (1/2) + viewPortX)
	#enviar a la funcion pylygon los valores de vertexList
	#----glPolygon(vertexList)

	#for para llenar el poligono
	for x in range(comienzoX, finalX+1):

		for y in range(comienzoY, finalY+1):
			#pintar el poligono
			isInside = glPointInPolygon(conX(x),conY(y), vertexList)
			if isInside:
				#pintar el poligono
				tImagen.point(x, y, 0)

	#conversion en x
def conX(x):
	#conversion para centrar
	conX = ((2*x)/viewPortWidth) - viewPortX - 1
	#regresamos conX despues de operar con la viewportWidth
	return conX
#conversion en Y
def conY(y):
	#conversion para centrar
	conY = (((2*y)/viewPortHeight) - viewPortY - 1)
	#regresamos conY despues de operar con la viewportHenight
	return conY
	#finalizar con la salida
def glFinish(nombre):
	global tImagen
	tImagen.write(nombre)
#para encontrar el centro


#llenar los poligonos
def glPointInPolygon(x, y, vertexList):
	contador = 0
	p1 = vertexList[0]
	n = len(vertexList)
	for i in range(n+1):
		p2 = vertexList[i % n]
		if(y > min(p1[1], p2[1])):
			if(y <= max(p1[1], p2[1])):
				if(p1[1] != p2[1]):
					xinters = (y-p1[1])*(p2[0]-p1[0])/(p2[1]-p1[1])+p1[0]
					if(p1[0] == p2[0] or x <= xinters):
						contador += 1
		p1 = p2
	if(contador % 2 == 0):
		return False
	else:
		return True
	#algoritmo extraido de http://www.eecs.umich.edu/courses/eecs380/HANDOUTS/PROJ2/InsidePoly.html
	#llenar poligonos

#pintar con color las caras.
def glmtl (name):
	#variables globales
	global nombremtl
	global colormtl
	#abrimos el archivo
	archivo=open(name,"r")
	#leemos todas las lineas
	for i in archivo.readlines():
		line=i.strip().split(" ")
		#guardamos todos los nombres
		if line[0] =="newmtl":
			nombremtl.append(line[1])
		#guardamos todos los colores
		if line[0]=="Kd":
			color=(float(line[1]),float(line[2]),float(line[3]))
			colormtl.append(color)
	#cerramos el archivo
	archivo.close()




def globj(nombre):
	global coordenadas
	global caraT
	global caraTN
	global normales
	global caraifn
	nombreobjmtl=0
	materialI=0
	contador=0
	archivo=open(nombre,"r")
	for i in archivo.readlines():
		linea=i.strip().split(" ")
		if linea[0]=="usemtl":

			if contador==0:
				nombreobjmtl=linea[1]
				caraI=len(caraT)
				materialI=nombreobjmtl
			if contador>0:
				caraF=len((caraT))-1
				caraifn.append((nombreobjmtl,caraI,caraF))
				caraI=len(caraT)
				nombreobjmtl=linea[1]

			contador=contador+1



		if linea[0]== "v":

			#o = 1 if linea[0]==""else 0
			numero1=float(linea[1])
			numero2=float(linea[2])
			numero3=float(linea[3])
			xy=(numero1,numero2,numero3)
			coordenadas.append(xy)
		if linea[0]=="f":
			if len(linea)>5:
				v1=(int(linea[1].split("/")[0]), int((linea[1].split("/")[-1])))
				v2=(int(linea[2].split("/")[0]), int((linea[2].split("/")[-1])))
				v3=(int(linea[3].split("/")[0]), int((linea[3].split("/")[-1])))
				v4=(int(linea[4].split("/")[0]), int((linea[4].split("/")[-1])))
				caras=(v1,v2,v3,v4)
			else:
				v1=(int(linea[1].split("/")[0]), int((linea[1].split("/")[-1])))
				v2=(int(linea[2].split("/")[0]), int((linea[2].split("/")[-1])))
				v3=(int(linea[3].split("/")[0]), int((linea[3].split("/")[-1])))
				caras=(v1,v2,v3)
			caraT.append(caras)
		if linea[0]=="vn":
			nor1 = float(linea[1])
			nor2 = float(linea[2])
			nor3 = float(linea[3])
			normal = (nor1,nor2,nor3)
			normales.append(normal)

	if materialI != nombreobjmtl:
		caraF=len((caraT))-1
		caraifn.append((nombreobjmtl,caraI,caraF))
		print(caraifn)

	archivo.close()

def globjbmp (escala=(1,1,1)):
	luz=(0,0,1)
	#import type
	global coordenadas
	global caraT
	global caraTN
	global normales
	global colormtl
	global nombremtl
	global caraifn
	contador=0



	for i in caraT:
		coordenadaT=[]
		for p in i:
			coordenadaT.append((coordenadas[p[0]-1][0]*escala[0],coordenadas[p[0]-1][1]*escala[1],coordenadas[p[0]-1][2]*escala[2]))
		if caraifn[0][1]==contador:
			numerof=nombremtl.index(caraifn[0][0])
			color=colormtl[numerof]
		if caraifn[1][1]==contador:
			numerof=nombremtl.index(caraifn[1][0])
			color=colormtl[numerof]

		vnormal = normales[p[1]-1]
		gris=productoPunto(vnormal,luz)

		if gris<0:
			continue

		glColor(gris*color[0], gris*color[1], gris*color[2])
		glPolygonFull(coordenadaT)
		contador+=1

def vector (punto1,punto2):
	return(punto2[0]-punto1[0],punto2[1]-punto1[1],punto2[2]-punto1[2])

def productoX (v1,v2):

	hola=(v1[1]*v2[2]-v1[2]*v2[1],v1[2]*v2[0]-v1[0]*v2[2],v1[0]*v2[1]-v1[1]*v2[0])

	return hola

def productoPunto (v1,v2):
	adios=(v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2])
	return adios




#---------------------------clase-------------------------#
class Bitmap(object):
	vertex_color=1
	def __init__(self, width,height):
		self.width = width
		self.height = height
		self.pixels=[]
		self.clear_color = color(51,102,0)
		self.vertex_color = color(0,0,0)
		self.clear()

	def clear(self):
		self.pixels = [
			[self.clear_color for x in range(self.width)]
			for y in range (self.height)
		]

	def write(self, filename):
		f = open(filename, 'wb')



		f.write(char('B'))
		f.write(char('M'))
		f.write(dword(14 + 40 + self.width * self.height *3))
		f.write(dword(0))
		f.write(dword(14+40))
		f.write(dword(40))
		f.write(dword(self.width))
		f.write(dword(self.height))
		f.write(word(1))
		f.write(word(24))
		f.write(dword(0))
		f.write(dword(self.width * self.height *3))
		f.write(dword(0))
		f.write(dword(0))
		f.write(dword(0))
		f.write(dword(0))

		for x in range(self.height):
			for y in range(self.width):
				f.write(self.pixels[x][y])

		f.close()

	def point(self, x, y, color):
		self.pixels[y][x] = self.vertex_color


#r = Bitmap(300,300)
#----------------Linea-------------------#
#r.point(100,201, color(255, 255, 255))
#r.point(100,202, color(255, 255, 255))
#r.point(100,203, color(255, 255, 255))
#r.point(100,204, color(255, 255, 255))
#r.point(100,205, color(255, 255, 255))
#r.point(100,206, color(255, 255, 255))
#r.point(100,207, color(255, 255, 255))
#r.point(100,208, color(255, 255, 255))
#r.point(100,209, color(255, 255, 255))
#r.point(100,210, color(255, 255, 255))
#----------------------------------------#
