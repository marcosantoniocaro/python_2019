from Estructura import *
nuevo(0,"inicio");
#################################################################
def Ej_ya_hechos():
	#Con tab colocaremos aqui las prácticas hechas
	pass
print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                     CLASES                                  ║
║                                    --------                                 ║
║                                                                             ║
║          __init__(self, ...)                                                ║
║              This method is called just before the newly created object is  ║
║              returned for usage.                                            ║
║                                                                             ║
║          __del__(self)                                                      ║
║              Called just before the object is destroyed (which has          ║
║              unpredictable timing, so avoid using this)                     ║
║                                                                             ║
║          __str__(self)                                                      ║
║              Called when we use the print function or when str() is used.   ║
║                                                                             ║
║          __lt__(self, other)                                                ║
║              Called when the less than operator (<) is used. Similarly,     ║
║               there are special methods for all the operators (+, >, etc.)  ║
║                                                                             ║
║          __getitem__(self, key)                                             ║
║              Called when x[key] indexing operation is used.                 ║
║                                                                             ║
║          __len__(self)                                                      ║
║              Called when the built-in len() function is used for            ║
║              the sequence object.                                           ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                           Objetos                                           ║
║                                  self.                                      ║
║                                                                             ║
║                           Clases                                            ║
║                                  Atributos (del objeto)                     ║
║                                  métodos (funciones del objeto)             ║
║                                                                             ║
║                           Constructor                                       ║
║                                  __init__                                   ║
║                                  __str__                                    ║
║                                                                             ║
║                           Class (object) Padre                              ║
║                                                                             ║
║                           Objetos                  	                      ║
║                                  estado                                     ║
║                                  propiedades                                ║
║                                  comportamiento                             ║
║                                                                             ║
║                           Instancia                                         ║
║                                                                             ║
║                           Modularizacion                                    ║
║                                                                             ║
║                           Encapsulado                                       ║
║                               _oculta                                       ║
║                               __privada                                     ║
║                                                                             ║
║                           Herencia Simple y múltiple                        ║
║                           	Orden de herencia                             ║
║                               super()                                       ║
║                               isinstance                                    ║
║                                                                             ║
║                           Polimorfismo                                      ║
║                                                                             ║
║                           Abstracción                                       ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
Para crear objetos - instanciar llamamos a una clase.
Un constructor es un método especial que Python llama para instanciar un objeto usando las definiciones encontradas en tu clase.
Python usa este constructor para crear tareas como la inicialización (asignar valores a variables), que se necesiten para iniciar.
Los constructores también pueden verificar que hay suficientes recursos para que el objecto desempeñe cualquier otra tarea para iniciar.
El método __init__ es el encargado de construir - inicializar una serie de atributos y ejecutar el código que le definamos al momento de que se cree un objeto de la clase, al ser llamado “__init__” con dos guiones bajos al inicio y final de la palabra init posee la sintaxis adecuada para que Python lo tome como un método "autoinicio" y  debe ejecutarse al momento de hacer una instancia de la clase
El constructor acepta argumentos, como minimo un Self, que es el nombre del objeto cuando es necesario crear o construirlo.
Tipos de constructores :
    default constructor :The default constructor is simple constructor which doesn’t accept any arguments.It’s definition has only one argument which is a reference to the instance being constructed.
    parameterized constructor :constructor with parameters is known as parameterized constructor.The parameterized constructor take its first argument as a reference to the instance being constructed known as self and the rest of the arguments are provided by the programmer.

""");
nuevo(0,"inicio");
##################################################################################################################################
#Ejercicio_Clases_01
class Para_Construir_objetos:
	def __init__(self):#pasa por aquí el nombre del objeto
		'''pasa por aquí el nombre del objeto'''
		self.ojos=2
		self.piernas=2
		self.pies=2
		self.color_sangre="roja"
		self.respirar=True
		self.comer=True
		self.dormir=True
		self.trabajar=False

	def __str__(self):
		return  f"Nombre de la clase:{self.__class__.__name__}\n" \
				f"ojos\t {self.ojos}\n" \
				f"piernas\t\t {self.piernas}\n" \
				f"pies\t\t {self.pies}\n" \
				f"color_sangre\t {self.color_sangre}\n" \
				f"Puede respirar\t\t {self.respirar}\n" \
				f"Puede comer\t\t {self.comer}\n" \
				f"Puede dormir\t\t {self.dormir}\n" \
				f"Puede trabajar\t\t {self.trabajar}\n" \



objeto_1=Para_Construir_objetos()

print(f" posee las siguientes características:\n\t\t {str(objeto_1)}")

nuevo(1);
##################################################################################################################################
#Ejercicio_Clases_02
class Constructor_Familia:
	"""
	╔══════════════════════════════╗
	║        Clase Familia         ║
	╚══════════════════════════════╝"""

	def __init__(self,padre,madre,hijos=[]):
		self.padre=padre
		self.madre=madre
		self.hijos=hijos
	def __str__(self):
		cadena="Padre:"+self.padre+","+"Madre:"+self.madre
		for hi in self.hijos:
			cadena=cadena+","+"Hijo:"+hi
		return cadena

familia1=Constructor_Familia("Jorge","Carla",["Marcelo","Pedro"])
familia2=Constructor_Familia(madre="Carla",padre="Jorge")
familia3=Constructor_Familia(madre="Carla",hijos=["Marcelo","Pedro"],padre="Jorge")

print(familia1)
print(familia2)
print(familia3)
print(familia3.__doc__)
"""
print("Constructor_Familia");print(dir(Constructor_Familia))
print("Constructor_Familia");print(dir({Constructor_Familia}))
print("familia3");print(dir(familia3))
print("familia3");print(dir({familia3}))
print(Constructor_Familia.__dict__.items())
"""
nuevo(2);
##################################################################################################################################
#Ejercicio_Clases_03
class Mascota:
	def __init__(self,nombre, especie=None, raza=None, patas=4,  edad=None):
		self.nombre=nombre;
		self.especie=especie;
		self.raza=raza;
		self.patas=patas;
		self.edad=edad;
	def nombrar(self, dato_nombre):
		self.nombre =dato_nombre;
	def datar(self,especie=None, raza=None, patas=4, nombre=None, edad=None):
		self.especie=especie;
		self.raza=raza;
		self.patas=patas;
		self.nombre=nombre;
		self.edad=edad;
perro= Mascota("Wanda","Can","Weimaraner",4,6)
gato1= Mascota("Manchas","Felino","calle",4,5)
gato2 =Mascota("Grey")
print (f"Mi 1ra mascota stiene las sig caracteristicas: ",perro.especie,perro.raza,perro.patas,perro.nombre,perro.edad);
print (f"Mi 2da mascota stiene las sig caracteristicas: ",gato1.especie,gato1.raza,gato1.patas,gato1.nombre,gato1.edad);
print (f"Mi 2da mascota stiene las sig caracteristicas: ",gato2.especie,gato2.raza,gato2.patas,gato2.nombre,gato2.edad);
gato2.datar (nombre="Grey", especie="Felino", raza="calle", patas=4,  edad=2)
print (f"Mi 2da mascota stiene las sig caracteristicas: ",gato2.especie,gato2.raza,gato2.patas,gato2.nombre,gato2.edad);

gato2.datar (nombre="Grey", especie="Felino", raza="angora", patas=8,  edad=2)
print (f"Mi 2da mascota stiene las sig caracteristicas: ",gato2.especie,gato2.raza,gato2.patas,gato2.nombre,gato2.edad);

limpiar();
#################################################################
