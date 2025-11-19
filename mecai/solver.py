import math
import sympy as sp

def resolver_problema(params: dict) -> dict:
    """Resuelve problemas simples según el tipo detectado."""
    tipo = params.get("tipo", "desconocido")
    if tipo == "proyectil":
        return resolver_proyectil(params)
    elif tipo == "caida_libre":
        return resolver_caida_libre(params)
    elif tipo == "mrua":
        return resolver_mrua(params)
    elif tipo == "oscilatorio":
        return resolver_oscilatorio(params)
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
    
def resolver_mrua(params):
    """Resuelve problemas básicos de MRUA."""
    v0 = float(params.get("v0", 0))
    a = float(params.get("a", 0))
    t = float(params.get("t", 0))

    x = v0 * t + 0.5 * a * t**2
    vf = v0 + a * t

    return {
        "posición (m)": round(x, 3),
        "velocidad final (m/s)": round(vf, 3)
    }


def resolver_oscilatorio(params):
    """Movimiento armónico simple: x(t)=A cos(wt + φ)."""
    import math

    A = float(params.get("A", 1))
    w = float(params.get("w", 1))
    phi = float(params.get("phi", 0))
    t = float(params.get("t", 0))

    x = A * math.cos(w * t + phi)
    v = -A * w * math.sin(w * t + phi)

    return {
        "posición (m)": round(x, 3),
        "velocidad (m/s)": round(v, 3)
    }

