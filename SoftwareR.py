""" universidad del Valle de Guatemala
	Graficas por Computadora
	Alexis Fernando Hengstenberg Chocooj
	Carnet: 17699
	clase OBJ
"""


#Importamos las librerias

#clase de bitmap
from BMP import *
#clase para cargar el obj
from CargarOBJ import *
#clase para cargar las texturas
from Texturas import *
#clase para obtener seno y cos
from math import cos, sin




#creamos la clase de software SoftwareRender
class SoftwareR(object):




#para iniciar el software render.
	def glInit(self):

		#los valores iniciales
		self.imagen = BMP(0,0)
		#los tamanios de alto y ancho
		self.viewPortStart = (0,0)
		self.vieportSize = (0,0)
		#introducimos el color
		self.color = self.imagen.color(255,255,255)
		self.obj = None
		self.texto = None




#
#  def display(self, filename):
#
#    self.write(filename)
#
#    try:
#      from wand.image import Image
#
#      from wand.display import display
#
#
#      with Image(filename=filename) as image:
#        display(image)
#
#    except ImportError:
#      pass  # do nothing if no wand is installed
#
 # def set_color(self, color):
#    self.current_color = color
#
 # def point(self, x, y, color = None):
#
#    try:
#      self.pixels[y][x] = color or self.current_color
#    except:
#
#      pass
#

		#encviamos la imagen en formato bmp
	def setImage(self, bmp):
		self.imagen = bmp



		#creamos la funcion glCreateWindow
		#variables:
		#width altura
		#height ancho
		#funcion para crear la ventana de un tamaño determinado
	def glCreateWindow(self, width, height):

		#tamanio del bmp que se creara.
		self.imagen = BMP(width, height)

		#tamanio para poder dibujar
		self.vieportSize = (width, height)


		#definimos la funcion glViewPort
		#variables
		#x coordenada donde inicia dentro de la ventana creada
		#Y coordenada donde inicia dentro de la ventana creada
		#width altura de la ventada donde se podra pintar
		#height ancho de la ventana donde se podra pintar
	def glViewPort(self, x, y, width, height):

		#coordenadas de inicio
		self.viewPortStart = (x, y)


		#tamaño
		self.vieportSize = (width,height)



		#definimos la funcio glClear
		#funcion de pintar de un solo color la ventana o la imagen
	def glClear(self):
		self.imagen.clear()


		#definimos la funcion glClearColor
		#variables:
		#R
		#G
		#B
		#su funicion es cambiar el color para que glClear cambie totalmente el color de la ventana
	def glClearColor(self, r, g, b):

		#introducimos el color para la ventana o el fondo
		self.imagen.clear(int(255*r), int(255*g), int(255*b))




		#definimos la funcio glVertex
		#variables:
		#x coordenada en x dentro del viewPortX
		#y coordenada en y dentro del viewPortY
		#la funcion es cambiar de color o colocar un punto de un color dentro de la imagen
	def glVertex(self, x, y):


		#hubicacion de la entrada en x
		viewPortX = int(self.vieportSize[0] * (x+1) * (1/2) + self.viewPortStart[0])
		#hubicacion de la entrada en y
		viewPortY = int(self.vieportSize[1] * (y+1) * (1/2) + self.viewPortStart[1])


		self.imagen.point(viewPortX, viewPortY, self.color)




		#definimos la funcion glVertexColor
		#variables
		#x coordenada donde cambia de color en # X
		#y coordenada donde cambia de color en y
	def glVertexColor(self, x, y):

		viewPortX = int(self.vieportSize[0] * (x+1) * (1/2) + self.viewPortStart[0])



		viewPortY = int(self.vieportSize[1] * (y+1) * (1/2) + self.viewPortStart[1])



		self.imagen.point(viewPortX, viewPortY, self.color)


		self.imagen.point(viewPortX, viewPortY+1, self.color)


		self.imagen.point(viewPortX+1, viewPortY, self.color)


		self.imagen.point(viewPortX+1, viewPortY+1, self.color)




		#definimos la funcion glColor
		#variables:
		#R para la intencidad en el color rojo
		#G para la initencidad en el color verde
		#B para la intencidad en el color azul
		#la funcion principal es cambiar el color predeterminado del vectex
	def  glColor(self, r, g, b):

		#obtenemos los valores
		#operamos
		self.color = self.imagen.color(int(255*r), int(255*g), int(255*b))
		#Retornamos los nuevos vaores de RGB
		return self.imagen.color(int(255*r), int(255*g), int(255*b))


		#definimos la funcion glFinish
		# es donde se escribe el archivo final
		# la salida es un archivo .BMP
		#con el nombre que nos mandaron
	def glFinish(self):


		self.imagen.write(self.__filename)


		#definimos la funcion glLine
		#obtenemos las variables:
		#x0 coordenada donde comienza la linea en x
		#x1 coordenada donde termina en x
		#y0 coordenada donde comienza la linea en y
		#y1 coordenada donde termina en y
		#su funcion es crear lineas dentro de la imagen.

	def glLine(self, xo, yo, xf, yf):

		#x1 donde comenzara la linea
		x1 = int(self.vieportSize[0] * (xo+1) * (1/2) + self.viewPortStart[0])

		#y1 donde comenzara la linea
		y1 = int(self.vieportSize[1] * (yo+1) * (1/2) + self.viewPortStart[1])

		#x2 donde terminara la linea
		x2 = int(self.vieportSize[0] * (xf+1) * (1/2) + self.viewPortStart[0])

		#y2 donde terminara la linea
		y2 = int(self.vieportSize[1] * (yf+1) * (1/2) + self.viewPortStart[1])

		#diferencial y
		#diferencial x
		#abs valor absoluto de la resta.
		dy = abs(y2 - y1)
		dx = abs(x2 - x1)


		#paso dy, dx
		steep = dy > dx

		#corregir los valores dependiendo de cuales son mas graandes.
		#cambiar de  valores entre las x y y  para comenzar de nuevos
		#y que x1 y1 siemrpe sean menor
		if steep:
			x1, y1 = y1, x1
			x2, y2 = y2, x2
		if (x1 > x2):
			x1, x2 = x2, x1
			y1, y2 = y2, y1

		#diferencial entre y2 y1
		#diferencial entre x2 , x1
		dy = abs(y2 - y1)
		dx = abs(x2 - x1)
		offset = 0
		threshold = dx
		y = y1

		#for para pintar la linea
		for x in range(x1, x2 + 1):


			if steep:

				self.imagen.point(y, x, self.color)

			else:
				self.imagen.point(x, y, self.color)


			offset += dy * 2


			if offset >= threshold:
				y +=1 if y1 < y2 else -1
				threshold += 2 * dx

		#definimos la funcions setFileName
		#enviamos el nombre para guardar los archivos
	def setFileName(self, filename):

		#el nombre
		self.__filename = filename


		#definimos la funcion loadOBJ

	def loadOBJ(self, filename, translate=(0, 0, 0), scale=(1, 1, 1), fill=True, textured=None, rotate=(0, 0, 0), shader=None):

		self.modelMatrix(translate, scale, rotate)
		self.obj = CargarOBJ(filename)

		#cargamos el objeto
		self.obj.load()

		#generamos la luz
		light = self.norm((0,0,1))
		faces = self.obj.getFaceList()
		vertex = self.obj.getVertexList()
		materials = self.obj.getMaterials()
		tvertex = self.obj.getTextureVertex()
		nvertex = self.obj.getVertexNormalList()
		matFaces = self.obj.getMaterialFaces()
		self.texto = Texture(textured)



		#materiales
		if materials:
			for mats in matFaces:


				start, stop = mats[0]

				color = materials[mats[1]].difuseColor

				for index in range(start, stop):

					face = faces[index]
					vcount = len(face)



					if vcount == 3:


						f1 = face[0][0] - 1

						f2 = face[1][0] - 1

						f3 = face[2][0] - 1


						a = self.transform(vertex[f1])


						b = self.transform(vertex[f2])

						c = self.transform(vertex[f3])






#shaders
						if shader:
							nA = nvertex[f1]

							nB = nvertex[f2]

							nC = nvertex[f3]

							self.crearTriangulo(a, b, c, baseColor=color, shader=shader, normals=(nA, nB, nC))
						else:
							normal = self.norm(self.cross(self.sub(b,a), self.sub(c,a)))
							intensity = self.dot(normal, light)

							if not self.texto.isTextured():
								if intensity < 0:
									continue
								self.crearTriangulo(a, b, c,color=self.glColor(color[0]*intensity, color[1]*intensity, color[2]*intensity))


		else:

			for face in faces:

				vcount = len(face)

				if vcount == 3:
					f1 = face[0][0] - 1

					f2 = face[1][0] - 1

					f3 = face[2][0] - 1


					a = self.transform(vertex[f1])

					b = self.transform(vertex[f2])

					c = self.transform(vertex[f3])

					if shader:
						nA = nvertex[f1]

						nB = nvertex[f2]

						nC = nvertex[f3]



						self.crearTriangulo(a, b, c, baseColor=color, shader=shader, normals=(nA, nB, nC))



					else:



						normal = self.norm(self.cross(self.sub(b,a), self.sub(c,a)))
						intensity = self.dot(normal, light)



						if not self.texto.isTextured():

							if intensity < 0:
								continue
							self.crearTriangulo(a, b, c,color=self.glColor(intensity, intensity, intensity))



						else:

							if self.texto.isTextured():
								t1 = face[0][-1] - 1
								t2 = face[1][-1] - 1
								t3 = face[2][-1] - 1
								tA = tvertex[t1]
								tB = tvertex[t2]
								tC = tvertex[t3]
								self.crearTriangulo(a, b, c, texture=self.texto.isTextured(), texture_coords=(tA, tB, tC), intensity=intensity)

				else:
					f1 = face[0][0] - 1
					f2 = face[1][0] - 1
					f3 = face[2][0] - 1
					f4 = face[3][0] - 1


					vertexList = [self.transform(vertex[f1]),self.transform(vertex[f2]),self.transform(vertex[f3]),self.transform(vertex[f4])]




					normal = self.norm(self.cross(self.sub(vertexList[0], vertexList[1]), self.sub(vertexList[1], vertexList[2])))



					intensity = self.dot(normal, light)



					A, B, C, D = vertexList

					if not textured:

						if intensity < 0:
							continue
						self.crearTriangulo(A, B, C, color=self.glColor(intensity, intensity, intensity))

						self.crearTriangulo(A, C, D, color=self.glColor(intensity, intensity, intensity))

					else:
						if self.texto.isTextured():
							t1 = face[0][-1] - 1

							t2 = face[1][-1] - 1

							t3 = face[2][-1] - 1

							t4 = face[3][-1] - 1

							tA = tvertex[t1]

							tB = tvertex[t2]

							tC = tvertex[t3]


							tD = tvertex[t4]
							self.crearTriangulo(A, B, C, texture=self.texto.isTextured(), texture_coords=(tA, tB, tC), intensity=intensity)

							self.crearTriangulo(A, C, D, texture=self.texto.isTextured(), texture_coords=(tA, tC, tD), intensity=intensity)




		#definimos la funcion crearTriangulo
		#obtiene las variables
		#A punto de inicio A
		#B punto de inicio B
		#c punto de inicio C
		#color color a pintar el triangulo
		#texture textura que tendra el crearTriangulo
		#texture_coords para ver la hubicacion del triangulo
		#intensidad 1
		#shadets si obtiene
		#baseColor si tiene una base para su color
		#su funcion es ir creando y pintando triangulos dentro de la ventana.

	def crearTriangulo(self, A, B, C, color=None, texture=None, texture_coords=(), intensity=1, normals=None, shader=None, baseColor=(1,1,1)):




		bbox_min, bbox_max = self.bbox(A, B, C)

		for x in range(bbox_min[0], bbox_max[0] + 1):

			for y in range(bbox_min[1], bbox_max[1] + 1):


				w, v, u = self.barycentric(A, B, C, x, y)

				if w < 0 or v < 0 or u < 0:

					continue
				if texture:

					tA, tB, tC = texture_coords

					tx = tA[0] * w + tB[0] * v + tC[0] * u
					ty = tA[1] * w + tB[1] * v + tC[1] * u

					color = self.texto.getColor(tx, ty, intensity)

				elif shader:
					color = shader(self, bary=(w,u,v), Vnormals=normals, baseColor=baseColor)
				z = A[2] * w + B[2] * v + C[2] * u



				if x<0 or y<0:
					continue


				if z > self.imagen.getZbufferValue(x,y):


					self.imagen.point(x, y, color)
					self.imagen.setZbufferValue(x,y,z)

		#definimos la funcion bbox_max
		#entra una lista con vertexN
		#su funcion es encontrar el cuadro delimitado mas pequenio
	def bbox(self, *vertexList):

		xs = [vertex[0] for vertex in vertexList]

		ys = [vertex[1] for vertex in vertexList]
		xs.sort()
		ys.sort()
		return (xs[0], ys[0]), (xs[-1], ys[-1])



	#definimos la funcion de load
	#filname obtenemos el nombre del archivos
	#traslate obtenemos en que posicion estara
	#sale obtenemos el tamanio del objeto
	#textured obtenemos la textura del objeto
	#rotate obtenemos la rotacion del objeto

	#su funcion es trasladar el objeto y cargarlo para poder pintarlo en la imagen

	def load(self, filename, translate=(0, 0, 0), scale=(1, 1, 1),  textured=None, rotate=(0, 0, 0)):

		self.modelMatrix(translate, scale, rotate)
		self.obj = CargarOBJ(filename)
		self.obj.load()
		vertex = self.obj.getVertexList()
		faces = self.obj.getFaceList()
		nvertex = self.obj.getVertexNormalList()
		materials = self.obj.getMaterials()
		tvertex = self.obj.getTextureVertex()
		light = (0,0,1)
		if materials and not textured:
			matIndex = self.obj.getMaterialFaces()
			for mat in matIndex:
				difuseColor = materials[mat[1]].difuseColor
				for i in range(mat[0][0], mat[0][1]):
					cooList = []
					textCoo = []
					for face in faces[i]:
						coo = ((vertex[face[0]-1][0] + translate[0]) * scale[0], (vertex[face[0]-1][1] + translate[1]) * scale[1], (vertex[face[0]-1][2] + translate[2]) * scale[2])
						cooList.append(coo)
					if fill:
						inten = self.dot(nvertex[face[1]-1], light)
						if inten < 0:
							continue
						self.glFilledPolygon(cooList, color=(inten*difuseColor[0],inten*difuseColor[1],inten*difuseColor[2]))
					else:
						self.glPolygon(cooList)
		elif textured and not materials:
			for face in faces:
				cooList = []
				textCoo = []
				for vertexN in face:
					coo = ((vertex[vertexN[0]-1][0] + translate[0]) * scale[0], (vertex[vertexN[0]-1][1] + translate[1]) * scale[1], (vertex[vertexN[0]-1][2] + translate[2]) * scale[2])
					cooList.append(coo)
					if len(vertexN) > 2:
						text = ((tvertex[vertexN[2]-1][0]+ translate[0]) * scale[0], (tvertex[vertexN[2]-1][1]+ translate[1]) * scale[1])
						textCoo.append(text)
				if fill:
					inten = self.dot(nvertex[vertexN[1]-1], light)
					if inten < 0:
						continue
					self.glFilledPolygon(cooList, intensity=inten, texture=textured, textureCoords=textCoo)
				else:
					self.glPolygon(cooList)
				cooList = []
		else:
			for face in faces:
				cooList = []
				textCoo = []
				for vertexN in face:
					coo = vertex[vertexN[0]-1] #self.transform(vertex[vertexN[0]-1])
					cooList.append(coo)
				if fill:
					inten = self.dot(nvertex[vertexN[1]-1], light)
					if inten < 0:
						continue
					self.glFilledPolygon(cooList, color=(inten,inten,inten))
				else:
					self.glPolygon(cooList)
				cooList = []









	def glRenderTextureGrid(self, filename=None, newfile=True, translate=(0, 0), scale=(1, 1)):

		if self.obj:

			faces = self.obj.getFaceList()
			materials = self.obj.getMaterials()
			tvertex = self.obj.getTextureVertex()

			if newfile and filename:
				canvas = SoftwareR()
				canvas.glInit()
				canvas.glCreateWindow(self.imagen.width, self.imagen.height)
				canvas.glViewPort(self.viewPortStart[0], self.viewPortStart[1], self.vieportSize[0], self.vieportSize[1])
				canvas.setFileName(filename)
			else:
				canvas = self

			if materials:
				matIndex = self.obj.getMaterialFaces()
				for mat in matIndex:
					difuseColor = materials[mat[1]].difuseColor
					for i in range(mat[0][0], mat[0][1]):
						textCoo = []
						for face in faces[i]:
							if len(face) > 2:
								text = ((tvertex[face[2]-1][0]+ translate[0]) * scale[0], (tvertex[face[2]-1][1]+ translate[1]) * scale[1], 0)
								textCoo.append(text)
							if len(textCoo)>2:
								canvas.glPolygon(textCoo)
			else:
				for face in faces:
					textCoo = []
					for vertexN in face:
						if len(vertexN) > 2:
							text = ((tvertex[vertexN[2]-1][0]+ translate[0]) * scale[0], (tvertex[vertexN[2]-1][1]+ translate[1]) * scale[1],0)
							textCoo.append(text)
						if len(textCoo)>2:
							canvas.glPolygon(textCoo)
			return canvas


	def glPolygon(self, vertexList):
		"""
		poligono
		"""
		for i in range(len(vertexList)):
			if i == len(vertexList)-1:
				st = vertexList[i]
				fi = vertexList[0]
			else:
				st = vertexList[i]
				fi = vertexList[i+1]
			self.glLine(st[0], st[1], fi[0], fi[1])




			#creamos glFilledPolygon
			#color el color
			#texture el tipo de texturas
			#intensity la intensidad
			#texture coords coordenada de las texturas.

			#algoritmo para rellenar poligonos

	def glFilledPolygon(self, vertexList, color=None, texture=None, intensity=1, textureCoords = (), zVal=True):

		inten = intensity
		if not texture:
			color = self.color if color == None else self.imagen.color(int(255*color[0]), int(255*color[1]), int(255*color[2]))


		else:
			if self.texto == None:

				text = Texture(texture)
				self.texto = text


			else:

				text = self.texto
		startX = (sorted(vertexList, key=lambda tup: tup[0])[0][0])

		finishX = (sorted(vertexList, key=lambda tup: tup[0], reverse = True)[0][0])


		startY = (sorted(vertexList, key=lambda tup: tup[1])[0][1])

		finishY = (sorted(vertexList, key=lambda tup: tup[1], reverse=True)[0][1])


		startX = int(self.vieportSize[0] * (startX+1) * (1/2) + self.viewPortStart[0])

		finishX = int(self.vieportSize[0] * (finishX+1) * (1/2) + self.viewPortStart[0])


		startY = int(self.vieportSize[0] * (startY+1) * (1/2) + self.viewPortStart[0])

		finishY = int(self.vieportSize[0] * (finishY+1) * (1/2) + self.viewPortStart[0])


		for x in range(startX, finishX+1):

			for y in range(startY, finishY+1):

				isInside = self.glPointInPolygon(self.norX(x), self.norY(y), vertexList)
				if isInside:

					if texture:
						A = (self.norInvX(vertexList[0][0]), self.norInvX(vertexList[0][1]))
						B = (self.norInvX(vertexList[1][0]), self.norInvX(vertexList[1][1]))
						C = (self.norInvX(vertexList[2][0]), self.norInvX(vertexList[2][1]))
						w,v,u = self.barycentric(A, B, C, x, y)
						A = textureCoords[0]
						B = textureCoords[1]
						C = textureCoords[2]
						tx = A[0] * w + B[0] * v +  C[0] * u
						ty = A[1] * w + B[1] * v + C[1] * u
						color = text.getColor(tx, ty, intensity=inten)
					z = self.glPLaneZ(vertexList, x, y)


					if z > self.imagen.getZbufferValue(x,y):

						self.imagen.point(x, y, color)
						self.imagen.setZbufferValue(x,y,z)



		#definimos barycentric
		#obtenemos todas las coordenadasd varicentricas
	def barycentric(self, A, B, C, x, y):

		v1 = (C[0]-A[0], B[0]-A[0],A[0]-x)
		v2 = (C[1]-A[1], B[1]-A[1],A[1]-y)

		bary = self.cross(v1, v2)

		if abs(bary[2])<1:

			return -1,-1,-1
		return ( 1 - (bary[0] + bary[1]) / bary[2], bary[1] / bary[2], bary[0] / bary[2])


		#normailizamos coordenada en x
	def norX(self, x):
		norX = ((2*x)/self.vieportSize[0]) - self.viewPortStart[0] - 1
		return norX

		#normalizamos coordenada en y
	def norY(self, y):
		norY = ((2*y)/self.vieportSize[1]) - self.viewPortStart[1] - 1
		return norY

	def norInvX(self, x):
		norX = int(self.vieportSize[0] * (x+1) * (1/2) + self.viewPortStart[0])
		return norX
	def norInvY(self, y):
		norY = int(self.vieportSize[0] * (y+1) * (1/2) + self.viewPortStart[0])
		return norY
	def norm(self, v0):
		v = self.length(v0)
		if not v:
			return [0,0,0]
		return [v0[0]/v, v0[1]/v, v0[2]/v]

	def length(self, v0):
		return (v0[0]**2 + v0[1]**2 + v0[2]**2)**0.5



		#vdefinimos la funcion glPointInPolygon
		#obtenemos
		#x coordenadas
		#y coordenadasd
		#guardamos en una lista

		#la funcion es para ver si un punto se encuentra dentro de un poligono
	def glPointInPolygon(self,x, y, vertexList):

		counter = 0
		p1 = vertexList[0]
		n = len(vertexList)

		for i in range(n+1):

			p2 = vertexList[i % n]
			if(y > min(p1[1], p2[1])):

				if(y <= max(p1[1], p2[1])):

					if(p1[1] != p2[1]):

						xinters = (y-p1[1])*(p2[0]-p1[0])/(p2[1]-p1[1])+p1[0]

						if(p1[0] == p2[0] or x <= xinters):

							counter += 1
			p1 = p2
		if(counter % 2 == 0):
			return False

		else:
			return True
			#obtenido de http://www.eecs.umich.edu/courses/eecs380/HANDOUTS/PROJ2/InsidePoly.html



			#obtenemos el producto punto entre dos vectores
			#v0 vector 1
			#v1 vector 2
	def dot(self, v0, v1):
		return v0[0] * v1[0] + v0[1] * v1[1] + v0[2] * v1[2]


			#obtenemos el producto cruz entre dos vectores
			#v0 vector 1
			#v1 vector 2
	def cross(self, v0, v1):
		return [v0[1] * v1[2] - v0[2] * v1[1], v0[2] * v1[0] - v0[0] * v1[2], v0[0] * v1[1] - v0[1] * v1[0]]


		#creamos un vector pq
	def vector(self, p, q):
		return [q[0]-p[0], q[1]-p[1], q[2]-p[2]]

	def sub(self, v0, v1):
		return [v0[0] - v1[0], v0[1] - v1[1], v0[2] - v1[2]]


#crear planos
#introduccion de la coordenada z
	def glPLaneZ(self, vertexList, x,y):

		pq = self.vector(vertexList[0], vertexList[1])
		pr = self.vector(vertexList[0], vertexList[2])
		normal = self.cross(pq, pr)

		if normal[2]:
			z = ((normal[0]*(x-vertexList[0][0])) + (normal[1]*(y-vertexList[0][1])) - (normal[2]*vertexList[0][2]))/(-normal[2])
			return z
		else:
			return -float("inf")


			#renderizamos el zbuffer en z
	def glRenderZBuffer(self, filename = None):

		if filename == None:
			filename = self.__filename.split(".")[0] + "ZBuffer.bmp"
		self.imagen.write(filename, zbuffer = True)



	def matMult(self, m1,m2):
		if len(m1[0]) == len(m2):
			filas1 = len(m1)
			col1 = len(m1[0])
			filas2 = len(m2)
			col2 = len(m2[0])
			matResult = []
			for i in range(filas1):
				matResult.append([0] * col2)
			for i in range(filas1):
				for j in range(col2):
					for k in range(col1):
						matResult[i][j] = m1[i][k] * m2[k][j]
			return matResult
		else:
			print("Error " + str(len(m1[0])) + " and " +str(len(m2)))
			return 0


			#generamos los model matrix
	def modelMatrix(self, translate=(0, 0, 0), scale=(1, 1, 1), rotate=(0, 0, 0)):
		translation_matrix = Matrix([[1, 0, 0, translate[0]],[0, 1, 0, translate[1]],[0, 0, 1, translate[2]],[0, 0, 0, 1],])
		a = rotate[0]
		rotation_matrix_x = Matrix([[1, 0, 0, 0],[0, cos(a), -sin(a), 0],[0, sin(a),  cos(a), 0],[0, 0, 0, 1]])
		a = rotate[1]
		rotation_matrix_y = Matrix([[cos(a), 0,  sin(a), 0],[     0, 1,       0, 0],[-sin(a), 0,  cos(a), 0],[     0, 0,       0, 1]])
		a = rotate[2]
		rotation_matrix_z = Matrix([[cos(a), -sin(a), 0, 0],[sin(a),  cos(a), 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])
		rotation_matrix = rotation_matrix_x * rotation_matrix_y * rotation_matrix_z
		scale_matrix = Matrix([[scale[0], 0, 0, 0],[0, scale[1], 0, 0],[0, 0, scale[2], 0],[0, 0, 0, 1],])
		self.Model = translation_matrix * rotation_matrix * scale_matrix
		#generamos view matrix
	def viewMatrix(self, x, y, z, center):
		m = Matrix([[x[0], x[1], x[2],  0],[y[0], y[1], y[2], 0],[z[0], z[1], z[2], 0],[0,0,0,1]])
		o = Matrix([[1, 0, 0, -center[0]],[0, 1, 0, -center[1]],[0, 0, 1, -center[2]],[0, 0, 0, 1]])
		self.View = m * o
		#generamos projection matrix
	def projectionMatrix(self, coeff):
		self.Projection = Matrix([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, coeff, 1]])
		#generamos vieport matrix
	def viewportMatrix(self, x=0, y =0):
		self.Viewport =  Matrix([[self.imagen.width/2, 0, 0, x + self.imagen.width/2],[0, self.imagen.height/2, 0, y + self.imagen.height/2],[0, 0, 128, 128],[0, 0, 0, 1]])
		#posicion de la camara
	def lookAt(self, eye, center, up):
		z = self.norm(self.sub(eye, center))
		x = self.norm(self.cross(up, z))
		y = self.norm(self.cross(z,x))
		self.viewMatrix(x, y, z, center)
		self.projectionMatrix(-1/self.length(self.sub(eye, center)))
		self.viewportMatrix()
		#transformaciones de matrices
	def transform(self, vertex):
		agv = Matrix([[vertex[0]],[vertex[1]],[vertex[2]],[1]])
		transformed_vertex = self.Viewport * self.Projection * self.View * self.Model * agv
		transformed_vertex = transformed_vertex.tolist()
		tra = [round(transformed_vertex[0][0]/transformed_vertex[3][0]), round(transformed_vertex[1][0]/transformed_vertex[3][0]), round(transformed_vertex[2][0]/transformed_vertex[3][0])]
		return tra

#creamos la clase Matrix
class Matrix(object):
	def __init__(self, data):
		self.data = data
		self.row = len(data)
		self.col = len(data[0])


#multiplicacion de las matrices
	def __mul__(self, m2):
		result = []
		for i in range(self.row):
			result.append([])
			for j in range(m2.col):
				result[-1].append(0)

		for i in range(self.row):
			for j in range(m2.col):
				for k in range(m2.row):
					result[i][j] += self.data[i][k] * m2.data[k][j]

		return Matrix(result)

	def tolist(self):
		return self.data
