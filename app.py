from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from auto_template import setup_templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = setup_templates(directory="templates")


@app.get("/")
async def index(request: Request):
    context = {
        "content": "Hello Cloudflare Workers from Python!",
    }

    return templates.TemplateResponse(
        request=request,
        context=context,
        name="index.html",
    )
