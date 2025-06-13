from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
