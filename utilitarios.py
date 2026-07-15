from datetime import datetime
FORMATO_DATA = "%d/%m/%y"

def proximo_codigo(lista): #A lista é o parametro | obs, essa dunção poderá ser reaproveitada
    if not lista: #Verifica se a lista está vazia o primeiro código será 1
        return 1
    return max(item["codigo"] for item in lista) + 1 # Procura o maior código e soma + 1 a ele - evita repetir os códigos

def buscar_por_codigo(lista, codigo):
    for item in lista: # percorrendo cada item da lista
        if item["codigo"] == codigo: # compara o código do item com o código procurado
            return item # quando encontra, devolve o registro/item e termina a função
        return None #Só será executado depois que toda a lista for percorrida e sem encontrar o código, no caso até terminar o laço(for)
    
def ler_inteiro(mensagem): 
    while True: # Função repete até o usuário acertar
        try: #Não deixe com que algum valor digitado encerre o programa
            valor = int(input(mensagem))
            if valor >= 0: # condição para não ser negativo, pois tem que ser > ou = a 0
                return valor #Devolve o número válido e finaliza a função
            print("Digite um número igual ou maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def ler_valor(mensagem): 
    while True: 
        try:
            texto = input(mensagem).strip().replace(",", ".") #Essa função permite números decimais, com virgula ou ponto | strip remove espaços desnecessários no começo ou fim
            valor = float(texto)
            
            if valor >= 0:
                return valor
            print("O valor não pode ser negativo!")
        except ValueError:
            print("Entrada inválida, Digite um valor numérico.")


def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip() # Recebe o texto e remove os espaços no começo e fim
        if texto:                              # Se texto vazio, printa a mensagem
            return texto
        print("Esse campo não pode ficar vazio.")


def ler_data(mensagem, permitir_passado=True):
    while True: 
        texto = input(mensagem).strip()
        try: 
            data = datetime.strptime(texto, FORMATO_DATA) # Essa função interpreta o texto como uma data
            if not permitir_passado and data.date() < datetime.now().date():
                print("A data não pode estar no passado.")
                continue
            return texto
        except ValueError:
            print("Data inválida. Use DD/MM/AAAA")