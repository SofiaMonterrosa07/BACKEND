from app.core.database import Database
from app.models.inscripcion import Inscripcion
from datetime import date

class InscripcionRepository:
    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM inscripcion ORDER BY id ASC;")
            inscripciones = cursor.fetchall()
            return inscripciones
        except Exception as e:
            print(f"❌ Error al obtener inscripciones: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def obtener_por_id(self, inscripcion_id: int):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM inscripcion WHERE id = %s;", (inscripcion_id,))
            inscripcion = cursor.fetchone()
            return inscripcion
        except Exception as e:
            print(f"❌ Error al obtener inscripción: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def crear(self, inscripcion: Inscripcion):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            fecha_actual = date.today()
            query = """
                INSERT INTO inscripcion (estudiante_id, actividad_id, fecha_inscripcion, estado) 
                VALUES (%s, %s, %s, %s) RETURNING id;
            """
            cursor.execute(query, (
                inscripcion.estudiante_id, 
                inscripcion.actividad_id, 
                fecha_actual, 
                inscripcion.estado
            ))
            nuevo_id = cursor.fetchone()['id']
            conn.commit()
            return nuevo_id
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al crear inscripción: {e}")
            raise
        finally:
            if conn:
                conn.close()

    # ✅ CORREGIDO: Ahora incluye fecha_inscripcion
    def actualizar(self, inscripcion_id: int, inscripcion: Inscripcion):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = """
                UPDATE inscripcion 
                SET estudiante_id = %s, actividad_id = %s, fecha_inscripcion = %s, estado = %s
                WHERE id = %s
                RETURNING id;
            """
            cursor.execute(query, (
                inscripcion.estudiante_id, 
                inscripcion.actividad_id, 
                inscripcion.fecha_inscripcion,
                inscripcion.estado,
                inscripcion_id
            ))
            actualizado = cursor.fetchone()
            conn.commit()
            return actualizado is not None
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al actualizar inscripción: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def eliminar(self, inscripcion_id: int):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM inscripcion WHERE id = %s RETURNING id;", (inscripcion_id,))
            eliminado = cursor.fetchone()
            conn.commit()
            return eliminado is not None
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al eliminar inscripción: {e}")
            raise
        finally:
            if conn:
                conn.close()