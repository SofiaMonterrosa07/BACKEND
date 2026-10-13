from app.core.database import Database
from app.models.actividad import Actividad


class ActividadRepository:

    def __init__(self):
        self.db = Database()

    # ==========================================
    # OBTENER TODAS LAS ACTIVIDADES
    # ==========================================

    def obtener_todos(self):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT *
                FROM actividad
                ORDER BY id ASC;
            """)
            return cursor.fetchall()
        except Exception as e:
            print(f"❌ Error al obtener actividades: {e}")
            raise
        finally:
            if conn:
                conn.close()

    # ==========================================
    # OBTENER ACTIVIDAD POR ID
    # ==========================================

    def obtener_por_id(self, actividad_id: int):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT *
                FROM actividad
                WHERE id = %s;
            """, (actividad_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"❌ Error al obtener actividad: {e}")
            raise
        finally:
            if conn:
                conn.close()

    # ==========================================
    # CREAR ACTIVIDAD
    # ==========================================

    def crear(self, actividad: Actividad):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO actividad
                (
                    nombre,
                    descripcion,
                    fecha,
                    hora,
                    lugar,
                    cupo,
                    categoria_id,
                    estado
                )
                VALUES
                (%s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id;
            """, (
                actividad.nombre,
                actividad.descripcion,
                actividad.fecha,
                actividad.hora,
                actividad.lugar,
                actividad.cupo,
                actividad.categoria_id,
                actividad.estado
            ))
            nuevo_id = cursor.fetchone()["id"]
            conn.commit()
            return nuevo_id
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al crear actividad: {e}")
            raise
        finally:
            if conn:
                conn.close()

    # ==========================================
    # ACTUALIZAR ACTIVIDAD
    # ==========================================

    def actualizar(self, actividad_id: int, actividad: Actividad):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE actividad
                SET
                    nombre = %s,
                    descripcion = %s,
                    fecha = %s,
                    hora = %s,
                    lugar = %s,
                    cupo = %s,
                    categoria_id = %s,
                    estado = %s
                WHERE id = %s
                RETURNING id;
            """, (
                actividad.nombre,
                actividad.descripcion,
                actividad.fecha,
                actividad.hora,
                actividad.lugar,
                actividad.cupo,
                actividad.categoria_id,
                actividad.estado,
                actividad_id
            ))
            actualizado = cursor.fetchone()
            conn.commit()
            return actualizado is not None
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al actualizar actividad: {e}")
            raise
        finally:
            if conn:
                conn.close()

    # ==========================================
    # ELIMINAR ACTIVIDAD
    # ==========================================

    def eliminar(self, actividad_id: int):
        conn = None
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM actividad
                WHERE id = %s
                RETURNING id;
            """, (actividad_id,))
            eliminado = cursor.fetchone()
            conn.commit()
            return eliminado is not None
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"❌ Error al eliminar actividad: {e}")
            raise
        finally:
            if conn:
                conn.close()