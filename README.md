        # Portafolio Profesional (Oscuro, Elegante) - FastAPI + Uvicorn

        ## Ejecutar localmente

        1. Crear y activar entorno virtual:

```
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate
```

2. Instalar dependencias:

```
pip install -r requirements.txt
```

3. Ejecutar servidor:

```
uvicorn app.main:app --reload --port 8000
```

4. Abrir en el navegador: http://127.0.0.1:8000

---

Para incluir tu foto y el logo del IUTEPI, reemplaza los archivos en `app/static/images/foto.jpg` y `app/static/images/logo.png`.
