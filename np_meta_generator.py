import csv

# Load product data
input_file = "C:/Users/admin/product_data.csv"

with open(input_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        product_name = row["product_name"].strip()
        brand = row["brand"].strip()
        alt1 = row["alt_suffix_1"].strip()
        alt2 = row["alt_suffix_2"].strip()
        age = row["age_info"].strip()
        batteries = row["batteries"].strip()

        slug = product_name.lower().replace(" ", "-") + "-ireland"
        seo_title = f"{brand} {product_name} – Cash Register Toy Ireland"
        meta = f"Buy the {brand} {product_name} from ToyTown.ie Toymaster, Longford. Includes accessories for checkout play."

        alt_text_1 = f"{brand} {product_name} {alt1} with scanner and food – Ireland"
        alt_text_2 = f"{brand} {product_name} {alt2} showing calculator and card reader – Ireland"

        heading = f"{brand} {product_name} Ireland"

        paragraph = (
            f"This colourful {product_name.lower()} includes a working calculator, chip and pin reader, scanner, and microphone. "
            "With realistic accessories and branded food items, it's perfect for checkout play at home."
        )

        bullets = [
            "Touch-style keypad with working calculator",
            "Chip and pin reader with play debit card",
            "Includes coins, notes and branded food",
            "Built-in microphone for announcements",
            f"Requires {batteries}",
            f"Suitable for ages {age}"
        ]

        print("------")
        print(f"SEO Title: {seo_title}")
        print(f"Slug: {slug}")
        print(f"Meta: {meta}")
        print(f"Alt Text 1: {alt_text_1}")
        print(f"Alt Text 2: {alt_text_2}")
        print()
        print(heading)
        print()
        print(paragraph)
        print()
        for b in bullets:
            print(f"- {b}")
