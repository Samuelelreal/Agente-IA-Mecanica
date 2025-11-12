from mecai.parser import parse_enunciado
from mecai.solver import resolver_problema
from mecai.explain import generar_explicacion

if __name__ == "__main__":
    print("=== Agente de Mecánica Clásica (MECAI) ===")
    enunciado = input("Introduce el enunciado del problema:\n> ")

    datos = parse_enunciado(enunciado)
    solucion = resolver_problema(datos)
    explicacion = generar_explicacion(datos, solucion)

    print("\n--- DATOS EXTRAÍDOS ---")
    print(datos)
    print("\n--- RESULTADOS ---")
    print(solucion)
    print("\n--- EXPLICACIÓN ---")
    print(explicacion)
