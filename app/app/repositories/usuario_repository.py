from app.core.database import Database
from app.models.usuario import Usuario

class UsuarioRepository:
    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario ORDER BY id ASC;")
            usuarios = cursor.fetchall()
            return usuarios
        except Exception as e:
            print(f"❌ Error al obtener usuarios: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def obtener_por_id(self, usuario_id: int):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario WHERE id = %s;", (usuario_id,))
            usuario = cursor.fetchone()
            return usuario
        except Exception as e:
            print(f"❌ Error al obtener usuario: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def crear(self, usuario: Usuario):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO usuario (nombre, correo, password, rol_id) 
                VALUES (%s, %s, %s, %s) RETURNING id;
            """
            cursor.execute(query, (usuario.nombre, usuario.correo, usuario.password, usuario.rol_id))
            nuevo_id = cursor.fetchone()['id']
            conn.commit()
            return nuevo_id
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al crear usuario: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def actualizar(self, usuario_id: int, usuario: Usuario):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = """
                UPDATE usuario 
                SET nombre = %s, correo = %s, password = %s, rol_id = %s
                WHERE id = %s
                RETURNING id;
            """
            cursor.execute(query, (usuario.nombre, usuario.correo, usuario.password, usuario.rol_id, usuario_id))
            actualizado = cursor.fetchone()
            conn.commit()
            return actualizado is not None
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al actualizar usuario: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def eliminar(self, usuario_id: int):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM usuario WHERE id = %s RETURNING id;", (usuario_id,))
            eliminado = cursor.fetchone()
            conn.commit()
            return eliminado is not None
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al eliminar usuario: {e}")
            raise
        finally:
            if conn:
                conn.close()