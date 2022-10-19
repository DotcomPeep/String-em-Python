url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
print(url) # pegando url de um site de troca de moeda

url_base = url[0:27]
print(url_base) # pegando o url básico do site --> 0 é a primeira posição e 27 é o "?" (https...?) o "?" não é
# adicionado pois, 0 é uma posição inclusiva e a partir da posição 1 é exclusiva logo se chamar 
# url_base = url[0:1] ou url_base = url[0] ele trará "h" mas, se chamar url_base = url[0:2] ele trará "ht" e 
# assim por diante...

url_parametros = url[28:79]
print(url_parametros)