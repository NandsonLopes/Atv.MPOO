class idendereço  :
    def __init__(self, rua, num, cep):
      self.rua = rua
      self.num = num
      self.cep = cep
    
    def getrua(self):
       return self.rua
    
    def setrua(self, novarua):
        self.rua= novarua

    def getnum(self):
       return self.num
    
    def getcep(self):
       return self.cep
    
    def __str__(self):
       return f"rua: {self.rua}\nnum: {self.num}\ncep:{self.cep}"
    
endereço = idendereço  ("rua", 00, )
print(endereço)