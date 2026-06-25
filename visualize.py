# =====================================================================
# MODULE 3: VISUALIZE.PY - CV2 BOUNDING BOX RENDERING
# =====================================================================
import cv2
import numpy as np
from typing import List, Dict, Any

class Visualizer:
    @staticmethod
    def draw_annotations(image_path: str, detection_data: Dict[str, Any], output_path: str) -> None:
        """Loads source frames and paints verified bounding box dimensions onto space coordinates."""
        image = cv2.imread(image_path)
        if image is None:
            print(f"❌ Visualization Error: Image file context at {image_path} empty.")
            return

        for det in detection_data["detections"]:
            bbox = det["bounding_box_xyxy"]
            label = f"{det['class_name']} {det['confidence_score']:.2%}"
            
            # Map box coordinates to pixel integers
            x1, y1, x2, y2 = map(int, bbox)
            
            # Draw primary bounding box outline
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # Paint label backdrop anchor box
            (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
            cv2.rectangle(image, (x1, y1 - 20), (x1 + w, y1), (0, 255, 0), -1)
            
            # Render descriptive identifier string text blocks
            cv2.putText(image, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

        # Save out annotated image asset layer
        cv2.imwrite(output_path, image)
        print(f"🎯 Output successfully visualized and saved to: {output_path}")
