from scraper import raspar_precos

def limpar_preco(preco_str):
    preco_limpo = preco_str.replace("$", "").replace(" ", "").replace(".", "").replace(",", ".")
    try:
        return float(preco_limpo)
    except:
        return None

def calcular_media(precos_str):
    precos_float = [limpar_preco(p) for p in precos_str]
    precos_validos = [p for p in precos_float if p is not None]
    if not precos_validos:
        return None
    return sum(precos_validos) / len(precos_validos)

if __name__ == "__main__":
    precos = raspar_precos()
    media = calcular_media(precos)
    if media is not None:
        print(f"Preço médio: ${media:.2f}")
    else:
        print("Nenhum preço válido encontrado.")
