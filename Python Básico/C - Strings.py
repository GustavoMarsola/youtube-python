# Funções bem úteis das strings

# 1) replace

frase_errada = 'O CORINTHIANS É O MELHOR TIME DO BRASIL'
frase_correta = frase_errada.replace('CORINTHIANS', 'SÃO PAULO')
# print(frase_correta)


# 2) isnumeric

cpf = '123.456.789-00'

# print(cpf.isnumeric()) # False, pois tem pontos e hífen

cpf = '12345678900'

# print(cpf.isnumeric()) # True, pois contém somente números

# 3) lower e upper

cidade1 = "Osasco"    
cidade2 = "OSASCO"

conferir_cidades = cidade1 == cidade2

print('É a mesma cidade: ', conferir_cidades)
print('Cidade 1: ', cidade1)
print('Cidade 2: ', cidade2)