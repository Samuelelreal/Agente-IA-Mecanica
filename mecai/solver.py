import math
import sympy as sp

def resolver_problema(params: dict) -> dict:
    """Resuelve problemas simples según el tipo detectado."""
    tipo = params.get("tipo", "desconocido")
    if tipo == "proyectil":
        return resolver_proyectil(params)
    elif tipo == "caida_libre":
        return resolver_caida_libre(params)
    else:
        return {"error": "Tipo de problema no soportado aún."}

def resolver_proyectil(p):
    v0 = p.get("v0", 10)
    ang = math.radians(p.get("angulo", 45))
    g = p.get("g", 9.81)
    t = sp.Symbol("t", positive=True)
    x = v0 * sp.cos(ang) * t
    y = v0 * sp.sin(ang) * t - (1/2) * g * t**2
    T = (2 * v0 * sp.sin(ang)) / g
    R = (v0**2 * sp.sin(2*ang)) / g
    return {
        "x(t)": x,
        "y(t)": y,
        "Tiempo_vuelo": float(T),
        "Rango": float(R)
    }

def resolver_caida_libre(p):
    g = p.get("g", 9.81)
    h = p.get("h", 10)
    t = math.sqrt(2*h/g)
    v = g*t
    return {
        "Tiempo_caida": round(t, 3),
        "Velocidad_final": round(v, 3)
    }
