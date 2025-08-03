from playwright.sync_api import sync_playwright
import re
import time

def raspar_precos():
    url = "https://www.carrefour.com.ar/harina%201kg?_q=harina%201kg&map=ft&order=OrderByPriceASC"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60000)

        # Espera 30 segundos para garantir que tudo carregue (simulando seu pedido)
        page.wait_for_timeout(30000)

        # Simula CTRL+A + CTRL+C pegando todo texto visível da página
        texto_pagina = page.evaluate("""
            () => {
                window.getSelection().removeAllRanges();
                const range = document.createRange();
                range.selectNode(document.body);
                window.getSelection().addRange(range);
                return window.getSelection().toString();
            }
        """)

        # Extrai todos os preços que aparecem depois do símbolo $
        precos = re.findall(r"\$\s?[\d\.\,]+", texto_pagina)

        # Remove duplicados e ordena
        precos = sorted(set(precos))

        browser.close()
        return precos
