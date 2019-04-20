""" universidad del Valle de Guatemala
	Graficas por Computadora
	Alexis Fernando Hengstenberg Chocooj
	Carnet: 17699
	clase BMP
	SoftwareRender
"""


#llamamos a las librerias

#libreria para estructurar los datos.
import struct
#libreria para abrir archivos en distintas carpetas.
import os

#creamos la clase BMP que utilizaremos para crear los bmp
#clase de tipo bitmap
#width = Ancho
#height= largo
class BMP(object):
		#todos los valores se crearan en negro.
		def __init__(self, width, height):

			self.width = abs(int(width))
			self.height = abs(int(height))
			self.framebuffer = []
			self.zbuffer = []
			self.clear()


#limpiar el bitmap de un solo color.
		def clear(self, r=0, b=0, g=0):
			self.framebuffer = [
				[
					self.color(r, b, g)
						for x in range(self.width)
				]
				for y in range(self.height)
			]

			self.zbuffer = [ [-float('inf') for x in range(self.width)] for y in range(self.height)]



#creamos los colores por RGB por medio de bytes
#0 a 255
#si la entrada no es correcta se colocara en blanco automatico.

		def color(self, r=0, g=0, b=0):

#entrada incorrecta
			if (r > 255 or g > 255 or b > 255 or r < 0 or g < 0 or b <0):
				r = 1
				g = 1
				b = 1
			#el color sera blanco

			#retornamos bytes de rgb
			return bytes([b, g, r])




#crea un punto en una cordenada que se le envia
		def point(self, x, y, color):
			if(x < self.width and y < self.height):
				try:
					self.framebuffer[x][y] = color
				except Exception as e:
					pass


#escribimos el mbp
		def write(self, filename, zbuffer=False):

			#color negro
			BLACK = self.color(0,0,0)

			os.makedirs(os.path.dirname(filename), exist_ok=True)
			file = open(filename, "bw")
			pWidth =  self.__padding(4, self.width)
			pHeight = self.__padding(4, self.height)
			#Header de archivo
			file.write(self.__char("B"))
			file.write(self.__char("M")) #BM
			file.write(self.___dword(14 + 40 + pWidth * pHeight))
			file.write(self.___dword(0))
			file.write(self.___dword(14 + 40))
			file.write(self.___dword(40))
			file.write(self.___dword(self.width))
			file.write(self.___dword(self.height))
			file.write(self.___word(1))
			file.write(self.___word(24))
			file.write(self.___dword(0))
			file.write(self.___dword(pWidth * pHeight))
			file.write(self.___dword(0))
			file.write(self.___dword(0))
			file.write(self.___dword(0))
			file.write(self.___dword(0))
			for x in range(pWidth):
				for y in range(self.height):
					if(x < self.width and y < self.height):
						if zbuffer:
							if self.zbuffer[y][x] == -float("inf"):
								file.write(BLACK)
							else:
								z = abs(int(self.zbuffer[y][x]*255))
								file.write(self.color(z,z,z))
						else:
							file.write(self.framebuffer[y][x])
					else:
						file.write(self.__char("c"))
			file.close()


#cargamos el nombre
		def load(self, filename):
			file = open(filename, "rb")
			file.seek(10)
			headerSize = struct.unpack("=l", file.read(4))[0]
			file.seek(18)
			#altura
			self.width = struct.unpack("=l", file.read(4))[0]
			#anchura
			self.height = struct.unpack("=l", file.read(4))[0]
			self.clear()
			for y in range(self.height):
				for x in range(self.width):
					if x < self.width and y < self.height:
						b, g, r = ord(file.read(1)), ord(file.read(1)), ord(file.read(1))
						self.point(x, y, self.color(r,g,b))
			file.close()

			#pading a un numero
		def __padding(self, base, c):
			if(c %  base == 0):
				return c
			else:
				while (c % base):
					c += 1
				return c



#-------------------Helpfull-----------
		def __char(self, c):
			#caracter ascii
			return struct.pack("c", c.encode("ascii"))

		def ___word(self, c):
			return struct.pack("h", c)

		def ___dword(self, c):
			return struct.pack("l", c)

			#tener el valor de x y para las cordenadas del zbuffer
		def getZbufferValue(self, x, y):
			if x < self.width and y < self.height:
				return self.zbuffer[x][y]
			else:
				return -float("inf")

		def setZbufferValue(self, x, y, z):
			if x < self.width and y < self.height:
				self.zbuffer[x][y] = z
				return 1
			else:
				return 0

#--------------------------------------
