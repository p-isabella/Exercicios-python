'''Defina uma matriz de caracteres para guardar um texto para fazer um editor de texto
que leia as várias linhas dadas pelo usuário e quando este digitar uma linha em
branco, reescreva o texto do usuário e imprima as seguintes estatísticas do texto:
número de caracteres digitados, número de espaços em branco e número de linhas.'''

texto = []

# Laço de repetição para inserção de texto:
print('''𝗘𝗗𝗜𝗧𝗢𝗥 𝗗𝗘 𝗧𝗘𝗫𝗧𝗢: \n''')

while True:
    linha = input("Digite um texto: ")
    if linha == "":
        break
    texto.append(linha)

    print("Você digitou as seguintes frases:")
    for linha in texto:
        print(linha)

# Variáveis de leitura:

num_linhas = len(texto)
num_caracteres = sum(len(linha) for linha in texto)
num_espacoBranco = sum(linha.count(" ") for linha in texto)

# Exibindo ao usuário:

print(f"O número de linhas foi: {num_linhas}.")
print(f"O número de caracteres foi: {num_caracteres}.")
print(f"O número de espaços em branco foi: {num_espacoBranco}.")