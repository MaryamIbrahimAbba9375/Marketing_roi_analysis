# =====================================================================
# MODULE 3: MAIN.PY - FASTAPI MULTIMEDIA STREAM WRAPPER
# =====================================================================
import time
from fastapi import FastAPI, Response, HTTPException
from pydantic import BaseModel
from models import generator_engine
from utils import convert_pil_to_bytes

app = FastAPI(
    title="ImagiServe Generative Core Portal",
    description="High-velocity endpoint routing serving compressed Stable Diffusion frames over HTTP."
)

class ImageGenerationRequest(BaseModel):
    prompt: str
    negative_prompt: str = "blurry, low quality, distorted, extra limbs"

@app.post("/generate/image")
async def generate_image_endpoint(request: ImageGenerationRequest):
    """Processes generation prompts and returns raw image binaries directly."""
    if not request.prompt.strip():
        raise HTTPException(status_code=400, detail="Inbound request prompt cannot be empty.")
        
    try:
        # Run inference through models engine
        pil_img = generator_engine.generate_image_from_text(
            prompt=request.prompt,
            negative_prompt=request.negative_prompt
        )
        
        # Transform image object into network bytes stream using utility method
        image_bytes = convert_pil_to_bytes(pil_img)
        
        # Stream the binary chunk with explicit media type declaration
        return Response(content=image_bytes, media_type="image/png")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Failure: {str(e)}")
