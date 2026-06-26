# =====================================================================
# MODULE 3: MAIN.PY - FASTAPI MEDIA ROUTING MILESTONE (GET ENDPOINT)
# =====================================================================
from fastapi import FastAPI, Response, HTTPException, Query
from models import generator_engine
from utils import convert_pil_to_bytes

app = FastAPI(
    title="ImagiServe Generative Core Portal",
    description="High-velocity endpoint routing serving compressed Stable Diffusion frames over HTTP."
)

# Milestone 3: Define a GET endpoint with response_class=Response and media_type='image/png'
@app.get("/generate/image", response_class=Response)
async def generate_image_endpoint(
    prompt: str = Query(..., description="The text prompt guiding the image generation"),
    negative_prompt: str = Query("blurry, low quality, distorted, extra limbs", description="Negative quality filters")
):
    """Processes generation prompts via HTTP GET parameters and streams image binaries."""
    if not prompt.strip():
        raise HTTPException(status_code=400, detail="Inbound query prompt string cannot be empty.")
        
    try:
        # Run inference through the models engine
        pil_img = generator_engine.generate_image(prompt=prompt, negative_prompt=negative_prompt)
        
        # Transform image object into network bytes stream using utility method
        image_bytes = convert_pil_to_bytes(pil_img)
        
        # Return standard Response object matching requested media guidelines
        return Response(content=image_bytes, media_type="image/png")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Failure: {str(e)}")
