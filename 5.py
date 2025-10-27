# Verifica a quantidades de sim em uma lista e retorna uma mensagem
def perguntas(respostas):

    quantidade_de_sim = sum(1 for item in respostas if item == 'S')

    if quantidade_de_sim == 5:
        return "Você é o Assassino!"
    elif quantidade_de_sim >= 3:
        return "Você é Cúmplice!"
    elif quantidade_de_sim == 2:
        return "Você é Suspeito!"
    else:
        return "Você é Inocente!"

# Função principal
def main():

    #entrada de dados
    print("Considere “S” para sim ou “N” para não.")
    pergunta_1 = input("Telefonou para a vítima ?: ").strip()
    pergunta_2 = input("Esteve no local do crime ?: ").strip()
    pergunta_3 = input("Mora perto da vítima ?: ").strip()
    pergunta_4 = input("Devia para a vítima ?: ").strip()
    pergunta_5 = input("Já trabalhou com a vítima ?: ").strip()

    #processamento
    respostas = [pergunta_1, pergunta_2, pergunta_3, pergunta_4, pergunta_5]
    resultado = perguntas(respostas)

    #saida de dados
    print(resultado)

# Chama a função principal
if __name__ == '__main__':
    main()