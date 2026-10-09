from app.core.database import Database
from app.models.notificacion import Notificacion
from datetime import datetime

class NotificacionRepository:
    def __init__(self):
        self.db = Database()

    def obtener_todos(self):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM notificacion ORDER BY id ASC;")
            notificaciones = cursor.fetchall()
            return notificaciones
        except Exception as e:
            print(f"❌ Error al obtener notificaciones: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def obtener_por_id(self, notificacion_id: int):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM notificacion WHERE id = %s;", (notificacion_id,))
            notificacion = cursor.fetchone()
            return notificacion
        except Exception as e:
            print(f"❌ Error al obtener notificación: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def crear(self, notificacion: Notificacion):
        if not notificacion.usuario_id and not notificacion.actividad_id:
            raise ValueError("La notificacion debe tener al menos un usuario o una actividad asociada.")
        
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            fecha_actual = datetime.now()
            query = """
                INSERT INTO notificacion (usuario_id, actividad_id, titulo, mensaje, fecha_envio, leida) 
                VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;
            """
            cursor.execute(query, (
                notificacion.usuario_id,
                notificacion.actividad_id,
                notificacion.titulo,
                notificacion.mensaje,
                fecha_actual,
                notificacion.leida
            ))
            nuevo_id = cursor.fetchone()['id']
            conn.commit()
            return nuevo_id
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al crear notificación: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def actualizar(self, notificacion_id: int, notificacion: Notificacion):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            query = """
                UPDATE notificacion 
                SET usuario_id = %s, actividad_id = %s, titulo = %s, mensaje = %s, leida = %s
                WHERE id = %s
                RETURNING id;
            """
            cursor.execute(query, (
                notificacion.usuario_id,
                notificacion.actividad_id,
                notificacion.titulo,
                notificacion.mensaje,
                notificacion.leida,
                notificacion_id
            ))
            actualizado = cursor.fetchone()
            conn.commit()
            return actualizado is not None
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al actualizar notificación: {e}")
            raise
        finally:
            if conn:
                conn.close()

    def eliminar(self, notificacion_id: int):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM notificacion WHERE id = %s RETURNING id;", (notificacion_id,))
            eliminado = cursor.fetchone()
            conn.commit()
            return eliminado is not None
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al eliminar notificación: {e}")
            raise
        finally:
            if conn:
                conn.close()