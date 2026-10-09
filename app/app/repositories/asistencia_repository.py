from app.core.database import Database
from app.models.asistencia import Asistencia

class AsistenciaRepository:
    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM asistencia ORDER BY id ASC;")
            asistencias = cursor.fetchall()
            return asistencias
        except Exception as e:
            print(f"❌ Error al obtener asistencias: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def obtener_por_id(self, asistencia_id: int):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM asistencia WHERE id = %s;", (asistencia_id,))
            asistencia = cursor.fetchone()
            return asistencia
        except Exception as e:
            print(f"❌ Error al obtener asistencia: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def crear(self, asistencia: Asistencia):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO asistencia (inscripcion_id, asistio, observacion) 
                VALUES (%s, %s, %s) RETURNING id;
            """
            cursor.execute(query, (
                asistencia.inscripcion_id, 
                asistencia.asistio, 
                asistencia.observacion
            ))
            nuevo_id = cursor.fetchone()['id']
            conn.commit()
            return nuevo_id
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al crear asistencia: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def actualizar(self, asistencia_id: int, asistencia: Asistencia):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = """
                UPDATE asistencia 
                SET inscripcion_id = %s, asistio = %s, observacion = %s
                WHERE id = %s
                RETURNING id;
            """
            cursor.execute(query, (
                asistencia.inscripcion_id, 
                asistencia.asistio, 
                asistencia.observacion,
                asistencia_id
            ))
            actualizado = cursor.fetchone()
            conn.commit()
            return actualizado is not None
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al actualizar asistencia: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def eliminar(self, asistencia_id: int):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM asistencia WHERE id = %s RETURNING id;", (asistencia_id,))
            eliminado = cursor.fetchone()
            conn.commit()
            return eliminado is not None
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al eliminar asistencia: {e}")
            raise
        finally:
            if conn:
                conn.close()