from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import (
    rol_routes, usuario_routes, modulo_routes, modulo_rol_routes,
    estudiante_routes, acudiente_routes, categoria_actividad_routes,
    actividad_routes, inscripcion_routes, autorizacion_routes,
    asistencia_routes, notificacion_routes, actividad_docente_routes
)

app = FastAPI(
    title="Colegio san Miguel: Area de gestoria para Eventos y Actividades extracurriculares",
    description="API para gestión de actividades extracurriculares con autorización digital - Colegio san Miguel",
    version="1.0.0"
)

# Permitir que SvelteKit se conecte con FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Registrar todas las rutas (conecta con lqa fastAPI)
app.include_router(rol_routes.router)
app.include_router(usuario_routes.router)
app.include_router(modulo_routes.router)
app.include_router(modulo_rol_routes.router)
app.include_router(estudiante_routes.router)
app.include_router(acudiente_routes.router)
app.include_router(categoria_actividad_routes.router)
app.include_router(actividad_routes.router)
app.include_router(inscripcion_routes.router)
app.include_router(autorizacion_routes.router)
app.include_router(asistencia_routes.router)
app.include_router(notificacion_routes.router)
app.include_router(actividad_docente_routes.router)

@app.get("/")
def root():
    return {
        "Colegio": "Colegio san Miguel",
        "message": "API Gestión de Eventos y Actividades Extracurriculares",
        "docs": "/docs",
        "status": "Funcionando correctamente"
    }