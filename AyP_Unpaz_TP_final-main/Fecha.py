from datetime import date


class Fecha:
    def __init__(self, p_dia, p_mes, p_anio):
        if isinstance(p_dia, int) and isinstance(p_mes, int) and isinstance(p_anio, int):
            if 0 < p_dia <= 31 and 0 < p_mes <= 12 and 1900 <= p_anio <= 2100:
                self.fecha = date(p_anio, p_mes, p_dia)
            else:
                raise AttributeError(
                    f"El día debe estar entre 1 - 31, el mes entre 1 - 12 y el año entre 1900 - 2100. Valores ingresados p_dia={p_dia} p_mes={p_mes} p_año={p_anio}")
        else:
            raise AttributeError(
                f"Dia, Mes y Año deben ser del tipo int. Sin embargo son p_dia={type(p_dia)} p_mes={type(p_mes)} p_año={type(p_anio)}")

    def __str__(self):
        return self.fecha.strftime('%d/%m/%y')

    def __eq__(self, other):
        if isinstance(other, Fecha):
            return self.fecha == other.fecha
        raise AttributeError(f"El parámetro other debe ser un objeto Fecha, en cambio se paso un objeto {type(other)}")

    def __lt__(self, other):
        if isinstance(other, Fecha):
            return self.fecha < other.fecha
        raise AttributeError(f"El parámetro other debe ser un objeto Fecha, en cambio se paso un objeto {type(other)}")

    def __le__(self, other):
        if isinstance(other, Fecha):
            return self.fecha <= other.fecha
        raise AttributeError(f"El parámetro other debe ser un objeto Fecha, en cambio se paso un objeto {type(other)}")

    def __gt__(self, other):
        if isinstance(other, Fecha):
            return self.fecha > other.fecha
        raise AttributeError(f"El parámetro other debe ser un objeto Fecha, en cambio se paso un objeto {type(other)}")

    def __ge__(self, other):
        if isinstance(other, Fecha):
            return self.fecha >= other.fecha
        raise AttributeError(f"El parámetro other debe ser un objeto Fecha, en cambio se paso un objeto {type(other)}")
