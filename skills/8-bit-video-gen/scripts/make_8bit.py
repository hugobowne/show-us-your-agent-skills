# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "google-genai>=1.53.0",
#   "pillow",
#   "python-dotenv",
# ]
# ///
import argparse
import sys
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from PIL import Image

load_dotenv()

DEFAULT_PROMPT = "This exact image, but 8 bit."

parser = argparse.ArgumentParser(description="Stylize an image as an 8-bit still via Gemini.")
parser.add_argument("input_image", type=Path, help="input image to stylize")
parser.add_argument("output_image", nargs="?", type=Path, help="output PNG path (default: <input_stem>_8bit.png)")
parser.add_argument("--prompt", default=DEFAULT_PROMPT, help="override still-image prompt for this run")
args = parser.parse_args()

input_path = args.input_image
output_path = args.output_image if args.output_image else input_path.with_name(f"{input_path.stem}_8bit.png")

client = genai.Client()

with Image.open(input_path) as image:
    response = client.models.generate_content(
        model="gemini-3.1-flash-image-preview",
        contents=[args.prompt, image],
    )

saved = False
for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        out = part.as_image()
        out.save(output_path)
        print(f"saved: {output_path}")
        saved = True

if not saved:
    print("no image returned", file=sys.stderr)
    sys.exit(2)
