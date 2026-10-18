from pydantic import BaseModel

class Voice(BaseModel):
    text : str


class MessageRequest(BaseModel):
    text : str
