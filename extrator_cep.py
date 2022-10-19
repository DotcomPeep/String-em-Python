import re

endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

# o "?" após os colchetes significa que o hífen é opcional, para casos onde o cep não está com hífen,
# o programa ainda o encontrará
padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")

# Outra forma de encontrar o cep
# padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")

busca = padrao.search(endereco) # Match

if busca:
    cep = busca.group()
    print(cep)