import re

def parse_enunciado(texto: str) -> dict:
    """Extrae variables básicas del enunciado del problema."""
    res = {}
    res["enunciado"] = texto
    m = re.search(r'(\d+(?:\.\d+)?)\s*kg', texto)
    if m: res["m"] = float(m.group(1))
    v = re.search(r'v0\s*=?\s*(\d+(?:\.\d+)?)\s*m/s', texto)
    if v: res["v0"] = float(v.group(1))
    a = re.search(r'(\d+(?:\.\d+)?)\s*°', texto)
    if a: res["angulo"] = float(a.group(1))
    g = re.search(r'g\s*=?\s*(\d+(?:\.\d+)?)', texto)
    if g: res["g"] = float(g.group(1))
    else: res["g"] = 9.81
    # tipo de problema básico
    if "lanza" in texto or "proyectil" in texto:
        res["tipo"] = "proyectil"
    elif "cae" in texto:
        res["tipo"] = "caida_libre"
    else:
        res["tipo"] = "desconocido"
    return res
