from fastapi import FastAPI
from pydantic import BaseModel
from model_loader import load_model, generate_text
from metrics import llm_latency_histogram
import time

app = FastAPI(title="Multi-Region LLM Inference API")

model = load_model()

class Prompt(BaseModel):
    prompt: str
    max_length: int = 128

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate")
def generate(req: Prompt):
    start = time.time()
    output = generate_text(model, req.prompt, req.max_length)
    llm_latency_histogram.observe(time.time() - start)
    return {"result": output}
