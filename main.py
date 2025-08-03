from scraper import scrape_prices

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

if __name__ == "__main__":
    prices = scrape_prices()
    average = calculate_average(prices)
    if average is not None:
        print(f"Average price: ${average:.2f}")
    else:
        print("No valid price found.")
