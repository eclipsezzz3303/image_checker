from pathlib import Path
from PIL import Image

IMAGES_DIR = Path("images")
IMAGES_DIR.mkdir(exist_ok=True)

Image.new("RGB", (640, 480), color="red").save(IMAGES_DIR / "photo1.jpg")
Image.new("RGB", (1920, 1080), color="green").save(IMAGES_DIR / "photo2.png") 
Image.new("RGB", (100, 100), color="blue").save(IMAGES_DIR / "photo3.jpg")

(IMAGES_DIR / "broken.jpg").write_bytes(b"this is not a real image")

(IMAGES_DIR / "notes.txt").write_text("just a text file")

print("测试图片已生成到 images/ 目录") 