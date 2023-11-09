class Alumno:
    def __init__(self, p_id_alumno, p_nombre, p_apellido, p_genero):
        self.codigo_identificador = p_id_alumno
        self.nombre = p_nombre
        self.apellido = p_apellido
        self.genero = p_genero

    def __str__(self):
        return f"Codigo {self.codigo_identificador} - Nombre y apellido: {self.nombre} {self.apellido} - Genero: {self.genero}"

    def obtener_codigo_identificador(self):
        return self.codigo_identificador

    def actualizar(self, nombre, apellido, genero):
        if nombre != '':
            self.nombre = nombre
        if apellido != '':
            self.apellido = apellido
        if genero != '':
            self.genero = genero