from playwright.sync_api import sync_playwright
import re

def scrape_prices(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(30000)

        page_text = page.evaluate("""
            () => {
                window.getSelection().removeAllRanges();
                const range = document.createRange();
                range.selectNode(document.body);
                window.getSelection().addRange(range);
                return window.getSelection().toString();
            }
        """)

        prices = re.findall(r"\$\s?[\d\.\,]+", page_text)
        prices = sorted(set(prices))

        browser.close()
        return prices
