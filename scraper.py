from playwright.sync_api import sync_playwright
import re
import time

def scrape_prices():
    url = "https://www.carrefour.com.ar/harina%201kg?_q=harina%201kg&map=ft&order=OrderByPriceASC"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60000)

        # Wait 30 seconds to make sure everything loads (simulating your request)
        page.wait_for_timeout(30000)

        # Simulate CTRL+A + CTRL+C to get all visible text on the page
        page_text = page.evaluate("""
            () => {
                window.getSelection().removeAllRanges();
                const range = document.createRange();
                range.selectNode(document.body);
                window.getSelection().addRange(range);
                return window.getSelection().toString();
            }
        """)

        # Extract all prices that appear after the $ symbol
        prices = re.findall(r"\$\s?[\d\.\,]+", page_text)

        # Remove duplicates and sort
        prices = sorted(set(prices))

        browser.close()
        return prices
