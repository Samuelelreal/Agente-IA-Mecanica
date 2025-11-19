def generar_explicacion(datos, solucion):
    tipo = datos.get("tipo", "desconocido")
    if "error" in solucion:
        return "Error: " + solucion["error"]

    if tipo == "proyectil":
        return (
            f"Se trata de un lanzamiento de proyectil con v₀ = {datos.get('v0','?')} m/s "
            f"y ángulo θ = {datos.get('angulo','?')}°. "
            f"Tiempo de vuelo ≈ {solucion.get('Tiempo_vuelo','?'):.2f} s "
            f"y alcance ≈ {solucion.get('Rango','?'):.2f} m."
        )
    elif tipo == "caida_libre":
        return (
            f"Cálculo de caída libre con g = {datos.get('g',9.81)} m/s². "
            f"Tiempo de caída ≈ {solucion.get('Tiempo_caida','?')} s, "
            f"velocidad al impacto ≈ {solucion.get('Velocidad_final','?')} m/s."
        )
    elif tipo == "mrua":
        return (
            f"Usamos la ecuación del MRUA: x = x0 + v0·t + ½·a·t².\n"
            f"x0 = {datos.get('x0',0.0)} m, v0 = {datos.get('v0',0.0)} m/s, a = {datos.get('a',0.0)} m/s², t = {datos.get('t',0.0)} s.\n"
            f"Posición final = {solucion.get('posicion_final_m')} m."
        )
    elif tipo == "oscilatorio":
        return (
            f"Movimiento armónico simple: x(t)=A cos(ω t + φ).\n"
            f"A = {datos.get('A',1.0)} m, ω = {datos.get('w',1.0)} rad/s, φ = {datos.get('phi',0.0)}, t = {datos.get('t',0.0)} s.\n"
            f"Posición = {solucion.get('posicion_m')} m."
        )
    else:
        return "No se pudo generar explicación para este tipo de problema."
