'''2. Um dado material radioativo perde metade de sua massa a cada 50 s. Dada a massa
inicial em gramas, fazer um algoritmo que determine o tempo necessário para que
essa massa seja menor que 0,5g. '''

# CONSTANTES:

MASSA_FINAL = 0.5


# INÍCIO:

print("PROGRAMA QUE DEFINE A DECADÊNCIA DE UM MATERIAL RADIOATIVO: \n ")


while True:
    massa_inicial = input("Insira a quantidade aproximadamente da massa em gramas: ").replace(",", ".")

    tempo_final = 0
    # Verificação de número:
    if massa_inicial.count(".") > 1 or massa_inicial.isalpha() == True:
        print("Por favor, insira um número válido.")
    else:
            massa_inicial = float(massa_inicial)
            if massa_inicial > MASSA_FINAL:
                while massa_inicial > MASSA_FINAL:
                    massa_inicial /= 2
                    tempo_final += 50
                print(f"O tempo necessário para que haja decadência radioativa é de: {tempo_final} segundos.")
            else:   
                print("Não é necessário tempo para decadência radioativa. A massa é menor do que 0,5 gramas.")