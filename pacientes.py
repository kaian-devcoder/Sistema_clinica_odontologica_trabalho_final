from persistencia import salvar_dados       #importando do arquivo persistencia a função -> salvar_dados
from utilitarios import (                   #importando do arquivo utilitarios a função -> buscar_por_codigo
        buscar_por_codigo,
        ler_inteiro,
        ler_texto,
        pausar,
        proximo_codigo
        #Aqui eu faço as importações de todas essas funções que estão lá no arquivo utilitários.
)
# Iniciando o CRUD

def listar_pacientes(dados, pausar_no_final=True): #Essa função tá recebendo dois parametros = (dados) Que é o dicionário completo carregado do JSON
    print("\n ============== PACIENTES CADASTRADOS ==============")

    if not dados["pacientes"]:  #Se a lista de pacientes estiver vazia, caso contrario o else percorre os pacientes.
        print("|  Nenhum paciente cadastrado.  |")
    else:
        for paciente in dados["pacientes"]:  #Estamos acessando somente pacientes
            print(
                f'Código: {paciente["codigo"]} | ' 
                f'Nome: {paciente["nome"]} | '
                f'Telefone: {paciente["telefone"]} | '
                f'Atendimento: {paciente["tipo_atendimento"]}'
            )
    if pausar_no_final: #Essa função lista os pacientes e espera o usuário apertar o Enter
        pausar()