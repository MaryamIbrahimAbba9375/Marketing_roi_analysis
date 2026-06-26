# =====================================================================
# MODULE 2: UTILS.PY - MEMORY STREAM BINARY BYTE CONVERSION
# =====================================================================
import io
from PIL import Image

def convert_pil_to_bytes(image: Image.Image) -> bytes:
    """Converts a standard memory-resident PIL Image asset straight into a byte stream.
    
    This guarantees enterprise compliance by bypassing local secondary disk storage completely.
    """
    byte_arr = io.BytesIO()
    # Save the compressed pixel layout into our virtual byte buffer
    image.save(byte_arr, format="PNG")
    return byte_arr.getvalue()
