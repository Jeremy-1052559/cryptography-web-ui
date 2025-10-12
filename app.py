from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="web/templates")
app.mount("/static", StaticFiles(directory="web/static"), name="static")


@app.get("/", include_in_schema=False)
async def home(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})
