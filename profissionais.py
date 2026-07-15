from persistencia import salvar_dados
from utilitarios import (
    buscar_por_codigo,
    ler_inteiro,
    ler_texto,
    pausar,
    proximo_codigo
)

from especialidades import listar_especialidades

def listar_profissionais(dados, pausar_no_final=True):
    print("\n========== PROFISSIONAIS CADASTRADOS ==========")

    if not dados["profissionais"]:
        print("Nenhum profissional cadastrado.")

    else:
        for profissional in dados["profissionais"]:
            especialidade = buscar_por_codigo(
                dados["especialidades"],
                profissional["especialidade_codigo"]
            )

            nome_especialidade = (
                especialidade["nome"]
                if especialidade
                else "Não encontrada"
            )

            print(
                f'Código: {profissional["codigo"]} | '
                f'Nome: {profissional["nome"]} | '
                f'Especialidade: {nome_especialidade} | '
                f'Situação: {profissional["situacao"]}'
            )

    if pausar_no_final:
        pausar()

def cadastrar_profissional(dados):
    if not dados["especialidades"]:
        print("\nCadastre uma especialidade primeiro.")
        pausar()
        return

    print("\n========== CADASTRO DE PROFISSIONAL ==========")

    nome = ler_texto("Nome do profissional: ")

    listar_especialidades(dados, False)

    codigo_especialidade = ler_inteiro(
        "\nCódigo da especialidade: "
    )

    especialidade = buscar_por_codigo(
        dados["especialidades"],
        codigo_especialidade
    )

    if not especialidade:
        print("Especialidade não encontrada.")
        pausar()
        return

    profissional = {
        "codigo": proximo_codigo(dados["profissionais"]),
        "nome": nome,
        "especialidade_codigo": codigo_especialidade,
        "situacao": "Ativo"
    }

    dados["profissionais"].append(profissional)
    salvar_dados(dados)

    print(
        f'Profissional cadastrado com o código '
        f'{profissional["codigo"]}.'
    )
    pausar()


def alterar_profissional(dados):
    if not dados["profissionais"]:
        print("\nNenhum profissional cadastrado.")
        pausar()
        return

    listar_profissionais(dados, False)

    codigo = ler_inteiro(
        "\nCódigo do profissional que será alterado: "
    )

    profissional = buscar_por_codigo(
        dados["profissionais"],
        codigo
    )

    if not profissional:
        print("Profissional não encontrado.")
        pausar()
        return

    novo_nome = input(
        f'Nome [{profissional["nome"]}]: '
    ).strip()

    if novo_nome:
        profissional["nome"] = novo_nome


    print("\n1. Ativo")
    print("2. Afastado")
    print("0. Manter situação atual")

    while True:
        opcao = ler_inteiro("Situação: ")

        if opcao in (0, 1, 2):
            break

        print("Escolha 0, 1 ou 2.")

    if opcao == 1:
        profissional["situacao"] = "Ativo"
    elif opcao == 2:
        profissional["situacao"] = "Afastado"

    resposta = input(
        "Alterar a especialidade? (s/n): "
    ).strip().lower()

    if resposta == "s":
        listar_especialidades(dados, False)

        codigo_especialidade = ler_inteiro(
            "Novo código da especialidade: "
        )

        especialidade = buscar_por_codigo(
            dados["especialidades"],
            codigo_especialidade
        )

        if especialidade:
            profissional["especialidade_codigo"] = codigo_especialidade
        else:
            print(
                "Especialidade não encontrada. "
                "A especialidade anterior foi mantida."
            )

    salvar_dados(dados)
    print("Profissional alterado com sucesso.")
    pausar()


def remover_profissional(dados):
    if not dados["profissionais"]:
        print("\nNenhum profissional cadastrado.")
        pausar()
        return

    listar_profissionais(dados, False)

    codigo = ler_inteiro(
        "\nCódigo do profissional que será removido: "
    )

    profissional = buscar_por_codigo(
        dados["profissionais"],
        codigo
    )

    if not profissional:
        print("Profissional não encontrado.")
        pausar()
        return

    # Impede a remoção caso o profissional possua consultas registradas.
    if any(
        consulta["profissional_codigo"] == codigo
        for consulta in dados["consultas"]
    ):
        print(
            "O profissional possui consultas registradas "
            "e não pode ser removido."
        )
        pausar()
        return

    confirmacao = input(
        f'Remover o profissional {profissional["nome"]}? (s/n): '
    ).strip().lower()

    if confirmacao == "s":
        dados["profissionais"].remove(profissional)
        salvar_dados(dados)
        print("Profissional removido com sucesso.")
    else:
        print("Remoção cancelada.")

    pausar()


def menu_profissionais(dados):
    while True:
        print("\n========== MENU DE PROFISSIONAIS ==========")
        print("1. Cadastrar profissional")
        print("2. Listar profissionais")
        print("3. Alterar profissional")
        print("4. Remover profissional")
        print("0. Voltar")

        opcao = ler_inteiro("Escolha uma opção: ")

        if opcao == 1:
            cadastrar_profissional(dados)

        elif opcao == 2:
            listar_profissionais(dados)

        elif opcao == 3:
            alterar_profissional(dados)

        elif opcao == 4:
            remover_profissional(dados)

        elif opcao == 0:
            break

        else:
            print("Opção inexistente.")