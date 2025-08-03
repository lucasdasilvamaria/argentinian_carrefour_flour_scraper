# Carrefour Argentina Flour Price Scraper

This project scrapes the prices of 1kg flour products from the Carrefour Argentina website.

It uses Playwright to open the webpage, wait for content to load, extract the full visible text, and then parse all prices starting with "$".

Finally, it calculates the average price of the flour products found.

---

## How to use

1. Install dependencies:

pip install -r requirements.txt

2. Remember to run "playwright install" on the terminal after installing the packages to get the browser binaries.

3. Run on the terminal:

python main.py