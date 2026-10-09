from app.core.database import Database
from app.models.autorizacion import Autorizacion
from datetime import date

class AutorizacionRepository:
    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM autorizacion ORDER BY id ASC;")
            autorizaciones = cursor.fetchall()
            return autorizaciones
        except Exception as e:
            print(f"❌ Error al obtener autorizaciones: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def obtener_por_id(self, autorizacion_id: int):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM autorizacion WHERE id = %s;", (autorizacion_id,))
            autorizacion = cursor.fetchone()
            return autorizacion
        except Exception as e:
            print(f"❌ Error al obtener autorización: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def crear(self, autorizacion: Autorizacion):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            fecha_actual = date.today()
            query = """
                INSERT INTO autorizacion (inscripcion_id, acudiente_id, estado, fecha_autorizacion) 
                VALUES (%s, %s, %s, %s) RETURNING id;
            """
            cursor.execute(query, (
                autorizacion.inscripcion_id, 
                autorizacion.acudiente_id, 
                autorizacion.estado,
                fecha_actual
            ))
            nuevo_id = cursor.fetchone()['id']
            conn.commit()
            return nuevo_id
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al crear autorización: {e}")
            raise
        finally:
            if conn:
                conn.close()

    # ✅ CORREGIDO: Ahora incluye fecha_autorizacion
    def actualizar(self, autorizacion_id: int, autorizacion: Autorizacion):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = """
                UPDATE autorizacion 
                SET inscripcion_id = %s, acudiente_id = %s, estado = %s, fecha_autorizacion = %s
                WHERE id = %s
                RETURNING id;
            """
            cursor.execute(query, (
                autorizacion.inscripcion_id, 
                autorizacion.acudiente_id, 
                autorizacion.estado,
                autorizacion.fecha_autorizacion,
                autorizacion_id
            ))
            actualizado = cursor.fetchone()
            conn.commit()
            return actualizado is not None
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al actualizar autorización: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def eliminar(self, autorizacion_id: int):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM autorizacion WHERE id = %s RETURNING id;", (autorizacion_id,))
            eliminado = cursor.fetchone()
            conn.commit()
            return eliminado is not None
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al eliminar autorización: {e}")
            raise
        finally:
            if conn:
                conn.close()