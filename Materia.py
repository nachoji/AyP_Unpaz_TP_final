class Materia:
    def __init__(self, p_id_materia, p_nombre, p_correlativas):
        self.__codigo_identificador = p_id_materia
        self.nombre = p_nombre
        self.correlativas = p_correlativas

    def __str__(self):
        return f"Codigo {self.__codigo_identificador} - Nombre: {self.nombre} - Correlativas: {self.correlativas}"

    def obtener_codigo_identificador(self):
        return self.__codigo_identificador

    def obtener_correlativa(self):
        return self.correlativas

    def actualizar(self, nombre, correlativa):
        if nombre != '':
            self.nombre = nombre
        if correlativa != '':
            self.correlativas = correlativa