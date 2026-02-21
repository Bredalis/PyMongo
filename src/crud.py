
import pymongo
from bson import ObjectId

class CRUD:
	def __init__(self):
		"""Inicializa la conexión con la bbdd de MongoDB."""
		try:
			self.cliente = pymongo.MongoClient("PON TU URL")
			self.db = self.cliente["Escuela"]
			self.coleccion = self.db["Alumnos"]
		
		except pymongo.errors.ConnectionFailure as error_conexion:
			print(f"Error al conectarse a MongoDB: {error_conexion}")
			self.cliente = None
	 
	def insertar_datos(self):
		"""Inserta un documento nuevo a la colección."""
		if not self.cliente:
			print("Conexión no establecida.")
			return
		try:
			documento = {
				"Nombre": "Lisa", 
				"Sexo": "Femenina", 
				"Calificacion": 10
			}
			self.coleccion.insert_one(documento)
		
		except pymongo.errors.PyMongoError as e:
			print(f"Error al insertar datos: {e}")
		finally:
			self.cerrar_conexion()

	def crear_consulta(self):
		"""Consulta y muestra los documentos donde el nombre es 'Juan'."""
		if not self.cliente:
			print("Conexión no establecida.")
			return
		try:
			for documento in self.coleccion.find({"Nombre": "Juan"}):
				print(documento)
		
		except pymongo.errors.PyMongoError as e:
			print(f"Error al crear consulta: {e}")
		finally:
			self.cerrar_conexion()

	def leer_documentos(self):
		"""Lee y muestra todos los documentos en la colección."""
		if not self.cliente:
			print("Conexión no establecida.")
			return
		try:
			for documento in self.coleccion.find():
				print("Nombre:", documento.get("Nombre"), "Sexo:", documento.get("Sexo"), 
					"Calificación:", documento.get("Calificacion"))
		
		except pymongo.errors.PyMongoError as e:
			print(f"Error al leer documentos: {e}")
		finally:
			self.cerrar_conexion()

	def buscar(self):
		"""Busca documentos que coincidan con los criterios proporcionados."""
		if not self.cliente:
			print("Conexión no establecida.")
			return
		try:
			criterios_busqueda = {"Nombre": "Lisa", "Sexo": "Femenino"}
			for documento in self.coleccion.find(criterios_busqueda):
				print(documento)
		
		except pymongo.errors.PyMongoError as e:
			print(f"Error al buscar colecciones: {e}")
		finally:
			self.cerrar_conexion()

	def actualizar(self):
		"""Actualiza un documento basado en su ID."""
		if not self.cliente:
			print("Conexión no establecida.")
			return
		try:
			filtro = {"_id": ObjectId("6532537798c4f4853acfafe2")}
			nuevos_datos = {
				"$set": {
					"Nombre": "Juan", 
					"Sexo": "Masculino", 
					"Calificacion": 7
				}
			}
			resultado = self.coleccion.update_one(filtro, nuevos_datos)
			if resultado.matched_count == 0:
				print("No se encontró el documento para actualizar.")
		
		except pymongo.errors.PyMongoError as e:
			print(f"Error al actualizar colecciones: {e}")
		finally:
			self.cerrar_conexion()
	
	def borrar(self):
		"""Elimina un documento que coincida con el criterio proporcionado."""
		if not self.cliente:
			print("Conexión no establecida.")
			return
		try:
			criterio_borrado = {"Nombre": "Juan"}
			resultado = self.coleccion.delete_one(criterio_borrado)
			if resultado.deleted_count == 0:
				print("No se encontró el documento para eliminar.")
		
		except pymongo.errors.PyMongoError as e:
			print(f"Error al borrar colección: {e}")
		finally:
			self.cerrar_conexion()

	def cerrar_conexion(self):
		"""Cierra la conexión con la base de datos."""
		if self.cliente:
			self.cliente.close()
			print("Conexión cerrada.")