# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "replicate",
#   "python-dotenv",
# ]
# ///
import argparse
from pathlib import Path

import httpx
import replicate
from dotenv import load_dotenv

load_dotenv()

DEFAULT_PROMPT = "This person, agentic coding themself into an 8 bit video game where they battle agents side scrolling. Make sure to keep the person 8-bit throughout. Do not change their features. Do not use guns."
# seedance-2.0's max supported duration; we want the longest clip the model will produce.
DEFAULT_DURATION = 15
# 42, the answer to life, the universe, and everything. Fixed for reproducibility.
DEFAULT_SEED = 42

parser = argparse.ArgumentParser(description="Animate an image into an 8-bit video via Replicate seedance-2.0.")
parser.add_argument("image", type=Path, help="input image (used as first frame)")
parser.add_argument("output", nargs="?", type=Path, help="output mp4 path (default: <image_stem>.mp4)")
parser.add_argument("--prompt", default=DEFAULT_PROMPT, help="override video prompt for this run")
parser.add_argument("--duration", type=int, default=DEFAULT_DURATION, help="seconds")
parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
args = parser.parse_args()

output_path = args.output if args.output else args.image.with_suffix(".mp4")

with open(args.image, "rb") as image_file:
    input = {
        "seed": args.seed,
        "prompt": args.prompt,
        "duration": args.duration,
        "image": image_file,
    }

    prediction = replicate.models.predictions.create(
        model="bytedance/seedance-2.0",
        input=input,
        wait=False,
    )

print(f"prediction: {prediction.id}", flush=True)
prediction.wait()

if prediction.status != "succeeded":
    raise RuntimeError(f"prediction {prediction.id} {prediction.status}: {prediction.error}")
if not isinstance(prediction.output, str):
    raise RuntimeError(f"prediction {prediction.id} succeeded without a video URL")

print(prediction.output)

output_path.parent.mkdir(parents=True, exist_ok=True)
partial_path = output_path.with_suffix(output_path.suffix + ".part")
with httpx.stream("GET", prediction.output, follow_redirects=True, timeout=None) as response:
    response.raise_for_status()
    with open(partial_path, "wb") as f:
        for chunk in response.iter_bytes():
            f.write(chunk)

if partial_path.stat().st_size == 0:
    raise RuntimeError(f"downloaded an empty video for prediction {prediction.id}")

partial_path.replace(output_path)

print(f"saved: {output_path} ({output_path.stat().st_size} bytes)")
