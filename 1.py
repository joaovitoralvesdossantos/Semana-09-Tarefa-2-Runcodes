# Verifica qual é o dia da semana
def semana(dia):
    if dia == 1: 
        return "domingo"
    elif dia == 2: 
        return "segunda-feira"
    elif dia == 3: 
        return "terça-feira"
    elif dia == 4: 
        return "quarta-feira"
    elif dia == 5: 
        return "quinta-feira"
    elif dia == 6: 
        return "sexta-feira"
    elif dia == 7: 
        return "sábado"
    else:
        return "valor inválido"

# Função principal
def main():

    #entrada de dados
    dia = int(input("Digite um número entre 1-7: "))
    
    #processamento
    dias = semana(dia)
    
    #saida de dados
    print(f"O dia escolhido foi: {dias}")

# Chama a função principal
if __name__ == '__main__':
    main()