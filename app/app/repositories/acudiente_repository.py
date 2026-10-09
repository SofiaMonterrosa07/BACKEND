from app.core.database import Database
from app.models.acudiente import Acudiente

class AcudienteRepository:
    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM acudiente ORDER BY id ASC;")
            acudientes = cursor.fetchall()
            return acudientes
        except Exception as e:
            print(f"❌ Error al obtener acudientes: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def obtener_por_id(self, acudiente_id: int):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM acudiente WHERE id = %s;", (acudiente_id,))
            acudiente = cursor.fetchone()
            return acudiente
        except Exception as e:
            print(f"❌ Error al obtener acudiente: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def crear(self, acudiente: Acudiente):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO acudiente (usuario_id, documento, telefono, parentesco) 
                VALUES (%s, %s, %s, %s) RETURNING id;
            """
            cursor.execute(query, (
                acudiente.usuario_id,
                acudiente.documento,
                acudiente.telefono,
                acudiente.parentesco
            ))
            nuevo_id = cursor.fetchone()['id']
            conn.commit()
            return nuevo_id
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al crear acudiente: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def actualizar(self, acudiente_id: int, acudiente: Acudiente):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = """
                UPDATE acudiente 
                SET usuario_id = %s, documento = %s, telefono = %s, parentesco = %s
                WHERE id = %s
                RETURNING id;
            """
            cursor.execute(query, (
                acudiente.usuario_id,
                acudiente.documento,
                acudiente.telefono,
                acudiente.parentesco,
                acudiente_id
            ))
            actualizado = cursor.fetchone()
            conn.commit()
            return actualizado is not None
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al actualizar acudiente: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def eliminar(self, acudiente_id: int):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM acudiente WHERE id = %s RETURNING id;", (acudiente_id,))
            eliminado = cursor.fetchone()
            conn.commit()
            return eliminado is not None
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al eliminar acudiente: {e}")
            raise
        finally:
            if conn:
                conn.close()