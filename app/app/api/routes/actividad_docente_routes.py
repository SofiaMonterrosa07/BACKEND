from fastapi import APIRouter, HTTPException
from app.models.actividad_docente import ActividadDocente
from app.repositories.actividad_docente_repository import ActividadDocenteRepository

router = APIRouter(prefix="/actividades-docentes", tags=["Actividad - Docente"])
repo = ActividadDocenteRepository()

# ============================================
# 1. OBTENER TODAS LAS ASIGNACIONES
# ============================================
@router.get("/")
def obtener_todos():
    return repo.obtener_todos()

# ============================================
# 2. OBTENER UNA ASIGNACIÓN POR ID
# ============================================
@router.get("/{id}")
def obtener_por_id(id: int):
    registro = repo.obtener_por_id(id)
    if not registro:
        raise HTTPException(status_code=404, detail="Asignación no encontrada")
    return registro

# ============================================
# 3. OBTENER DOCENTES DE UNA ACTIVIDAD
# ============================================
@router.get("/actividad/{actividad_id}")
def obtener_por_actividad(actividad_id: int):
    return repo.obtener_por_actividad(actividad_id)

# ============================================
# 4. OBTENER ACTIVIDADES DE UN DOCENTE
# ============================================
@router.get("/docente/{docente_id}")
def obtener_por_docente(docente_id: int):
    return repo.obtener_por_docente(docente_id)

# ============================================
# 5. VERIFICAR DISPONIBILIDAD DE UN DOCENTE
# ============================================
@router.get("/disponibilidad/{docente_id}")
def verificar_disponibilidad(docente_id: int, fecha: str, hora: str):
    """
    Verifica si un docente está disponible en una fecha y hora específicas.
    Ejemplo: /disponibilidad/40?fecha=2026-09-01&hora=14:00:00
    """
    disponible = repo.verificar_disponibilidad(docente_id, fecha, hora)
    return {
        "docente_id": docente_id,
        "fecha": fecha,
        "hora": hora,
        "disponible": disponible,
        "mensaje": "Docente disponible" if disponible else "Docente ocupado a esa fecha y hora"
    }

# ============================================
# 6. CREAR ASIGNACIÓN (CON VALIDACIÓN)
# ============================================
@router.post("/")
def crear_asignacion(data: ActividadDocente):
    try:
        nuevo_id = repo.crear(data)
        return {
            "id": nuevo_id, 
            "message": "Docente asignado a la actividad exitosamente"
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")

# ============================================
# 7. ACTUALIZAR ASIGNACIÓN (CON VALIDACIÓN)
# ============================================
@router.put("/{id}")
def actualizar_asignacion(id: int, data: ActividadDocente):
    try:
        if repo.actualizar(id, data):
            return {"message": "Asignación actualizada exitosamente"}
        raise HTTPException(status_code=404, detail="Asignación no encontrada")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")

# ============================================
# 8. ELIMINAR ASIGNACIÓN
# ============================================
@router.delete("/{id}")
def eliminar_asignacion(id: int):
    if repo.eliminar(id):
        return {"message": "Asignación eliminada exitosamente"}
    raise HTTPException(status_code=404, detail="Asignación no encontrada")