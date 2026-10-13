from app.core.database import Database
from app.models.configuracion import Configuracion

class ConfiguracionRepository:
    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM configuracion ORDER BY id ASC;")
            return cursor.fetchall()
        except Exception as e:
            print(f"❌ Error al obtener configuraciones: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def obtener_por_id(self, configuracion_id: int):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM configuracion WHERE id = %s;", (configuracion_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"❌ Error al obtener configuración: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def obtener_por_clave(self, clave: str):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM configuracion WHERE clave = %s;", (clave,))
            return cursor.fetchone()
        except Exception as e:
            print(f"❌ Error al obtener configuración por clave: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def crear(self, configuracion: Configuracion):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO configuracion (clave, valor, descripcion, estado, creado, actualizado) 
                VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;
            """
            cursor.execute(query, (
                configuracion.clave,
                configuracion.valor,
                configuracion.descripcion,
                configuracion.estado if configuracion.estado is not None else True,
                configuracion.creado,
                configuracion.actualizado
            ))
            nuevo_id = cursor.fetchone()['id']
            conn.commit()
            return nuevo_id
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al crear configuración: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def actualizar(self, configuracion_id: int, configuracion: Configuracion):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM configuracion WHERE id = %s;", (configuracion_id,))
            actual = cursor.fetchone()
            if not actual:
                return False

            clave = configuracion.clave if configuracion.clave is not None else actual['clave']
            valor = configuracion.valor if configuracion.valor is not None else actual['valor']
            descripcion = configuracion.descripcion if configuracion.descripcion is not None else actual['descripcion']
            estado = configuracion.estado if configuracion.estado is not None else actual['estado']
            creado = configuracion.creado if configuracion.creado is not None else actual['creado']

            query = """
                UPDATE configuracion 
                SET clave = %s, valor = %s, descripcion = %s, estado = %s, 
                    creado = %s, actualizado = %s
                WHERE id = %s
                RETURNING id;
            """
            cursor.execute(query, (
                clave, valor, descripcion, estado,
                creado, configuracion.actualizado,
                configuracion_id
            ))
            actualizado_row = cursor.fetchone()
            conn.commit()
            return actualizado_row is not None
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al actualizar configuración: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def eliminar(self, configuracion_id: int):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM configuracion WHERE id = %s RETURNING id;", (configuracion_id,))
            eliminado = cursor.fetchone()
            conn.commit()
            return eliminado is not None
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al eliminar configuración: {e}")
            raise
        finally:
            if conn:
                conn.close()