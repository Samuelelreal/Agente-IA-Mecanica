from pint import UnitRegistry
ureg = UnitRegistry()

def verificar_unidades(expr):
    """Ejemplo de verificación dimensional básica."""
    try:
        return expr.check('[length]')
    except Exception:
        return False
