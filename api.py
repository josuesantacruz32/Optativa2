from tempfile import template
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()
app.mount("/static",StaticFiles(directory="static/"),name="static")


# Ruta para la página principal
@app.get("/", response_class=HTMLResponse)
async def home():
    with open("templates/index.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return html_content

# Ruta para la tabla
@app.get("/tabla", response_class=HTMLResponse)
async def tabla():
    with open("templates/Tabla.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return html_content