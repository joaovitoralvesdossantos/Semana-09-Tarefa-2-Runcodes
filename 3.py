# Verifica se a data é valida
def data(data_int):

# pega o dia mes e ano do DDMMAAAA
    dia = data_int // 1000000        
    mes = (data_int % 1000000) // 10000 
    ano = data_int % 10000  

# verifica se o ano vai de janeiro aet feveiro
    if mes < 1 or mes > 12:
        return False
# se o numero do ano for menor que zero é invalido        
    if ano <= 0:
        return False

# verifica se o ano é bissexto
    e_bissexto = False 

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        e_bissexto = True

    dias_no_mes = 0
# meses com 31 dias
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        dias_no_mes = 31
# meses com 30 dias
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dias_no_mes = 30

# fevereiro
    elif mes == 2:
        if e_bissexto:
            dias_no_mes = 29
        else:
            dias_no_mes = 28
# o numero minimo do dia é setado em um e vai até 31            
    if dia >= 1 and dia <= dias_no_mes:
        return "A data inserida é válida"
    else:
        return "A data inserida é inválida"

# Função principal
def main():

    #entrada de dados
    ddmmaaaa = int(input("Digite uma data: (DDMMAAA): "))
    
    #processamento
    diamesano = data(ddmmaaaa)
    
    #saida de dados
    print(diamesano)

# Chama a função principal
if __name__ == '__main__':
    main()