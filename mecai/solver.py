import math
import sympy as sp  # si ya lo usas para proyectil está bien mantenerlo

def resolver_problema(params: dict) -> dict:
    """Dispatch según tipo."""
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
    # (mantén tu implementación existente)
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


def resolver_mrua(p):
    """
    Calcula posición final x = x0 + v0*t + 1/2*a*t^2
    Asume unidades SI (m, s, m/s, m/s^2).
    """

    try:
        v0 = float(p.get("v0", 0.0))
        a = float(p.get("a", 0.0))
        t = float(p.get("t", 0.0))
        x0 = float(p.get("x0", 0.0))
    except (TypeError, ValueError):
        return {"error": "Valores numéricos inválidos para v0, a o t."}

    # Validaciones básicas
    if t <= 0:
        # Si t==0 devolvemos la pos inicial
        x = x0
    else:
        x = x0 + v0 * t + 0.5 * a * t**2

    return {
        "posicion_final_m": round(x, 6),
        "unidad": "m",
        "metodo": "x = x0 + v0*t + 1/2*a*t^2"
    }


def resolver_oscilatorio(p):
    """Movimiento armónico simple: x(t)=A cos(w t + phi) — calcula posición a un tiempo t."""
    A = float(p.get("A", 1.0))
    w = float(p.get("w", 1.0))
    phi = float(p.get("phi", 0.0))
    t = float(p.get("t", 0.0))
    x = A * math.cos(w * t + phi)
    return {
        "posicion_m": round(x, 6),
        "unidad": "m",
        "metodo": "x(t) = A cos(ω t + φ)"
    }
