from pydantic import BaseModel
from typing import Set


class TranslatedTextResponse(BaseModel):
    text: str