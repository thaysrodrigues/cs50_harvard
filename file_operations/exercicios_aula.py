# # ==================== Parte 1: Coletar e armazenar nomes ====================

# # Armazena os nomes
# names = []

# # Coleta 3 nomes do usuário e armazena na lista
# for _ in range(3):
#     names.append(input("What's your name? "))

# # Imprimir os nomes coletados, ordenados em ordem alfabética
# for name in sorted(names):
#     print(f"Hello, {name}")

# # ==================== Parte 2: Gravar nome no arquivo ====================

# # Coleta o nome do usuário
# name = input("What's your name? ")

# # Abre o arquivo names.txt no modo de escrita e gravando o nome
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")  # Adiciona o nome no final do arquivo com uma nova linha

# # ==================== Parte 3: Ler e exibir nomes do arquivo ====================

# # Lê o conteúdo do arquivo names.txt e exibe os nomes com saudação
# with open("names.txt", "r") as file:
#     for line in file:
#         print("Hello,", line.rstrip())  # rstrip() remove a nova linha no final

# # ==================== Parte 4: Organizar e exibir nomes do arquivo ====================

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())  # Remove espaços extras e inclui a nova linha

for name in sorted(names):
    print(f"Hello, {name}")
