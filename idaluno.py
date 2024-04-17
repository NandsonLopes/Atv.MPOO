from idendereço  import idendereço 


class idaluno(idendereço  ):
    def __init__(self, nome, idade, rua, cep, num):
        super().__init__(rua, num, cep)
        self.nome = nome
        self.notas= []
        self.idade = idade

    def getnome(self):
       return self.nome
    
    def setnome(self, novonome):
       self.nome = novonome

    def getidade(self):
       return self.idade
    
    def setidade(self, novaidade):
       self.idade = novaidade

    def getnotas(self):
       return self.notas
    
    def setnotas(self, notas):
       self.notas = notas

    def __str__(self):
       return f"name: {self.nome}\nidade: {self.idade}\nnotas: {self.notas}"


aluno = idaluno("Nandson", "23", "amelia", "0000000", "00")
print(aluno)
