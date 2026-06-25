# =====================================================================
# MODULE 1: MODELS.PY - LOCAL LLM INFERENCE ENGINE
# =====================================================================
import os
import torch
from transformers import pipeline

class InferenceEngine:
    def __init__(self, model_name="TinyLlama/TinyLlama-1.1B-Chat-v1.0"):
        print(f"⏳ Initializing local inference pipeline for {model_name}...")
        self.device = 0 if torch.cuda.is_available() else -1
        self.generator = pipeline(
            "text-generation",
            model=model_name,
            torch_dtype=torch.bfloat16 if torch.cuda.is_available() else torch.float32,
            device=self.device
        )
        self.system_prompt = (
            "<|system|>\nYou are an expert, highly critical AI Code Reviewer. "
            "Analyze the user's code snippet for security bugs, performance bottlenecks, "
            "and PEP8 compliance. Provide concise, constructive fixes.</s>\n"
        )
        print("✅ Local LLM Engine Successfully Loaded.")

    def generate_response(self, user_prompt: str, max_new_tokens: int = 128) -> str:
        try:
            full_prompt = f"{self.system_prompt}<|user|>\n{user_prompt}</s>\n<|assistant|>\n"
            outputs = self.generator(
                full_prompt,
                max_new_tokens=max_new_tokens,
                do_sample=True,
                temperature=0.7,
                top_k=50,
                top_p=0.95
            )
            generated_text = outputs[0]["generated_text"]
            response_sequence = generated_text.split("<|assistant|>\n")[-1].strip()
            return response_sequence
        except Exception as e:
            return f"❌ Internal Model Inference Error: {str(e)}"

# Instantiate the engine
engine = InferenceEngine()
