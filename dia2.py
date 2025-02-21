num1 = float(input("Insira o primeiro numero: "))
num2 = float(input("Insira o segundo numero: "))

soma = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2


opera = str (input("Escolha a operacão para fazer o calculo: "))

if opera == "+" and len(opera) == 1:
    print ("Resultado da soma: ", soma)
    dec = (input("Voce deseja adicionar mais um numero? "))
    while dec == "sim":
        novo_num = float(input("Digite o novo numero: "))
        resultado = soma = soma + novo_num
        print("Resultado: ", resultado)
        dec.lower = str(input("Voce deseja adicionar mais um numero? "))

elif opera == "*" and len(opera) == 1:
    print ("Resultado da multiplicação: ", mult)
elif opera == "/" and len(opera) == 1:
    print ("Resultado da divisão: ", div)
else:
    print("Operação invalida!!!")