# =====================================================================
# MODULE 2: MAIN.PY - FASTAPI REST ENDPOINT SPECIFICATION
# =====================================================================
import time
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models import engine  # This will now work perfectly!

app = FastAPI(
    title="Lumina LLM Inference Serving Portal",
    description="Production-grade local model serving wrapper for developer workflow optimizations."
)

class PromptRequest(BaseModel):
    prompt: str
    max_tokens: int = 128

class CompletionResponse(BaseModel):
    response: str
    latency_seconds: float

@app.post("/v1/chat/completions", response_model=CompletionResponse)
async def serve_llm_inference(request: PromptRequest):
    if not request.prompt.strip():
        raise HTTPException(status_code=400, detail="User prompt string cannot be blank.")
        
    start_time = time.perf_counter()
    ai_output = engine.generate_response(request.prompt, max_new_tokens=request.max_tokens)
    end_time = time.perf_counter()
    
    return CompletionResponse(
        response=ai_output,
        latency_seconds=round(end_time - start_time, 3)
    )
