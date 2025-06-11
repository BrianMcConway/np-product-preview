import csv

from pathlib import Path

# Input and output files
input_file = "C:/Users/admin/product_data.csv"
output_file = "C:/Users/admin/np_output.csv"

def rewrite_description(raw):
    # Very basic rewrite logic to strip marketing fluff and simplify
    cleaned = raw.replace("perfect", "").replace("role play", "checkout play").replace("!", "").strip()
    return cleaned[0].upper() + cleaned[1:] if cleaned else ""

# Prepare output rows
output_rows = []

with open(input_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        product_name = row["product_name"].strip()
        brand = row["brand"].strip()
        alt1 = row["alt_suffix_1"].strip()
        alt2 = row["alt_suffix_2"].strip()
        age = row["age_info"].strip()
        batteries = row["batteries"].strip()
        raw_description = row.get("raw_description", "").strip()

        slug = product_name.lower().replace(" ", "-") + "-ireland"
        seo_title = f"{brand} {product_name} – Cash Register Toy Ireland"
        meta = f"Buy the {brand} {product_name} from ToyTown.ie Toymaster, Longford. Includes accessories for checkout play."

        alt_text_1 = f"{brand} {product_name} {alt1} with scanner and food – Ireland"
        alt_text_2 = f"{brand} {product_name} {alt2} showing calculator and card reader – Ireland"

        heading = f"{brand} {product_name} Ireland"
        paragraph = rewrite_description(raw_description)

        bullets = [
            "Touch-style keypad with working calculator",
            "Chip and pin reader with play debit card",
            "Includes coins, notes and branded food",
            "Built-in microphone for announcements",
            f"Requires {batteries}",
            f"Suitable for ages {age}"
        ]

        # Store all outputs in one row
        output_rows.append({
            "SEO Title": seo_title,
            "Slug": slug,
            "Meta Description": meta,
            "Alt Text 1": alt_text_1,
            "Alt Text 2": alt_text_2,
            "PD Heading": heading,
            "PD Paragraph": paragraph,
            "Bullet 1": bullets[0],
            "Bullet 2": bullets[1],
            "Bullet 3": bullets[2],
            "Bullet 4": bullets[3],
            "Bullet 5": bullets[4],
            "Bullet 6": bullets[5],
        })

# Write to CSV
with open(output_file, "w", newline='', encoding='utf-8') as csvout:
    fieldnames = output_rows[0].keys()
    writer = csv.DictWriter(csvout, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(output_rows)

print("✔ NP metadata generated to np_output.csv")
