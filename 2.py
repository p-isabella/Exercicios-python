'''Dadas duas listas L1 e L2, com n e m valores inteiros, respectivamente, escreva um
programa que concatene as listas L1 e L2 em uma nova lista L3. Em seguida, imprima
a lista L3 ordenada de maneira crescente e decrescente.'''

# Definindo listas e acumulador:

lista1 = []
lista2 = []
acumuladorValor = 0

while True:
    
    # Acumulador de valores:

    acumuladorValor += 1

    # Inserindo os valores:

    valorL1 = input(f"{acumuladorValor} - Insira um valor inteiro para a lista 1: \n")
    if valorL1.startswith("-") and valorL1[1:].isdigit() or valorL1.isdigit():
        valorL1 = int(valorL1)
        lista1.append(valorL1)
    else:
        print("Valor inválido. Digite um valor INTEIRO.")
        continue
    
    valorL2 = input(f"{acumuladorValor} - Insira um valor inteiro para a lista 2: \n")
    if valorL2.startswith("-") and valorL2[1:].isdigit() or valorL2.isdigit():
        valorL2 = int(valorL2)
        lista2.append(valorL2)
    else:
        print("Valor inválido. Digite um valor INTEIRO.")
        continue
    # Verificar se a pessoa quer inserir mais números:

    while True:

        continuar = input("Deseja continuar a inserção de números? (S/N) \n").upper()

        if continuar == "S" or continuar == "SIM" or continuar == "NÃO" or continuar == "NAO" or continuar == "N":
            break
        else:
            print("Resposta inválida. Por digite SIM ou NÃO.")
            print("-" * 50)
        
    if continuar == "NÃO" or continuar == "NAO" or continuar == "N": 
        break

# Imprimindo os resultados:

lista3 = []
lista3 = lista2 + lista1
lista3.sort()
print("Os valores em ordem crescente:")
print(lista3)

print("-" * 45)

lista3.sort(reverse=True)
print("Os valores em ordem decrescente:")
print(lista3)