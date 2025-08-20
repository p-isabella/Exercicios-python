'''6. Alterar o programa anterior para só contar caracteres diferentes de espaço em branco
e tabulação. '''

# PROGRAMA ANTERIOR:

'''5. Construir um programa que leia um conjunto de caracteres (uma frase, terminada por
“Enter”) da entrada padrão e ao final imprima o número de caracteres lidos.'''

while True:

    print("-" * 50)
    print(" " * 19, "𝗖𝗢𝗡𝗧𝗔𝗗𝗢𝗥")
    print("-" * 50)

    frase = input("Insira uma frase e quando terminar. Digite “Enter”: \n")
    frase = "".join(frase.split())    
    
    acumulador = 0

    for char in frase:
        acumulador += 1

    print(f"Sua frase possui {acumulador} caracteres.")
    print("-" * 50)
    
    continuar = input("Deseja continuar a escrever? (Sim/Não): \n").lower().strip()
    
    if continuar == "nao" or continuar == "não":
        print("Obrigado por utilizar o programa.")
        print("-" * 50)
        break
    elif continuar == "sim":
        print("-" * 50)
        continue
    else:
        print("Devido a entrada incorreta, iremos reiniciar o programa.")
        print("-" * 50)
        continue