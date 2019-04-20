""" universidad del Valle de Guatemala
	Graficas por Computadora
	Alexis Fernando Hengstenberg Chocooj
	Carnet: 17699
	clase Texturas
"""
#importamos las librerias

#libreria de bmp
from BMP import *


#creamos la clase Texturas
class Texture(object):

	#obtenemos el nombre
	def __init__(self, filename):

		self.nombre = filename
		self.texto = None

		#cargamos el archivo
		self.load()



#    def read(self):
#        image = open(self.path, "rb")
#
#        # we ignore all the header stuff
#
#        image.seek(2 + 4 + 4)  # skip BM, skip bmp size, skip zeros
#
#        header_size = struct.unpack("=l", image.read(4))[0]  # read header size
#        image.seek(2 + 4 + 4 + 4 + 4)
#
#
#
#        self.width = struct.unpack("=l", image.read(4))[0]  # read width
#        self.height = struct.unpack("=l", image.read(4))[0]  # read width
#        self.pixels = []
#
#        image.seek(header_size)
#        for y in range(self.height):
#
#            self.pixels.append([])
#            for x in range(self.width):
#
#                b = ord(image.read(1))
#                g = ord(image.read(1))
#                r = ord(image.read(1))
#                self.pixels[y].append(color(r,g,b))
#        image.close()




	def load(self):


		self.texto = BMP(0, 0)
		try:
			self.texto.load(self.nombre)



		except:
			self.texto = None
			#colorblanco
	def write(self):
		self.texto.write(self.nombre[:len(self.nombre)-4]+"text.bmp")


		#texturas
	def isTextured(self):


		return True if self.texto else False
		#color

#
#    def get_color(self, tx, ty, intensity=1):
#
#        x = int(tx * self.width)
#        y = int(ty * self.height)
#
#        try:
#            return bytes(map(lambda b: round(b*intensity) if b*intensity > 0 else 0, self.pixels[y][x]))
#        except:
#            pass


	def getColor(self, tx, ty, intensity=1):


		x = self.texto.width -1 if ty == 1 else int(ty*self.texto.width)


		y = self.texto.height -1 if tx == 1 else int(tx*self.texto.height)

		#retornamos
		return bytes(map(lambda b: round(b*intensity) if b*intensity > 0 else 0, self.texto.framebuffer[y][x]))
