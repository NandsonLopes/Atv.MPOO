from idendereço import idendereço 

class idprofessor (idendereço  ):
    def __init__(self, name, street, number, zipCode):
      self.name = name
      super().__init__(street, number, zipCode)

    def getName(self):
       return self.name
    
    def setName(self, newName):
       self.name = newName

    def __str__(self):
       return f"name: {self.name}"

professor = idprofessor("nandson", "00", "1", "5")
print(professor)