'''3. Para fazer o balanço mensal de um armazém, faça um programa que que leia para um
número qualquer de mercadorias diferentes o preço de custo, o preço de venda e a
quantidade vendida. A partir desses dados imprima: o número total de mercadorias
diferentes lidas, o faturamento total e o lucro total do armazém.'''

# ACUMULADORES:

acumulador_custo = 0
acumulador_faturamento = 0

# INICIO 

print("-" * 50)
print("PROGRAMA PARA BALANÇO MENSAL DE UM ARMAZÉM:")


# Cria-se uma lista para armazenar as diferentes mercadorias do cliente:
listaMercadoria = []

# Enquanto houver mercadorias, ele fica no looping:

while True:

    print("-" * 50)
    mercadoriaNome = input("Insira o nome da mercadoria ou do seu código: ")

    mercadoria_preco_custo = input("Insira o preço de custo: ").replace(",",".")
    if mercadoria_preco_custo.count(".") > 1:
        print("Insira um número válido.")
        print("-" * 50)
        continue
    else:
        mercadoria_preco_custo = float(mercadoria_preco_custo)
        if mercadoria_preco_custo < 0:
            print("Insira um valor positivo!")
            print("-" * 50)
            continue
        else:
            mercadoria_faturamento = input("Insira o preço de venda: ").replace(",",".")
            if mercadoria_faturamento.count(".") > 1:
                    print("Insira um número válido.")
                    print("-" * 50)
                    continue
            else:
                    mercadoria_faturamento = float(mercadoria_faturamento)
                    if mercadoria_faturamento < 0:
                        print("Insira um valor positivo!")
                        print("-" * 50)
                        continue
                    else:
                        mercadoria_quantidade = input(f"Digite a quantidade vendida de {mercadoriaNome}: ").replace(",",".")
                        if mercadoria_quantidade.count(".") >= 1:
                            print("Insira um número válido.")
                            print("-" * 50)
                            continue
                        else:
                            mercadoria_quantidade = int(mercadoria_quantidade)
                            if mercadoria_quantidade < 0:
                                  print("Insira um valor positivo.")
                                  print("-" * 50)
                            else:
                                if not mercadoriaNome in listaMercadoria:
                                    listaMercadoria.append(mercadoriaNome)
                                
                                acumulador_custo += mercadoria_preco_custo * mercadoria_quantidade
                                acumulador_faturamento += mercadoria_faturamento * mercadoria_quantidade

                                resposta = str(input("Deseja acrescentar mais itens? ")).lower().strip()
                                if resposta == "sim" or resposta == "s":
                                    continue
                                elif resposta == "nao" or resposta == "não" or resposta == "n":
                                     break
                                else:
                                    print("Não entendi a palavra. Irei encerrar o programa.")
                                     

print("_" * 50)
quantidadeMercadoria = len(listaMercadoria)
print("A quantidade de mercadorias diferentes adicionados são:", quantidadeMercadoria)

print("O faturamento do comércio foi de: ", acumulador_faturamento)

lucro = acumulador_faturamento - acumulador_custo
print(f"O lucro total é: {lucro}.")