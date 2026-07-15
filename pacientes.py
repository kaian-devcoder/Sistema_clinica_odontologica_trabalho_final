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


def alterar_paciente(dados):
    if not dados["pacientes"]:           #verificando se existe pacientes, se estiver vazia, a função vai ser encerrada lá no ( return - nesse contexto ele apenas impede que a função continue)
        print("\nNenhum paciente cadastrado. ")
        pausar()
        return
    listar_pacientes(dados, False)    #aqui é para listar os pacientes que estão em (dados -> .JSON), o false serve para não pausar no final, então não precisa clicar no ENTER  

    codigo = ler_inteiro("\nCódigo do paciente que será alterado: ")
    paciente = buscar_por_codigo(dados["pacientes"], codigo)
    if not paciente:   #Se nenhum paciente não for encontrado, o print do erro vai ser impresso!
        print("Paciente não encontrado. ")
        pausar()
        return
    
    print ("\n Deixe o campo vazio para manter o valor atual.")

    novo_nome = input(f'Nome [{paciente["nome"]}]: ').strip()
    novo_telefone = input(f'Telefone [{paciente["telefone"]}]: ').strip()

    if novo_nome:
        paciente["nome"] = novo_nome
    if novo_telefone:
        if novo_telefone.isdigit() and len(novo_telefone) >=8:
            paciente["telefone"] = novo_telefone
        else:
            print("Telefone inválido. O telefone anterior foi mantido.")


    print("\n1. Particular")
    print("2. Convênio")
    print("0. Manter o tipo atual")

    while True: 
        opcao = ler_inteiro("Tipo de atendimento: ")
        if opcao in (0, 1, 2):
            break
        print("Escolha 0, 1 ou 2.")
    if opcao == 1:
        paciente["tipo_atendimento"] =  "Particular"
    elif opcao ==2:
        paciente["tipo_atendimento"] = "Convênio"

    salvar_dados(dados)
    print("Paciente alterado com sucesso. ")
    pausar()
