'''8. Faça um editor de texto usando uma matriz, que forneça as seguintes funções:
    a. O texto do usuário deve ser lido até que uma linha em branco seja digitada.
    b. O usuário pode reimprimir seu texto digitando i.
    c. O usuário pode trocar duas linhas de lugar digitando t onde o editor pergunta
    os números das linhas a serem trocadas entre si.
    d. O usuário pode redigitar uma linha digitando r, onde o editor pergunta o
    número da linha a ser redigitada.
    e. O usuário pode sair do editor digitando s.
    f. Se o usuário digitar um comando que não se encaixe em nenhum caso acima,
    o editor avisa que o comando não existe.'''

print("¨" * 50)
print("EDITOR DE TEXTO:\n")

texto = []

# Pede ao usuário os textos:
print("Digite textos e digite ' ' para encerrar:\n")
print("¨" * 50)

while True:
    linhas = input("→ ")
    if linhas == "":
        break
    else:
        texto.append(linhas)

# Exibindo o editor de texto:


# Acesso aos comandos:
while True:
    print("." * 50)
    print('''Digite o comando desejado, sendo:
      i = Reimprime o texto;
      t = Troca linhas de lugar;
      r = Redigita uma linha;
      s = Sai do editor.''')
    print("." * 50)
    resposta = input("→ ").lower().strip()

    # Reimprime os textos
    if resposta == "i":
        print("-" * 50)
        print(texto)
        print("-" * 50)
    # Troca as linhas de lugar:
    elif resposta == "t":
        print("-" * 50)
        print("Quais textos você deseja trocar de lugar?\n")

        # Antes de exibir, ele enumera as linhas para o usuário escolher
        for i, linha in enumerate(texto):
            print(f"{i + 1}.", linha)
        
        # - 1 é para diminuir um elemento no índice. 

        while True:
            texto1 = int(input("Linha a ser trocada → ")) - 1
            texto2 = int(input("Por → ")) - 1

            # Muda o lugar da linha:
            if texto1 < len(texto) and texto2 < len(texto):
                texto[texto1], texto[texto2] = texto[texto2], texto[texto1]
                print("-" * 50)
                print("Os textos ficaram assim:")
                print(texto)
                break
            
            else:
                print("-" * 50)
                print("Você escolheu um índice inválido.")
                print("Digite novamente:")
                continue
        print("-" * 50)
    # Comando para redigitação: 
    elif resposta == "r":
        print("-" * 50)
        print("Qual texto você deseja redigitar?\n")

        # Antes de exibir, ele enumera as linhas para o usuário escolher
        for i, linha in enumerate(texto):
            print(f"{i + 1}.", linha)
        
        # Comando para redigitação:

        while True:
            respostaRedigitar = int(input("→ ")) - 1
            if respostaRedigitar >= 0 and respostaRedigitar < len(texto):
                novaLinha = input("Digite o conteúdo para a linha: ")
                texto[respostaRedigitar] = novaLinha
                print("Os textos ficaram assim:")
                print(texto)
                break
            else:
                print("Valor de índice inválido. Digite novamente.")
                continue
    # Comando 'S'
    elif resposta == "s":
        print("Saindo... Obrigado por utilizar o EDITOR DE TEXTO!")
        break
    
    # Caso o usuário digite um comando inexistente:
    else:
        print("Comando inválido. Digite novamente.")
        continue
    
    continuar = input("Deseja continuar editando? (Sim/Não) \n > ").lower()
    if continuar == "sim" or continuar == "s":
        continue
    elif continuar == "nao" or continuar == "não" or continuar == "n":
        print("Saindo... Obrigado por usar o EDITOR DE TEXTO.")
        break