from idendereço import idendereço 

class idprofessor (idendereço  ):
    def __init__(self, nome, rua, num, cep):
      self.nome = nome
      super().__init__(rua, num, cep)

    def getnome(self):
       return self.nome
    
    def setnome(self, novonome):
       self.nome = novonome

    def __str__(self):
       return f"nome: {self.nome}"

professor = idprofessor("nandson", "00", "1", "59009898")
print(professor)
