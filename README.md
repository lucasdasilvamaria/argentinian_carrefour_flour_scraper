# Carrefour Argentina Price Scraper

This project scrapes the prices of grocery products from the Carrefour Argentina website using Playwright.

You can enter product names manually or load them from a `.txt` file. The program will visit the Carrefour search page for each product, extract the visible prices, calculate the average, and export everything to an `.xlsx` spreadsheet.

---

## Features

- Scrapes any product from Carrefour Argentina (not just flour)
- Supports multiple product inputs (manual or via text file)
- Calculates average price for each product
- Exports results to `results.xlsx`

---

## How to use

1. Install dependencies:

pip install -r requirements.txt

2. Remember to run "playwright install" on the terminal after installing the packages to get the browser binaries.

3. Choose one of the input methods when you run the script:

Manual input: Type each product name in Spanish and press Enter.

Text file input: Create a file named products.txt in the project folder, with one product per line.

Example: 
    harina 1kg
    leche condensada
    cacao en polvo

Notes:
Products must be entered in Spanish.
The script will automatically build the correct URLs and scrape visible prices from each product’s search page.
If no prices are found for a product, it will be reported in the Excel output.

4. Run on the terminal:

python main.py

5. After it finishes, check the generated results.xlsx file for your results.

