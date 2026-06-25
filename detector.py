# =====================================================================
# MODULE 1: DETECTOR.PY - YOLO MODEL MANAGEMENT
# =====================================================================
import os
import torch
from ultralytics import YOLO
from typing import Optional

class YOLODetector:
    def __init__(self, model_version: str = "yolov8n.pt"):
        """Initializes and loads the specified Ultralytics YOLOv8 model variant."""
        print(f"⏳ Loading pre-trained weight framework: {model_version}...")
        self.model_version = model_version
        
        try:
            # Enforce automatic device placement (CUDA GPU if available, else CPU)
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
            self.model = YOLO(model_version).to(self.device)
            print(f"✅ Model successfully anchored to device architecture: {self.device.upper()}")
        except Exception as e:
            raise RuntimeError(f"❌ Initialization Failed. Failed to parse weight path: {str(e)}")

    def run_inference(self, image_source, conf_threshold: float = 0.25):
        """Executes object detection inference pass with configurable confidence thresholds."""
        try:
            results = self.model(image_source, conf=conf_threshold, verbose=False)
            return results
        except Exception as e:
            print(f"❌ Core Inference Error encountered: {str(e)}")
            return None
