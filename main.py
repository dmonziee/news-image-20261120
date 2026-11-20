"""Entry for news-image-20261120: place the front-page image at the output.

The newspaper front page (entry.png, 1024x1024) was drawn in this session
from Friday 20 November 2026's reported news and sits next to this file.
This program only copies it into the output directory, using the standard
library, so two runs produce exactly the same bytes.
"""
import hashlib
import os
import shutil
import sys
from pathlib import Path

base = Path(__file__).resolve().parent
target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
target_dir.mkdir(parents=True, exist_ok=True)
source = base / "entry.png"
target = target_dir / "entry.png"
shutil.copyfile(source, target)
size = target.stat().st_size
# Byte-identical copy check: the output must hash exactly like the source.
source_hash = hashlib.sha256(source.read_bytes()).hexdigest()
target_hash = hashlib.sha256(target.read_bytes()).hexdigest()
assert source_hash == target_hash, "copied entry.png differs from source"
print(f"entry.png written to {target} ({size} bytes, sha256 "
      f"{target_hash[:12]}...)", file=sys.stderr)
