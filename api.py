from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()
app.mount("/static",StaticFiles(directory="static/"),name="static")

#@app.get("/")
#def home():
 #   return "Bienvenidos"

@app.get("/", response_class=HTMLResponse)
def home():
    with open("templates/index.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return html_content
