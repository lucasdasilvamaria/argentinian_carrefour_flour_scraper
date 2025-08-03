from scraper import scrape_prices
from urllib.parse import quote
from openpyxl import Workbook
import os


def clean_price(price_str):
    clean_price = price_str.replace("$", "").replace(" ", "").replace(".", "").replace(",", ".")
    try:
        return float(clean_price)
    except:
        return None


def calculate_average(price_strs):
    float_prices = [clean_price(p) for p in price_strs]
    valid_prices = [p for p in float_prices if p is not None]
    if not valid_prices:
        return None
    return sum(valid_prices) / len(valid_prices)


def build_url(product_name):
    product_path = quote(product_name)
    base_url = "https://www.carrefour.com.ar/"
    url = f"{base_url}{product_path}?_q={quote(product_name)}&map=ft&order=OrderByPriceASC"
    return url


def load_products_from_txt(filename="products.txt"):
    if not os.path.exists(filename):
        print(f"File '{filename}' not found.")
        return []

    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    if not lines:
        print(f"The file '{filename}' is empty.")
        return []

    return lines


def get_products():
    print("Choose how to provide the products:")
    print("1 - Type manually")
    print("2 - Load from 'products.txt'")

    choice = input("Enter 1 or 2: ").strip()

    products = []

    if choice == "1":
        print("\nWrite in Spanish the products that you would like to research.")
        while True:
            entry = input("Type a product name or press 1 to run the research: ").strip()
            if entry == "":
                print("Empty input, please write a product name or 1 to run.")
                continue
            if entry == "1":
                if not products:
                    print("You must enter at least one product before running the research.")
                    continue
                break
            products.append(entry)
    elif choice == "2":
        products = load_products_from_txt()
        if not products:
            print("No products to process. Exiting.")
            exit()
    else:
        print("Invalid option. Exiting.")
        exit()

    return products


def main():
    products = get_products()

    wb = Workbook()
    ws = wb.active
    ws.title = "Product Prices"
    ws.append(["Product", "Average Price (ARS)"])

    for product in products:
        url = build_url(product)
        print(f"\nSearching prices for '{product}' at: {url}")
        prices = scrape_prices(url)
        avg = calculate_average(prices)
        if avg is not None:
            print(f"Average price for '{product}': ${avg:.2f}")
            ws.append([product, avg])
        else:
            print(f"No valid prices found for '{product}'. Skipping.")
            ws.append([product, "No prices found"])

    xlsx_filename = "results.xlsx"
    wb.save(xlsx_filename)
    print(f"\nAll results saved to '{xlsx_filename}'")


if __name__ == "__main__":
    main()
