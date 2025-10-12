from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from crypto import decrypt, encrypt, get_env

app = FastAPI()
templates = Jinja2Templates(directory="web/templates")
app.mount("/static", StaticFiles(directory="web/static"), name="static")

env = get_env()

if not env.get("PASSWORD") or len(env.get("PASSWORD")) < 16:
    raise Exception(
        "This app requires a secure password of at least 16 characters to be provided to work"
    )

print(decrypt(encrypt("Hello World!", env.get("PASSWORD")), env.get("PASSWORD")))


@app.get("/", include_in_schema=False)
async def home(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})


@app.post("/encrypt", include_in_schema=False)
async def web_encrypt(request: Request):
    pass


@app.post("/decrypt", include_in_schema=False)
async def web_decrypt(request: Request):
    pass
