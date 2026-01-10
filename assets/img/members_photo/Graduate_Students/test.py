import os
from PIL import Image

def read_jpg_resolution(directory="."):
    for filename in os.listdir(directory):
        if filename.lower().endswith((".jpg", ".jpeg")):
            filepath = os.path.join(directory, filename)
            try:
                with Image.open(filepath) as img:
                    width, height = img.size
                    print(f"{filename}: {width} x {height}")
            except Exception as e:
                print(f"{filename}: 读取失败 ({e})")

if __name__ == "__main__":
    read_jpg_resolution()
