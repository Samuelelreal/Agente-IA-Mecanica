import re

def _extraer_numero(texto, unidad_patterns=None):
    """
    Extrae el primer número encontrado en el texto que cumpla alguna de las unidades opcionales.
    Si unidad_patterns es None, extrae el primer número sin unidad.
    Devuelve float o None.
    """
    if unidad_patterns:
        for pat in unidad_patterns:
            m = re.search(rf'(\d+(?:\.\d+)?)\s*{pat}', texto)
            if m:
                return float(m.group(1))
        return None
    else:
        m = re.search(r'(\d+(?:\.\d+)?)', texto)
        return float(m.group(1)) if m else None


def parse_enunciado(texto: str) -> dict:
    """Extrae variables básicas del enunciado del problema (asume unidades SI)."""
    res = {}
    txt = texto.lower()

    res["enunciado"] = texto

    # masa (kg)
    m = re.search(r'(\d+(?:\.\d+)?)\s*kg', txt)
    if m:
        res["m"] = float(m.group(1))

    # velocidad inicial v0 (m/s) - busca "v0" o "velocidad inicial" o "v=" si aplica
    v0 = re.search(r'v0\s*=?\s*(\d+(?:\.\d+)?)\s*m/s', txt)
    if not v0:
        v0 = re.search(r'velocidad inicial\s*=?\s*(\d+(?:\.\d+)?)\s*m/s', txt)
    if v0:
        res["v0"] = float(v0.group(1))

    # aceleración a (m/s^2)
    a = re.search(r'a\s*=?\s*(\d+(?:\.\d+)?)\s*m/s\^?2', txt)
    if not a:
        a = re.search(r'aceleraci[oó]n\s*=?\s*(\d+(?:\.\d+)?)\s*m/s\^?2', txt)
    if a:
        res["a"] = float(a.group(1))

    # tiempo t (s)
    t = re.search(r't\s*=?\s*(\d+(?:\.\d+)?)\s*s\b', txt)
    if not t:
        t = re.search(r'tiempo\s*=?\s*(\d+(?:\.\d+)?)\s*s\b', txt)
    if t:
        res["t"] = float(t.group(1))

    # posición inicial x0 (m)
    x0 = re.search(r'x0\s*=?\s*(\d+(?:\.\d+)?)\s*m', txt)
    if not x0:
        x0 = re.search(r'posici[oó]n inicial\s*=?\s*(\d+(?:\.\d+)?)\s*m', txt)
    if x0:
        res["x0"] = float(x0.group(1))
    else:
        # por defecto asumimos x0 = 0
        res["x0"] = 0.0

    # Amplitud A, frecuencia omegas, etc. (oscilatorio) - unidades simples
    A = re.search(r'A\s*=?\s*(\d+(?:\.\d+)?)\s*m', txt)
    if A:
        res["A"] = float(A.group(1))

    w = re.search(r'omega\s*=?\s*(\d+(?:\.\d+)?)\s*(rad/s)?', txt)
    if not w:
        w = re.search(r'ω\s*=?\s*(\d+(?:\.\d+)?)', txt)
    if w:
        res["w"] = float(w.group(1))

    phi = re.search(r'phi\s*=?\s*(\d+(?:\.\d+)?)', txt)
    if phi:
        res["phi"] = float(phi.group(1))

    # detectar tipo de problema básico (palabras clave)
    if "lanza" in txt or "proyectil" in txt or "ángulo" in txt or "angulo" in txt:
        res["tipo"] = "proyectil"
    elif "cae" in txt or "caída" in txt or "caida" in txt:
        res["tipo"] = "caida_libre"
    elif "acelerado" in txt or "mrua" in txt or "aceleración constante" in txt or ("aceleración" in txt and "m/s" in txt):
        res["tipo"] = "mrua"
    elif "oscil" in txt or "resorte" in txt or "armónico" in txt or "armonico" in txt:
        res["tipo"] = "oscilatorio"
    else:
        res["tipo"] = "desconocido"

    return res
