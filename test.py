import os
import json

jsonl_file = "/root/autodl-tmp/MixLoRA/data/images/union.jsonl"
image_dir = "/root/autodl-tmp/MixLoRA/data/images"

with open(jsonl_file, "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        image_path = os.path.join(image_dir, data["image_path"])
        if not os.path.exists(image_path):
            print(f"Missing image: {image_path}")