'''4. Faça um programa que calcule o Máximo Divisor Comum entre dois números. '''

print("PROGRAMA QUE CALCULA O MÁXIMO DIVISOR COMUM ENTRE DOIS NÚMEROS:")

while True:

    primeiro_numero = int(input("Insira um número positivo e inteiro para continuar: "))
    if primeiro_numero <= 0:
        print("-" * 50)
        print("Não é possível adicionar números negativos.")
        print("-" * 50)
        continue

    segundo_numero = int(input("Insira outro número positivo e inteiro para continuar: "))
    if segundo_numero <= 0:
        print("-" * 50)
        print("Não é possível adicionar números negativos. Tente novamente.")
        print("-" * 50)
        continue
    
    break

while segundo_numero != 0:
    primeiro_numero, segundo_numero = segundo_numero, primeiro_numero % segundo_numero
    # Na solução seguinte, utiliza-se o Algoritmo de Euclides, que diz:
    # O MDC entre dois números é sempre o MDC de B e o resto (%) da divisão entre A e B;
    # Isso significa que A sempre se torna o valor de B e B se torna o resto da divisão de a por b.
    # No caso do programa, o MDC será o MDC do segundo_numero e o resto (%) da divisão entre o primeiro_numero e segundo_numero.
    # SEMPRE EM MÓDULO; o que significa que não importa se segundo_numero é maior do que primeiro_numero. Ele sempre
    # realizará a operação corretamente. Essa divisão ocorrerá até que B se torne 0.

print(f"O MDC entre os números escolhidos é: {primeiro_numero}.")