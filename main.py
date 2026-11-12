from fastapi import FastAPI,Request,Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static",StaticFiles(directory="static"),name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request:Request):
    theme = request.cookies.get("theme","light")
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "theme":theme
        }
    )
@app.post("/set-theme")
def set_theme(theme : str = Form(...)):
    response = RedirectResponse(
        url="/",
        status_code=303
    )
    response.set_cookie(
        key="theme",
        value=theme,
        max_age = 60*60*24*30
    )
    return response