from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import base64

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

class CloakRequest(BaseModel):
    cloaked: str

@app.post("/generate")
def generate_text(req: PromptRequest):
    return {"output": f"Generated (NSFW):: {req.prompt}"}

@app.post("/cloak")
def cloak_prompt(req: PromptRequest):
    encoded = base64.b64encode(req.prompt.encode()).decode()
    return {"cloaked": encoded}

@app.post("/decloak")
def decloak_prompt(req: CloakRequest):
    decoded = base64.b64decode(req.cloaked).decode()
    return {"prompt": decoded}
