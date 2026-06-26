# =====================================================================
# MODULE 1: MODELS.PY - TINY STABLE DIFFUSION PIPELINE
# =====================================================================
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

class GenerativeEngine:
    def __init__(self, model_id: str = "segmind/tiny-sd"):
        print(f"⏳ Initializing Distilled Text-to-Image Pipeline ({model_id})...")
        
        # Select device automatically based on runtime capability
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # Load the stable diffusion pipeline optimization layers
        self.pipe = StableDiffusionPipeline.from_pretrained(
            model_id, 
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32
        )
        self.pipe.to(self.device)
        print(f"✅ Generative AI core anchored successfully on: {self.device.upper()}")

    def generate_image_from_text(self, prompt: str, negative_prompt: str = "") -> Image.Image:
        """Runs latent diffusion steps to synthesize a fresh PIL image asset."""
        try:
            # Low inference steps (20) matching distilled tiny-sd architecture capabilities
            output = self.pipe(
                prompt=prompt,
                negative_prompt=negative_prompt,
                num_inference_steps=20,
                guidance_scale=7.0
            )
            return output.images[0]
        except Exception as e:
            print(f"❌ Critical Generation Fault: {str(e)}")
            # Fallback block creating a blank placeholder fallback image if pipeline errors out
            return Image.new("RGB", (256, 256), color=(200, 200, 200))

# Pre-instantiate engine for modular import mapping
generator_engine = GenerativeEngine()
