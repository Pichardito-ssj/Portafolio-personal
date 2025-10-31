from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routers import web

app = FastAPI(title="Portafolio - Tu Nombre (Oscuro)")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(web.router)

@app.get("/health")
async def health():
    return {"status": "ok"}
