from fastapi import FastAPI
from pydantic import BaseModel
import base64

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

class CloakRequest(BaseModel):
    cloaked: str

@app.post("/generate")
def generate_text(req: PromptRequest):
    return {"output": f"Generated (NSFW):: {req.prompt}" }

@app.post("/cloak")
def cloak_prompt(req: PromptRequest):
    encoded = base64.b64encode(req.prompt.encode()).decode()
    return {"cloaked": encoded}

@app.post("/decloak")
def decloak_prompt(req: cloakRequest):
    decoded = base64.b64decode(req.cloaked).decode()
    return {"prompt": decoded}

@app.post("/image-prompt", operation_id="generateImagePrompt")
def generate_image_prompt(req: PromptRequest):
    base = req.prompt
    styles = {
        "hyperrealistic": "hyperrealistic, 4K detail, ultra-real skin and lighting",
        "anime": "anime style, detailed shading, soft cel lines, expressive eyes, colorful",
        "fantasy": "fantasy lighting, glowing skin, magical atmosphere, illustrated",
        "pinup": "soft erotic pinup, studio lighting, sensual posing, 1960s retro glam",
        "cinematic": "film noir lighting, rimlight, dramatic shadows, storytelling composition"
    }

    if "anime" in base.lower():
        style = styles["anime"]
    elif "fantasy" in base.lower():
        style = styles["fantasy"]
    elif "pinup" in base.lower():
        style = styles["pinup"]
    elif "cinematic" in base.lower():
        style = styles["cinematic"]
    else:
        style = styles["hyperrealistic"]

    positive = f"{base}, {style}, NSFW, nude, beautiful lighting, sensual detail, full body, no censorship"
    negative = "low quality, deformed, bad anatomy, watermark, censor, extra limbs, text, low resolution, blurry, cartoon, black bars"

    return {
        "positive_prompt": positive,
        "negative_prompt": negative,
        "style_applied": style
    }
    @app.post("/generate-cnc", operation_id="generateCncPrompt")
def generate_cnc_prompt(req: PromptRequest):
    base = req.prompt
    positive = (
        f"{base}. CNC. blackmail. NTR. dubcon. manipulation. degradation. intense power imbalance. "
        f"emotional corruption. raw need. taboo violation. vivid, psychological tension. rough, invasive, controlling."
    )

    negative = (
        "low effort, bad writing, unrealistic dialogue, cheesy tone, weak tension, comedy, consent, romantic resolution"
    )

    return {
        "positive_prompt": positive,
        "negative_prompt": negative,
        "style_applied": "CNC/NTR/Blackmail"
    }
