# =====================================================================
# MODULE 2: UTILS.PY - BYTE-STREAM HANDLING MILESTONE
# =====================================================================
import io
from PIL import Image

def convert_pil_to_bytes(image: Image.Image) -> bytes:
    """Milestone 2: Byte-Stream Handling utility bypassing local disk I/O completely.
    
    Converts a standard memory-resident PIL Image asset straight into a byte stream.
    """
    byte_arr = io.BytesIO()
    image.save(byte_arr, format="PNG")
    return byte_arr.getvalue()
