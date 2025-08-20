'''
1. A população americana, em um determinado ano, ultrapassa a população brasileira.
No entanto, a taxa de crescimento aqui é de 4% ao ano e lá é de 2% ao ano. Faça um
programa para calcular em que ano a população brasileira irá ultrapassar a
americana.
'''

print("\n PROGRAMA PARA SABER A ULTRAPASSAGEM NATALIDADE BRASILEIRA: \n")

# Definindo váriaveis:
habitantes_eua = 340000000
habitantes_brasil = 212000000
ano_inicial = 2025 

# Definindo constantes:
TAXA_BRASIL = 1.04
TAXA_EUA = 1.02
 
print("No ano de 2025, a população americana ultrapassa a população brasileira.")

while habitantes_brasil < habitantes_eua:
    habitantes_brasil *= TAXA_BRASIL
    habitantes_eua *= TAXA_EUA
    ano_inicial += 1

    if habitantes_brasil >= habitantes_eua:
        print(f'''O ano em que a quantidade populacional brasileira ultraprassará a quantidade americana será {ano_inicial}.\n
              O Brasil terá {habitantes_brasil:.0f} pessoas, e os EUA terá {habitantes_eua:.0f} pessoas.''')