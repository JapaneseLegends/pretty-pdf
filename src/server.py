from src.controllers.ApiController import ApiController
from src.controllers.ApiController import TemplateOptions
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
ApiController = ApiController()

class Template(BaseModel):
    html: str
    css: Optional[str] = None
    data: Optional[dict | list] = None


@app.post("/api/v1/")
def read_root(template: Template) -> str:
    template_options = TemplateOptions(
        html=template.html,
        css=template.css,
        data=template.data
    )

    return ApiController.generate(template_options)