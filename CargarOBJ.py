""" universidad del Valle de Guatemala
	Graficas por Computadora
	Alexis Fernando Hengstenberg Chocooj
	Carnet: 17699
	clase CargarOBJ
"""
#importamos librerias

#libreria para abrir archivos en distintas carpetas.
import os



#cargar el archvo.obj
class CargarOBJ(object):


#constructor
#filname (para mandar el nombre del archivo)
	def __init__(self, filename):
		self.vertex = []
		self.caras = []
		self.nvertex = []
		self.nombre = filename
		self.materiales = None
		self.materialesCaras = []
		self.tvertex = []




#cargamos el archivo con el nombre que mandamos
	def load(self):
#abrimos el archivo
#solo para lectura de datos
		file = open(self.nombre, "r")



		#lista para guardar las caras
		faces = []
		currentMat, previousMat = "default", "default"

		#contador de cargados
		contadorCaras = 0
		matIndex = []

		#lista para leer linea por linea
		lines = file.readlines()
		last = lines[-1]

		#for para leer todas las lineas y guardarlas
		for line in lines:
			#separar las lineas por un espacion
			line = line.rstrip().split(" ")
			#archivo mtl de __material
			if line[0] == "mtllib":
				#materiales
				mtlFile = MTL(os.path.dirname(file.name) + "/" + line[1])
				if mtlFile.isFileOpened():
					mtlFile.load()
					#self.caras = {}
					self.materiales = mtlFile.materials
				else:
					self.caras = []
			elif line[0] == "usemtl":
				if self.materiales:
					matIndex.append(contadorCaras)
					previousMat = currentMat
					currentMat = line[1]
					if len(matIndex) == 2:
						self.materialesCaras.append((matIndex, previousMat))
						matIndex= [matIndex[1]+1]
			#agregamos los vertices



			#para cada uno de las caras
			elif line[0] == "v":
				line.pop(0)
				i = 1 if line[0] == "" else 0
				self.vertex.append((float(line[i]), float(line[i+1]), float(line[i+2])))
			#vector normal
			elif line[0] == "vn":
				line.pop(0)
				i = 1 if line[0] == "" else 0
				self.nvertex.append((float(line[i]), float(line[i+1]), float(line[i+2])))

			#obtenemos las caras
			#guardamos en una lista
			elif line[0] == "f":
				line.pop(0)
				face = []
				for i in line:
					#separamos por un /
					i = i.split("/")
					if i[1] == "":
						face.append((int(i[0]), int(i[-1])))
					else:
						face.append((int(i[0]), int(i[-1]), int(i[1])))
				self.caras.append(face)
				contadorCaras += 1
				face = []
				#obtenemos vt
			elif line[0] == "vt":
				line.pop(0)
				self.tvertex.append((float(line[0]), float(line[1])))
		if len(matIndex) < 2 and self.materiales:
			matIndex.append(contadorCaras)
			self.materialesCaras.append((matIndex, currentMat))
			matIndex= [matIndex[1]+1]
		file.close()





#obtenemos los materiales
	def getMaterials(self):
		return self.materiales
#obtenemos la textura.
	def getTextureVertex(self):
		return self.tvertex
#obtenemos la lista de los materiales
	def getFaceList(self):
		return self.caras
#obtenemos el material de cada una de las caras
	def getMaterialFaces(self):
		return self.materialesCaras
#obtenemos los vertex
	def getVertexList(self):
		return self.vertex
#obtenemos el vector normal
	def getVertexNormalList(self):
		return self.nvertex








#cremos la segunda clase MTL para encontrar los materiales.
class MTL(object):


	def __init__(self, filename):
		#seclaramos las variables
		self.nombre = filename
		self.__file = None
		self.materials = {}
		self.readMTLFile()

		#leemos el archivo .mtl
	def readMTLFile(self):
		try:
			#abrimos y leemos el archivo
			#solo leectura
			self.__file = open(self.nombre, "r")
			self.__mtlFile = True
		except:
			self.__mtlFile = False


			#obtenemos los vertices
	def isFileOpened(self):

		return self.__mtlFile

			#obtenemos los materiales del mtl
	def load(self):

		#abrimos
		if self.isFileOpened():
			currentMat = None
			ac, dc, sc, ec, t, s, i, o = 0, 0, 0, 0, 0, 0, 0, 0
			for line in self.__file.readlines():

				#separamos por medio de espacions
				line = line.strip().split(" ")


				#obtenemos los materiales por sus siglas al principio de cada linea.
				if line[0] == "newmtl":
					currentMat = line[1].rstrip()
				elif line[0] == "Ka":
					ac = (float(line[1]), float(line[2]), float(line[3]))
				elif line[0] == "Kd":
					dc = (float(line[1]), float(line[2]), float(line[3]))
				elif line[0] == "Ks":
					sc = (float(line[1]), float(line[2]), float(line[3]))
				elif line[0] == "Ke":
					ec = (float(line[1]), float(line[2]), float(line[3]))
				elif line[0] == "d" or line[0] == "Tr":
					t = (float(line[1]), line[0])
				elif line[0] == "Ns":
					s = float(line[1])
				elif line[0] == "illum":
					i  = int(line[1])
				elif line[0] == "Ni":
					o = float(line[1])
				elif currentMat:
					self.materials[currentMat] = Material(currentMat, ac, dc, sc, ec, t, s, i, o)
			if currentMat not in self.materials.keys():
				self.materials[currentMat] = Material(currentMat, ac, dc, sc, ec, t, s, i, o)


#enviamos los tipos de materiales
class Material(object):

	def __init__(self, name, ac, dc, sc, ec, t, s, i, o):


		#nombre dle material
		self.name = name.rstrip()

		#color amiente
		self.ambientColor = ac

		#difuse color material
		self.difuseColor = dc

		#color especular material
		self.specularColor = sc

		#emissive coeficiente material
		self.emissiveCoeficient = ec

		#material de transparencia
		self.transparency = t

		#maetrial de shininess
		self.shininess = s

		#iluminacion
		self.illumination = i

		#densidad optica material
		self.opticalDensity = o
