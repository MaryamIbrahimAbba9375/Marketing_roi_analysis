# =====================================================================
# MODULE 2: PROCESS_MEDIA.PY - INFERENCE PIPELINE & DATA EXPORT
# =====================================================================
import json
import time
import numpy as np
from typing import List, Dict, Any
from detector import YOLODetector

class MediaProcessor:
    def __init__(self, detector: YOLODetector):
        self.detector = detector

    def process_image_to_json(self, image_path: str, output_json_path: str, conf: float = 0.25) -> Dict[str, Any]:
        """Runs inference and maps predictions to structural JSON metadata strings."""
        start_time = time.perf_counter()
        results = self.detector.run_inference(image_path, conf_threshold=conf)
        end_time = time.perf_counter()
        
        latency = end_time - start_time
        structured_data = {
            "image_path": image_path,
            "inference_latency_seconds": round(latency, 4),
            "detections": []
        }
        
        if results:
            result = results[0]  # Isolate first image result block
            boxes = result.boxes
            
            for box in boxes:
                # Extract coordinates from bounding box tensor blocks
                xyxy = box.xyxy[0].tolist()
                confidence = float(box.conf[0])
                class_id = int(box.cls[0])
                class_name = result.names[class_id]
                
                detection_entry = {
                    "class_name": class_name,
                    "class_id": class_id,
                    "confidence_score": round(confidence, 4),
                    "bounding_box_xyxy": [round(coord, 2) for coord in xyxy]
                }
                structured_data["detections"].append(detection_entry)
                
        # Export metrics out to physical storage path
        with open(output_json_path, 'w') as f:
            json.dump(structured_data, f, indent=4)
            
        return structured_data
