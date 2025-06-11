from PIL import Image
import os

# === CONFIGURATION ===
input_folder = "C:/Users/admin/images_in"       # folder with PNG/JPG files
output_folder = "C:/Users/admin/images_out"     # folder where .webp files will be saved

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Conversion settings
webp_settings = {
    "format": "WEBP",
    "quality": 85,
    "method": 6
}

# Process all image files
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        base = os.path.splitext(filename)[0]
        input_path = os.path.join(input_folder, filename)

        # You rename the file manually before dropping it in the folder
        output_filename = f"{base}-ireland.webp"
        output_path = os.path.join(output_folder, output_filename)

        with Image.open(input_path) as img:
            img.save(output_path, **webp_settings)
            print(f"✔ Saved {output_filename}")
