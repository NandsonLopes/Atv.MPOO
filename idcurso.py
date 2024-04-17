class idcurso:
    def __init__(self, nome, disciplina=None):
        self.nome = nome
        self.disciplina = disciplina if disciplina is not None else []

    def getnome(self):
        return self.nome
    
    def setnome(self, novonome):
        self.nome = novonome

    def getdisciplina(self):
        return self.disciplina
    
    def setdisciplina(self, novadisciplina):
        self.disciplina = novadisciplina

    def add_disciplina(self, nova_disciplina):
        self.disciplina.append(nova_disciplina)

    def __str__(self):
        disciplinas = ", ".join([str(cod) for cod in self.disciplina])
        return f"nome: {self.nome}\ndisciplina subjects: {disciplinas}"

class Disciplina:
    def __init__(self, nome, creditos):
        self.nome = nome
        self.creditos = creditos

    def __str__(self):
        return f"Disciplina: {self.nome}, Créditos: {self.creditos}"

curso = idcurso("Bacharelado em Sistemas de informação")
curso.add_disciplina(Disciplina("MPOO", 15))
print(curso)