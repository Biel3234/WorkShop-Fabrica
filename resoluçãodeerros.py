# def somar(a, b):
#     return a + b

# resultado = somar(10, 5)
# print(resultado)





#ERRO CORRIGIDO COM O EXCEPT INDEXERROR E O VALUEERROR
try:
     numeros = [10, 20, 30]
     indice = int(input("Digite um índice para acessar a lista: "))
     indice = int

     print(numeros[indice])

except IndexError:
     print("Erro!!! Valor escolhido nao esta armazenado na memoria")
except ValueError:
    print("ERRO!!! Valor invalido")






#ERRO RESOLVIDO COM TRY EXCEPT ZERODIVISIONERROR E O VALUEERROR
def dividir(a, b):
    return a / b

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

try:
    resultado = dividir(int(num1), int(num2))
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("ERRO!!! Voce tentou dividir por 0")
except ValueError:
    print("ERRO!!! Valor invalido")





#ERRO RESOLVIDO COM O TRY EXCEPT KEY ERROR
dados = {
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo",
}
try:
    chave = input("Digite a chave que deseja acessar: ")
    print(f"O valor da chave '{chave}' é: {dados[chave]}")
except KeyError:
    print("Erro")

dados = {
     "nome": "Isaac",
     "idade": 25,
     "cidade": "São Paulo",
}
chave = input("Digite a chave que deseja acessar: ")
chave = dados.get("endereco", "Nao encontrado")

print(f"O valor da chave '{chave}' é: {dados[chave]}")



# ERRO CORRIGIDO COM UM LOOP
def validar_idade(idade):
        try:
            if idade < 0 or idade > 120:
                raise ValueError("A idade deve estar entre 0 e 120 anos!")  # Erro personalizado
            idade == False
            return f"Idade válida: {idade}"
        except ValueError as teste:
            idade == True
            print(teste)
while True:

    idade = int(input("Digite sua idade: "))
    print(validar_idade(idade))

    if  idade < 0 or idade > 120:
        continue
    else:
        break

