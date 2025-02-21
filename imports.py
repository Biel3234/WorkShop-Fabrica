import math
import random
import requests
import json

# num1= "asd"
# print (math.sqrt(25))

# print (random.randint(1, 20))

resposta = requests.get("https://parallelum.com.br/fipe/api/v1/carros/marcas")

# Exibe o código de status da resposta
print("Status da Requisição:", resposta.status_code)



