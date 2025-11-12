from mecai.solver import resolver_proyectil

def test_proyectil():
    p = {"v0": 10, "angulo": 45, "g": 9.81}
    res = resolver_proyectil(p)
    assert round(res["Rango"], 2) == round((10**2 * 0.7071 * 2 * 0.7071) / 9.81, 2)
