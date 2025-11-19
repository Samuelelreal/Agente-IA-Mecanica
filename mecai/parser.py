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
    if "acelerado" in texto or "MRUA" in texto or "aceleración constante" in texto:
        res["tipo"] = "mrua"
        a = re.search(r"a\s*=\s*([\d\.]+)\s*m/s\^2", texto)
        if a: res["a"] = float(a.group(1))

        t = re.search(r"t\s*=\s*([\d\.]+)\s*s", texto)
        if t: res["t"] = float(t.group(1))

        x = re.search(r"x\s*=\s*([\d\.]+)\s*m", texto)
        if x: res["x"] = float(x.group(1))

    # Detectar oscilaciones
    elif "oscil" in texto or "resorte" in texto or "armónico" in texto:
        res["tipo"] = "oscilatorio"

        k = re.search(r"k\s*=\s*([\d\.]+)\s*N/m", texto)
        if k: res["k"] = float(k.group(1))

        m = re.search(r"m\s*=\s*([\d\.]+)\s*kg", texto)
        if m: res["m"] = float(m.group(1))

        A = re.search(r"A\s*=\s*([\d\.]+)\s*m", texto)
        if A: res["A"] = float(A.group(1))

    
    else:
        res["tipo"] = "desconocido"
    return res
