from persistencia import salvar_dados
from utilitarios import (
    buscar_por_codigo,
    ler_inteiro,
    ler_texto,
    ler_valor, #Essa função recebe o valor da consulta
    pausar,
    proximo_codigo
)

def listar_especialidades(dados, pausar_no_final=True):
    print("\n========== ESPECIALIDADES CADASTRADAS ==========")

    if not dados["especialidades"]:
        print("Nenhuma especialidade cadastrada.")
    else:
        for especialidade in dados["especialidades"]:
            print(
                f'Código: {especialidade["codigo"]} | '
                f'Nome: {especialidade["nome"]} | '
                f'Valor: R$ {especialidade["valor"]:.2f}'
            )

    if pausar_no_final:
        pausar()

def cadastrar_especialidade(dados):
    print("\n========== CADASTRO DE ESPECIALIDADE ==========")

    nome = ler_texto("Nome da especialidade: ")

    if any(
        especialidade["nome"].lower() == nome.lower()
        for especialidade in dados["especialidades"]
    ):
        print("Essa especialidade já está cadastrada.")
        pausar()
        return

    valor = ler_valor("Valor da consulta: R$ ")

    especialidade = {
        "codigo": proximo_codigo(dados["especialidades"]),
        "nome": nome,
        "valor": valor
    }

    dados["especialidades"].append(especialidade)
    salvar_dados(dados)

    print(
        f'Especialidade cadastrada com o código '
        f'{especialidade["codigo"]}.'
    )
    pausar()

def alterar_especialidade(dados):
    if not dados["especialidades"]:
        print("\nNenhuma especialidade cadastrada.")
        pausar()
        return

    listar_especialidades(dados, False)

    codigo = ler_inteiro(
        "\nCódigo da especialidade que será alterada: "
    )
    especialidade = buscar_por_codigo(
        dados["especialidades"], codigo
    )

    if not especialidade:
        print("Especialidade não encontrada.")
        pausar()
        return

    novo_nome = input(
        f'Nome [{especialidade["nome"]}]: '
    ).strip()

    if novo_nome:
        nome_repetido = any(
            item["nome"].lower() == novo_nome.lower()
            and item["codigo"] != codigo
            for item in dados["especialidades"]
        )

        if nome_repetido:
            print("Esse nome já está cadastrado. O anterior foi mantido.")
        else:
            especialidade["nome"] = novo_nome

    resposta = input(
        f'Alterar o valor atual de R$ '
        f'{especialidade["valor"]:.2f}? (s/n): '
    ).strip().lower()

    if resposta == "s":
        especialidade["valor"] = ler_valor("Novo valor: R$ ")

    salvar_dados(dados)
    print("Especialidade alterada com sucesso.")
    pausar()

def remover_especialidade(dados):
    if not dados["especialidades"]:
        print("\nNenhuma especialidade cadastrada.")
        pausar()
        return

    listar_especialidades(dados, False)

    codigo = ler_inteiro(
        "\nCódigo da especialidade que será removida: "
    )

    especialidade = buscar_por_codigo(
        dados["especialidades"], codigo
    )

    if not especialidade:
        print("Especialidade não encontrada.")
        pausar()
        return

    if any(
        profissional["especialidade_codigo"] == codigo
        for profissional in dados["profissionais"]
    ):
        print(
            "Essa especialidade está vinculada a um profissional "
            "e não pode ser removida."
        )
        pausar()
        return

    confirmacao = input(
        f'Remover a especialidade {especialidade["nome"]}? (s/n): '
    ).strip().lower()

    if confirmacao == "s":
        dados["especialidades"].remove(especialidade)
        salvar_dados(dados)
        print("Especialidade removida com sucesso.")
    else:
        print("Remoção cancelada.")

    pausar()

def menu_especialidades(dados):
    while True:
        print("\n========== MENU DE ESPECIALIDADES ==========")
        print("1. Cadastrar especialidade")
        print("2. Listar especialidades")
        print("3. Alterar especialidade")
        print("4. Remover especialidade")
        print("0. Voltar")

        opcao = ler_inteiro("Escolha uma opção: ")

        if opcao == 1:
            cadastrar_especialidade(dados)

        elif opcao == 2:
            listar_especialidades(dados)

        elif opcao == 3:
            alterar_especialidade(dados)

        elif opcao == 4:
            remover_especialidade(dados)

        elif opcao == 0:
            break

        else:
            print("Opção inexistente.")