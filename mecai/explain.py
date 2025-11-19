def generar_explicacion(datos, solucion):
    tipo = datos.get("tipo", "desconocido")
    if tipo == "proyectil":
        return (
            f"Se trata de un lanzamiento de proyectil con velocidad inicial v₀ = {datos.get('v0', '?')} m/s "
            f"y ángulo θ = {datos.get('angulo', '?')}°. "
            f"El tiempo total de vuelo es {solucion['Tiempo_vuelo']:.2f} s "
            f"y el alcance máximo es {solucion['Rango']:.2f} m."
        )
    elif tipo == "caida_libre":
        return (
            f"Se analizó una caída libre con aceleración g = {datos.get('g', 9.81)} m/s². "
            f"El tiempo de caída fue {solucion['Tiempo_caida']} s "
            f"y la velocidad al impactar fue {solucion['Velocidad_final']} m/s."
        )
    elif tipo == "mrua":
        return ("Usando las ecuaciones del MRUA: x = v0·t + 1/2·a·t² y vf = v0 + a·t")

    elif tipo == "oscilatorio":
        return ("Solución del movimiento armónico simple: x(t)=Acos(ωt+φ) y v(t)=-Aωsen(ωt+φ)")
    else:
        return "No se pudo generar explicación para este tipo de problema."
