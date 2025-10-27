# Calcula o valor do kg e aplica um desconto se for maior que 5kg
def calcular_preco(morango_kg, maca_kg):
    # preços 
    if morango_kg <= 5:
        preco_morango = 2.50
    else:
        preco_morango = 2.20

    if maca_kg <= 5:
        preco_maca = 1.80
    else:
        preco_maca = 1.50

    # calcula valores
    total_morango = morango_kg * preco_morango
    total_maca = maca_kg * preco_maca

    # soma total
    total_kg = morango_kg + maca_kg
    total = total_morango + total_maca

    #desconto 
    if total_kg > 8 or total > 25:
        total *= 0.9  

    return total

# Função principal
def main():

    #entrada de dados
    morango = float(input("Digite a quantidade de morangos (kg): "))
    maca = float(input("Digite a quantidade de maças (kg): "))

    #processamento
    valor_a_pagar = calcular_preco(morango, maca)

    #saida de dados
    print(f"O valor total da compra é: {valor_a_pagar:.2f}")

# Chama a função principal
if __name__ == '__main__':
    main()