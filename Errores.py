class Errores:

    def __init__(self,codigo,funcion,mensajee, excepccion):
        self.codigo = codigo
        self.funcion = funcion
        self.mensajee = mensajee
        self.excepccion = excepccion

    def codigo(self):
        return self.codigo

    def funcion(self):
        return self.funcion

    def mensaje(self):
        return self.mensaje

    def excepccion(self):
        return self.excepccion

    def imprimir(self):
        if len(self.excepccion) > 5:
            resumen = {"codigo": self.codigo, "funcion": self.funcion, "mensajee": self.mensajee, "excepccion": "excepccion[1]"}
        else:
            resumen = {"codigo": self.codigo, "funcion": self.funcion, "mensajee": self.mensajee, "excepccion": self.excepccion}
        return resumen

    def setcodigo(self,codigo):
        self.codigo = codigo

    def setfuncion(self, funcion):
        self.funcion = funcion

    def setmensaje(self, mensaje):
        self.mensaje = mensaje

    def setexcepccion(self, excepccion):
        self.excepccion = excepccion