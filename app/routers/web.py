from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
async def index(request: Request):
    context = {
        "request": request,
        "name": "Jose Pichardo",
        "title": "Portafolio Profesional",
        "role": "Estudiante de Analisis de Sistemas",
        "bio": "Desarrollador full-stack con experiencia en sistemas web y soluciones escalables.",
        "projects": [
            {"title": "Proyecto A", "desc": "Pequeño proyecto prototipo de una Pagina Web", "file": "/static/downloads/ProyectoA.rar"},
            {"title": "Proyecto B", "desc": "Descripción breve del Proyecto B", "file": "#"},
        ],
        "contact": {"email": "ramonjose886@gmail.com", "phone": "+58 412-1521475"},
    }
    return templates.TemplateResponse("index.html", context)
