import os
import csv
from PIL import Image

# Paths
input_folder = "C:/Users/admin/images_in"
output_folder = "C:/Users/admin/images_out"
mapping_file = "C:/Users/admin/image_map.csv"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Load mapping
mapping = {}
with open(mapping_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        mapping[row['input_filename']] = row['new_base_name']

# Process
for old_name, new_base in mapping.items():
    input_path = os.path.join(input_folder, old_name)
    output_name = f"{new_base}-ireland.webp"
    output_path = os.path.join(output_folder, output_name)

    try:
        with Image.open(input_path) as img:
            img.save(output_path, format="WEBP", quality=85, method=6)
            print(f"✔ Saved {output_name}")
    except FileNotFoundError:
        print(f"⚠ File not found: {old_name}")
    except Exception as e:
        print(f"❌ Error processing {old_name}: {e}")
