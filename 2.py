# Ler um numero e escreve detalhamente o resultado
def escreve_numero(n):
    if n == 1:
        return "uma"
    elif n == 2:
        return "duas"
    elif n == 3:
        return "três"
    elif n == 4:
        return "quatro"
    elif n == 5:
        return "cinco"
    elif n == 6:
        return "seis"
    elif n == 7:
        return "sete"
    elif n == 8:
        return "oito"
    elif n == 9:
        return "nove"

def extenso(numero):
    

    centenas = numero // 100         
    dezenas = (numero % 100) // 10   
    unidades = numero % 10           

    texto_c = ""
    texto_d = ""
    texto_u = ""

    if centenas > 0:

        palavra_numero = escreve_numero(centenas) 
        
        if centenas == 1:
            texto_c = f"{palavra_numero} centena" 
        else:
            texto_c = f"{palavra_numero} centenas" 

    if dezenas > 0:
        palavra_numero = escreve_numero(dezenas) 
        
        if dezenas == 1:
            texto_d = f"{palavra_numero} dezena"
        else:
            texto_d = f"{palavra_numero} dezenas" 

    if unidades > 0:
        palavra_numero = escreve_numero(unidades) 
        
        if unidades == 1:
            texto_u = f"{palavra_numero} unidade" 
        else:
            texto_u = f"{palavra_numero} unidades"

    if texto_c != "" and texto_d != "" and texto_u != "":
        return f"{texto_c}, {texto_d} e {texto_u}."
    
    
    elif texto_c != "" and texto_d != "" and texto_u == "":
        return f"{texto_c} e {texto_d}."
        
    
    elif texto_c != "" and texto_d == "" and texto_u != "":
        return f"{texto_c} e {texto_u}."
        
    
    elif texto_c == "" and texto_d != "" and texto_u != "":
        return f"{texto_d} e {texto_u}."
        
    
    elif texto_c != "" and texto_d == "" and texto_u == "":
        return f"{texto_c}."
        
  
    elif texto_c == "" and texto_d != "" and texto_u == "":
        return f"{texto_d}."
        
    elif texto_c == "" and texto_d == "" and texto_u != "":
        return f"{texto_u}."

# Função principal
def main():

    #entrada de dados
    n = int(input("Digite um número: "))  
    #processamento
    
    numero = extenso(n)
    
    #saida de dados
    print(numero)

# Chama a função principal
if __name__ == '__main__':
    main()