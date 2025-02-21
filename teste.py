class Pessoa:
    def __init__(self, peso, nome):
        self.peso
        self.nome
        
    def calcular_creatina(self):
        return self.peso * 0.03
    
    def apresentar(self):
        print (f"Ola, seu nome é {self.nome} e seu peso é peso{self.peso}")
        
p1 = Pessoa("Pedro", 75)

p1.apresentar()
