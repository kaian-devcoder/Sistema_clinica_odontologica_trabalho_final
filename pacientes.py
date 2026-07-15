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

        def cadastrar_paciente(dados):
            print("\n ============== CADASTRO DE PACIENTE ==============")

            nome = ler_texto("Nome: ")                           # Essa função impede o usuário de deixar o campo vazio

            while True:                                         #Repete até o telefone estar correto.
                telefone = ler_texto("Telefone, somente em números: ")

                if telefone.isdigit()  and len(telefone) >= 8:   # (isdigit) verifica se todos os caracteres são números e o (len) é para conferir se tem pelo menos 8 caracteres o telefone
                    break                                         # Atenção, o (and) não é (or), então as duas condições precisam ser verdadeiras
                print("Digite um número de telefone válido.")

            print("\n1. Particular") 
            print("2. Convênio")

            while True: 
                opcao = ler_inteiro("Tipo de atendimento: ")
                if opcao in (1, 2):                                #Se opção estiver entre 1 ou 2 - se opção for 1 ou 2
                    break

                print("Escolha 1 ou 2.")

            paciente = {   
                "codigo": proximo_codigo(dados["pacientes"]),
                "nome": nome,
                "telefone": telefone,
                "tipo_atendimento": "Particular" if opcao == 1 else "Convênio"          # Se a opção for 1 é particular, caso contrário é convenio
            
            }
            dados["pacientes"].append(paciente)                                          # Lembre-se das aulas, (.append) coloca um novo dicionário ao final da lista de pacientes
            salvar_dados(dados)                                #Aqui o dicionário é gravado em dados.json

            print(f'\nPaciente cadastrado com o código {paciente["codigo"]}')
            pausar()
