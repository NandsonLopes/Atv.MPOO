class Disciplina:
    def __init__(self, nome, codigo, sala, professor, alunos=None):
        self.nome = nome
        self.codigo = codigo
        self.sala = sala
        self.professor = professor
        self.alunos = alunos if alunos is not None else []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def __str__(self):
        alunos_str = ", ".join(self.alunos)
        return f"Disciplina: {self.nome}\nCódigo: {self.codigo}\nSala: {self.sala}\nProfessor: {self.professor}\nAlunos: {alunos_str}"

disciplina = Disciplina("Matemática", "MAT101", "Sala 101", "Prof. Silva", ["João", "Maria"])
print(disciplina)
disciplina.adicionar_aluno("Pedro")
print(disciplina)
    