class Sala:
    def __init__(self, numero, limite):
        self.numero = numero
        self.limite = limite

    def get_numero(self):
       return self.numero
    
    def set_numero(self, novo_numero):
       self.numero = novo_numero

    def get_limite(self):
       return self.limite
    
    def set_limite(self, novo_limite):
       self.limite = novo_limite

    def __str__(self):
       return f"Número da sala: {self.numero}\nLimite de alunos: {self.limite}"

sala = Sala(1, 10)
print(sala)