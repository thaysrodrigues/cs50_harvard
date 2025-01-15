# ==================== Seleção Aleatória de Cartas ====================
import random

cards = ["jack", "queen", "king"]


def main():
    # Deixa os resultados sejam sempre os mesmos em cada execução
    random.seed(1)

    # Seleciona 10 cartas aleatórias da lista, permitindo repetições
    print(random.choices(cards, k=10))

    # A probabilidade de jack ser escolhido é 75%,
    # sendo queen 20%, e king de 5%.
    # print(random.choices(cards, weights=[75, 20, 5], k=2))

    # Seleção de 2 cartas únicas (sem repetição)
    # print(random.sample(cards, k=2))


if __name__ == "__main__":
    main()
