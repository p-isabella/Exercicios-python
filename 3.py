'''
print("nota da turma:")
notatotal = 0

for i in range(6):
    nota = float(input("Nota do aluno"))
    notatotal = notatotal + nota

media = notatotal/5
print(media)
'''
'''
notatotal = []

for i in range(4):
    nota = float(input(f"Nota do aluno {i}"))
    notatotal.append(nota)

notatotal = sum(notatotal)/5
print(notatotal)
'''
'''
concatenar = 0
for i in range(2):
    teste = int(input("insira um numero"))
    concatenar = teste

print(concatenar)
'''
'''
n = 0
maior = n
menor = n

while n != -5:
    n = int(input("numero enquanto nao for -5"))
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print(maior, menor)
'''
'''
print("f para c")

graus = 50

for i in range(100):
    celsius = (graus - 32)/1.8
    print(celsius, graus)
    graus += 1
'''
'''
i = 1
h = 1

for i in range(10):
    if i % 2 == 0:
        n1 = (-1 * i)
    else:
        n1 = i

    if n1 != 0:    
        n2 = i**2 
        h = (n1/n2)

    print(h)
'''

vetor1 = [] 
vetor2 = []
vetor3 = []

for i in range(9):
    valor1 = int(input(f"Insira um valor vet1: {i+1} "))
    vetor1.append(valor1)


for i in range(9):
    valor2 = int(input(f"Insira um valor vet2: {i+1}"))
    vetor2.append(valor2)

i = 0
for i in range (9):
   vetor3.append(vetor1[i])
   vetor3.append(vetor2[i])
    
print(vetor3)
