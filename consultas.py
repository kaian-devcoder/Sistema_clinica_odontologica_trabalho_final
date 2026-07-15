from datetime import datetime

from persistencia import salvar_dados
from pacientes import listar_pacientes
from profissionais import listar_profissionais
from utilitarios import (
    FORMATO_DATA,
    buscar_por_codigo,
    ler_data,
    ler_horario,
    ler_inteiro,
    pausar,
    proximo_codigo
)


def listar_consultas(dados, pausar_no_final=True):
    print("\n========== CONSULTAS REGISTRADAS ==========")

    if not dados["consultas"]:
        print("Nenhuma consulta registrada.")

    else:
        for consulta in dados["consultas"]:
            paciente = buscar_por_codigo(
                dados["pacientes"],
                consulta["paciente_codigo"]
            )

            profissional = buscar_por_codigo(
                dados["profissionais"],
                consulta["profissional_codigo"]
            )

            especialidade = buscar_por_codigo(
                dados["especialidades"],
                consulta["especialidade_codigo"]
            )

            print("-" * 60)
            print(
                f'Código: {consulta["codigo"]} | '
                f'Data: {consulta["data"]} às {consulta["horario"]}'
            )
            print(
                f'Paciente: '
                f'{paciente["nome"] if paciente else "Não encontrado"}'
            )
            print(
                f'Profissional: '
                f'{profissional["nome"] if profissional else "Não encontrado"}'
            )
            print(
                f'Especialidade: '
                f'{especialidade["nome"] if especialidade else "Não encontrada"}'
            )
            print(
                f'Tipo: {consulta["tipo"]} | '
                f'Status: {consulta["status"]}'
            )
            print(f'Valor total: R$ {consulta["valor_total"]:.2f}')

    if pausar_no_final:
        pausar()

def horario_ocupado(
    dados,
    profissional_codigo,
    data,
    horario,
    ignorar_codigo=None
):
    for consulta in dados["consultas"]:
        if consulta["codigo"] == ignorar_codigo:
            continue

        if (
            consulta["profissional_codigo"] == profissional_codigo
            and consulta["data"] == data
            and consulta["horario"] == horario
            and consulta["status"] == "Agendada"
        ):
            return True

    return False


def calcular_valor_consulta(dados, paciente, profissional, data, tipo):
    especialidade = buscar_por_codigo(
        dados["especialidades"],
        profissional["especialidade_codigo"]
    )

    valor = especialidade["valor"]

    # Paciente de convênio recebe 20% de desconto.
    if paciente["tipo_atendimento"] == "Convênio":
        valor *= 0.80

    if tipo == "Retorno":
        data_nova = datetime.strptime(data, FORMATO_DATA)

        retorno_gratuito = any(
            consulta["paciente_codigo"] == paciente["codigo"]
            and consulta["profissional_codigo"] == profissional["codigo"]
            and consulta["status"] == "Concluída"
            and 0 <= (
                data_nova
                - datetime.strptime(consulta["data"], FORMATO_DATA)
            ).days <= 30
            for consulta in dados["consultas"]
        )

        if retorno_gratuito:
            return 0.0, True

    return valor, False

def agendar_consulta(dados):
    if not dados["pacientes"]:
        print("\nCadastre pelo menos um paciente primeiro.")
        pausar()
        return

    if not dados["profissionais"]:
        print("\nCadastre pelo menos um profissional primeiro.")
        pausar()
        return

    print("\n========== AGENDAMENTO DE CONSULTA ==========")

    listar_pacientes(dados, False)
    paciente_codigo = ler_inteiro("\nCódigo do paciente: ")

    paciente = buscar_por_codigo(
        dados["pacientes"],
        paciente_codigo
    )

    if not paciente:
        print("Paciente não encontrado.")
        pausar()
        return

    listar_profissionais(dados, False)
    profissional_codigo = ler_inteiro("\nCódigo do profissional: ")

    profissional = buscar_por_codigo(
        dados["profissionais"],
        profissional_codigo
    )

    if not profissional:
        print("Profissional não encontrado.")
        pausar()
        return

    if profissional["situacao"] != "Ativo":
        print("Esse profissional está afastado.")
        pausar()
        return

    data = ler_data(
        "Data da consulta (DD/MM/AAAA): ",
        permitir_passado=False
    )

    horario = ler_horario(
        "Horário da consulta (HH:MM): "
    )

    if horario_ocupado(
        dados,
        profissional_codigo,
        data,
        horario
    ):
        print("Esse horário já está ocupado.")
        pausar()
        return

    print("\n1. Primeira consulta")
    print("2. Retorno")

    while True:
        opcao = ler_inteiro("Tipo da consulta: ")

        if opcao in (1, 2):
            break

        print("Escolha 1 ou 2.")

    tipo = "Primeira consulta" if opcao == 1 else "Retorno"

    valor, retorno_gratuito = calcular_valor_consulta(
        dados,
        paciente,
        profissional,
        data,
        tipo
    )

    consulta = {
        "codigo": proximo_codigo(dados["consultas"]),
        "paciente_codigo": paciente_codigo,
        "profissional_codigo": profissional_codigo,
        "especialidade_codigo": profissional["especialidade_codigo"],
        "data": data,
        "horario": horario,
        "tipo": tipo,
        "status": "Agendada",
        "valor_consulta": valor,
        "procedimento": "Nenhum",
        "valor_procedimento": 0.0,
        "valor_total": valor
    }

    dados["consultas"].append(consulta)
    salvar_dados(dados)

    print(
        f'\nConsulta agendada com o código '
        f'{consulta["codigo"]}.'
    )

    if retorno_gratuito:
        print("Retorno dentro de 30 dias: consulta gratuita.")

    print(f'Valor previsto: R$ {valor:.2f}')
    pausar()


def remarcar_consulta(dados):
    if not dados["consultas"]:
        print("\nNenhuma consulta registrada.")
        pausar()
        return

    listar_consultas(dados, False)

    codigo = ler_inteiro(
        "\nCódigo da consulta que será remarcada: "
    )

    consulta = buscar_por_codigo(
        dados["consultas"],
        codigo
    )

    if not consulta:
        print("Consulta não encontrada.")
        pausar()
        return

    if consulta["status"] != "Agendada":
        print("Somente consultas agendadas podem ser remarcadas.")
        pausar()
        return

    nova_data = ler_data(
        "Nova data (DD/MM/AAAA): ",
        permitir_passado=False
    )

    novo_horario = ler_horario(
        "Novo horário (HH:MM): "
    )

    if horario_ocupado(
        dados,
        consulta["profissional_codigo"],
        nova_data,
        novo_horario,
        ignorar_codigo=consulta["codigo"]
    ):
        print("O novo horário já está ocupado.")
        pausar()
        return

    consulta["data"] = nova_data
    consulta["horario"] = novo_horario

    salvar_dados(dados)

    print("Consulta remarcada com sucesso.")
    pausar()

def atualizar_status_consulta(dados):
    if not dados["consultas"]:
        print("\nNenhuma consulta registrada.")
        pausar()
        return

    listar_consultas(dados, False)

    codigo = ler_inteiro("\nCódigo da consulta: ")
    consulta = buscar_por_codigo(dados["consultas"], codigo)

    if not consulta:
        print("Consulta não encontrada.")
        pausar()
        return

    if consulta["status"] != "Agendada":
        print("Essa consulta não está mais agendada.")
        pausar()
        return

    print("\n1. Concluir consulta")
    print("2. Cancelar consulta")
    print("3. Registrar falta sem aviso")

    opcao = ler_inteiro("Escolha uma opção: ")

    if opcao == 1:
        procedimentos = {
            1: ("Nenhum", 0.0),
            2: ("Procedimento simples", 50.0),
            3: ("Procedimento complexo", 100.0)
        }

        print("\n1. Nenhum - R$ 0,00")
        print("2. Procedimento simples - R$ 50,00")
        print("3. Procedimento complexo - R$ 100,00")

        while True:
            escolha = ler_inteiro("Procedimento realizado: ")

            if escolha in procedimentos:
                break

            print("Escolha 1, 2 ou 3.")

        nome, valor = procedimentos[escolha]

        consulta["status"] = "Concluída"
        consulta["procedimento"] = nome
        consulta["valor_procedimento"] = valor
        consulta["valor_total"] = consulta["valor_consulta"] + valor

        print(
            f'Consulta concluída. '
            f'Total: R$ {consulta["valor_total"]:.2f}'
        )

    elif opcao == 2:
        consulta["status"] = "Cancelada"
        consulta["valor_total"] = 0.0

        print("Consulta cancelada sem cobrança.")

    elif opcao == 3:
        consulta["status"] = "Falta"
        consulta["procedimento"] = "Multa por falta"
        consulta["valor_procedimento"] = 0.0
        consulta["valor_total"] = 30.0

        print("Falta registrada. Penalidade: R$ 30,00.")

    else:
        print("Opção inexistente.")
        pausar()
        return

    salvar_dados(dados)
    pausar()

def excluir_consulta(dados):
    if not dados["consultas"]:
        print("\nNenhuma consulta registrada.")
        pausar()
        return

    listar_consultas(dados, False)

    codigo = ler_inteiro(
        "\nCódigo da consulta que será excluída: "
    )

    consulta = buscar_por_codigo(
        dados["consultas"],
        codigo
    )

    if not consulta:
        print("Consulta não encontrada.")
        pausar()
        return

    confirmacao = input(
        f'Confirma a exclusão da consulta {codigo}? (s/n): '
    ).strip().lower()

    if confirmacao == "s":
        dados["consultas"].remove(consulta)
        salvar_dados(dados)
        print("Consulta excluída com sucesso.")
    else:
        print("Exclusão cancelada.")

    pausar()

def menu_consultas(dados):
    while True:
        print("\n========== MENU DE CONSULTAS ==========")
        print("1. Agendar consulta")
        print("2. Listar consultas")
        print("3. Remarcar consulta")
        print("4. Concluir, cancelar ou registrar falta")
        print("5. Excluir consulta")
        print("0. Voltar")

        opcao = ler_inteiro("Escolha uma opção: ")

        if opcao == 1:
            agendar_consulta(dados)

        elif opcao == 2:
            listar_consultas(dados)

        elif opcao == 3:
            remarcar_consulta(dados)

        elif opcao == 4:
            atualizar_status_consulta(dados)

        elif opcao == 5:
            excluir_consulta(dados)

        elif opcao == 0:
            break

        else:
            print("Opção inexistente.")

