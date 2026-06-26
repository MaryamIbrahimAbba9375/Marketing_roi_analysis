# =====================================================================
# MODULE 1: MODELS.PY - GENERATIVE LOGIC MILESTONE
# =====================================================================
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

class GenerativeEngine:
    def __init__(self, model_id: str = "segmind/tiny-sd"):
        print(f"⏳ Initializing Distilled Text-to-Image Pipeline ({model_id})...")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # Load the stable diffusion pipeline optimization layers
        self.pipe = StableDiffusionPipeline.from_pretrained(
            model_id, 
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32
        )
        self.pipe.to(self.device)
        print(f"✅ Generative AI core anchored successfully on: {self.device.upper()}")

    def generate_image(self, prompt: str, negative_prompt: str = "blurry, low quality, distorted") -> Image.Image:
        """Milestone 1: Generative Logic function returning a clean PIL Image."""
        try:
            output = self.pipe(
                prompt=prompt,
                negative_prompt=negative_prompt,
                num_inference_steps=20,
                guidance_scale=7.0
            )
            return output.images[0]
        except Exception as e:
            print(f"❌ Critical Generation Fault: {str(e)}")
            return Image.new("RGB", (512, 512), color=(240, 240, 240))

# Pre-instantiate engine for modular import mapping
generator_engine = GenerativeEngine()
