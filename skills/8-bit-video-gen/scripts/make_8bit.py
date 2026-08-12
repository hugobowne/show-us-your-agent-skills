# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "google-genai>=1.53.0",
#   "pillow",
#   "python-dotenv",
# ]
# ///
import argparse
import base64
import mimetypes
import sys
from pathlib import Path

from dotenv import load_dotenv
from google import genai

load_dotenv()

DEFAULT_PROMPT = "This exact image, but 8 bit."

parser = argparse.ArgumentParser(description="Stylize an image as an 8-bit still via Gemini.")
parser.add_argument("input_image", type=Path, help="input image to stylize")
parser.add_argument("output_image", nargs="?", type=Path, help="output PNG path (default: <input_stem>_8bit.png)")
parser.add_argument("--prompt", default=DEFAULT_PROMPT, help="override still-image prompt for this run")
parser.add_argument("--model", default="gemini-3.1-flash-image", help="Gemini image model to use")
args = parser.parse_args()

input_path = args.input_image
output_path = args.output_image if args.output_image else input_path.with_name(f"{input_path.stem}_8bit.png")

client = genai.Client()

mime_type, _ = mimetypes.guess_type(input_path)
if mime_type is None:
    mime_type = "image/png"

image_data = base64.b64encode(input_path.read_bytes()).decode("utf-8")
interaction = client.interactions.create(
    model=args.model,
    input=[
        {"type": "text", "text": args.prompt},
        {"type": "image", "data": image_data, "mime_type": mime_type},
    ],
)

if interaction.output_text:
    print(interaction.output_text)

if interaction.output_image:
    output_path.write_bytes(base64.b64decode(interaction.output_image.data))
    print(f"saved: {output_path}")
else:
    print("no image returned", file=sys.stderr)
    sys.exit(2)
