from app.core.database import Database
from app.models.estudiante import Estudiante

class EstudianteRepository:
    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM estudiante ORDER BY id ASC;")
            estudiantes = cursor.fetchall()
            return estudiantes
        except Exception as e:
            print(f"❌ Error al obtener estudiantes: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def obtener_por_id(self, estudiante_id: int):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM estudiante WHERE id = %s;", (estudiante_id,))
            estudiante = cursor.fetchone()
            return estudiante
        except Exception as e:
            print(f"❌ Error al obtener estudiante: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def crear(self, estudiante: Estudiante):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO estudiante (usuario_id, codigo_estudiante, grado) 
                VALUES (%s, %s, %s) RETURNING id;
            """
            cursor.execute(query, (estudiante.usuario_id, estudiante.codigo_estudiante, estudiante.grado))
            nuevo_id = cursor.fetchone()['id']
            conn.commit()
            return nuevo_id
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al crear estudiante: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def actualizar(self, estudiante_id: int, estudiante: Estudiante):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = """
                UPDATE estudiante 
                SET usuario_id = %s, codigo_estudiante = %s, grado = %s
                WHERE id = %s
                RETURNING id;
            """
            cursor.execute(query, (estudiante.usuario_id, estudiante.codigo_estudiante, estudiante.grado, estudiante_id))
            actualizado = cursor.fetchone()
            conn.commit()
            return actualizado is not None
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al actualizar estudiante: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def eliminar(self, estudiante_id: int):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM estudiante WHERE id = %s RETURNING id;", (estudiante_id,))
            eliminado = cursor.fetchone()
            conn.commit()
            return eliminado is not None
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al eliminar estudiante: {e}")
            raise
        finally:
            if conn:
                conn.close()