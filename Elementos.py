class Elementos:


    def __init__(self):
        self.tipo = "N/A"
        self.valor = "N/A"
        self.fondo = "N/A"
        self.valores = "N/A"
        self.evento = "N/A"
        self.obs = "N/A"
    
    #### [ GET ] ####

    def tipo(self):
        return self.tipo

    def valor(self):
        return self.valor
    
    def fondo(self):
        return self.fondo
    
    def valores(self):
        return self.valores
    
    def evento(self):
        return self.evento
    
    def obs(self):
        return self.obs
    
    #### [ SET ] ####

    def settipo(self,tipo):
        self.tipo = tipo
        return "ok"
    
    def setvalor(self,valor):
        self.valor = valor
        return "ok"
    
    def setfondo(self,fondo):
        self.fondo = fondo
        return "ok"
    
    def setvalores(self,valores):
        self.valores = valores
        return "ok"
    
    def setevento(self,evento):
        self.evento = evento
        return "ok"     

    def setobs(self,obs):
        self.obs = obs  
        return "ok"
    
    #### [ Imprimir ] ####

    def imprimir(self):
        resumen = {"tipo": str(self.tipo), "valor": self.valor, "fondo": self.fondo, "valores": self.valores, "evento": self.evento, "obs": self.obs}
        return resumen