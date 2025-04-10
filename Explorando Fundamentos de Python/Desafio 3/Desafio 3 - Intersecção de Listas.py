# TODO: Crie uma função 'elementos_comuns' que receba duas listas de números inteiros separados por espaço:

def elementos_comuns():
    # Leitura das listas
    lista1 = input().split()
    lista2 = input().split()

    # Verifica se todas os elementos das listas podem ser convertidos para inteiros
    if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):

        # Conversão para inteiros
        lista1 = list(map(int, lista1))
        lista2 = list(map(int, lista2))

        # Criação de conjuntos
        set1 = set(lista1)
        set2 = set(lista2)

        # Interseção dos conjuntos
        elementos = list(set1.intersection(set2))

        print(f"Elementos comuns às duas listas: {elementos}")
    else:
        print("Entrada inválida.")

if __name__ == "__main__":
    elementos_comuns()
