from typing import TypedDict, Optional

class TemplateRenderOptions(TypedDict):
    templatePath: str
    templateData: Optional[dict]
    jsonPath: Optional[str]