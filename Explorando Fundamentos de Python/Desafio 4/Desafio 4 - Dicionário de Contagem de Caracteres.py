def contar_caracteres(string):
#TODO: Inicialize um dicionário vazio 'contador' para armazenar as contagens de caracteres.:
  dicionario = {}
#TODO: Itere através de cada caractere na string string.
  for i in string:
    if i in dicionario:
      dicionario[i] += 1  # Se já existe, incrementa
    else:
      dicionario[i] = 1
  
  return dicionario
#TODO: Para cada caractere, verifique se ele já está presente no dicionário contador:

  
# Solicita entrada do usuário
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)
