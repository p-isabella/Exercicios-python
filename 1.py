'''Dadas duas listas P1 e P2, ambas com n valores reais que representam as notas de
uma turma na prova 1 e na prova 2, respectivamente, escreva um programa que
calcule a média da turma nas provas 1 e 2, imprimindo em qual das provas a turma
obteve a melhor média.'''

print("PROGRAMA DE CÁLCULO DE MÉDIA DA TURMA:")

# Definindo listas:
notaP1 = []
notaP2 = []
# Acumulador:
acumuladorAluno = 0

while True:

    acumuladorAluno += 1

    # nota 1:
    inserirNotasP1 = float(input(f"Insira a nota do {acumuladorAluno} aluno na primeira prova:\n"))
    notaP1.append(inserirNotasP1)

    # nota 2:
    inserirNotasP2 = float(input(f"Insira a nota do {acumuladorAluno} aluno na primeira prova:\n"))
    notaP2.append(inserirNotasP2)

    # verificação se o usuário quer continuar a inserir notas:

    while True:

        continuar = input("Deseja continuar a inserção de notas? (S/N) \n").upper()

        if continuar == "S" or continuar == "SIM" or continuar == "NÃO" or continuar == "NAO" or continuar == "N":
            break
        else:
            print("Resposta inválida. Por digite SIM ou NÃO.")
            print("-" * 50)
        
    if continuar == "NÃO" or continuar == "NAO" or continuar == "N": 
        break

mediaP1 = sum(notaP1)/len(notaP1)
mediaP2 = sum(notaP2)/len(notaP2)

if mediaP1 > mediaP2:
    print(f"A turma se deu melhor na primeira avaliação. Sua média geral foi: {mediaP1}, enquanto a segunda avaliação obteve {mediaP2} de média.")
elif mediaP1 < mediaP2:
    print(f"A turma se deu melhor na primeira avaliação. Sua média geral foi: {mediaP2}, enquanto a segunda avaliação obteve {mediaP1} de média.")
else:
    print("As médias são iguais.")