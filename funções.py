
# def soma(num1, num2):
#     return (num1 + num2)

# print ("Resultado com valores escolhidos por usuario: ", soma(int(input("digite um numero")), int(input("digite um numero"))))

# print ("Resultado com valores pre definidos: ", soma(5, 6))















# class Pessoa
#:
#     def __init__ (self, nome, idade, peso, altura):
#         self.nome = nome
#         self.idade = idade
#         self.peso = peso
#         self.altura = altura  
#     def apresentar(self):
#         print(f"Ola, meu nome é {self.nome} e eu tenho {self.idade} anos.")
        
#     def calcular_imc(self):
#             imc = self.peso / (self.altura ** 2)
#             return imc

# p1 = Pessoa
#("Pedro", 25, 70, 1.75)
# p1.apresentar()
# print (f"Meu imc é {p1.calcular_imc():.2f}")


class Creatina:
    def __init__ (self, peso, nome):
        self.peso
        self.nome
        
    def calcular_creatina(self):
        return self.peso * 0.03
    
    def apresentar(self):
        print (f"Ola, seu nome é {self.nome} e seu peso é peso{self.peso}")
        
p1 = Creatina(85, "Pedro")
p1.apresentar()
print("O tando de creatina que você deve tomar é: ", p1.calcular_creatina)
