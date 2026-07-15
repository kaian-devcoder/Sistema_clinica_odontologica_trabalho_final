import json
import os

PASTA_PROJETO = os.path.dirname(os.path.abspath(__file__)) # Encontrar a pasta onde está o persitencia.py
ARQUIVO_DADOS = os.path.join(PASTA_PROJETO, "dados.json") # juntar a pasta com o nome dados.json

def criar_dados_vazios(): # criando estrutura inicial do sistema, função sem paremetro, mas com retorno
    return {
        "pacientes": [],
        "especialidades": [],
        "profissionais": [],
        "consultas": []
    }

def salvar_dados(dados): # essa função recebe o dicionário do sistema
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii= False, indent=4)

def carregar_dados():
    if not os.path.exists(ARQUIVO_DADOS): #Se o arquivo de dados não existir
        dados = criar_dados_vazios() #chamando a função que eu criei lá em cima, a primeira função
        salvar_dados(dados) #Aqui eu chamo a segunda função que eu criei
        return dados
    try: #tentar executar este bloco
        with open(ARQUIVO_DADOS, "r", encoding= "utf-8") as arquivo:
            dados = json.load(arquivo) #Isso aqui ler o arquivo e transforma o Json em dicionário no PYt
        return dados
    
    except (json.JSONDecodeError, OSError): #Se acontecer algum desses erros, execute o bloco abaixo 
        print("Não foi possível ler o arquivo dados.json")
        return criar_dados_vazios()
    
'''if __name__ == "__main__": #executar essa parte somente quando o arquivo persistencia for executado diretamente
    dados = carregar_dados()
    print(dados)'''

