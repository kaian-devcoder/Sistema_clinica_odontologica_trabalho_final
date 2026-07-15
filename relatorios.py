from datetime import datetime

from utilitarios import (
    FORMATO_DATA,
    buscar_por_codigo,
    ler_data,
    ler_inteiro,
    pausar
)

def relatorio_consultas_por_data(dados):
    data = ler_data("\nDigite a data (DD/MM/AAAA): ")
    encontrou = False

    print(f"\n========== CONSULTAS DO DIA {data} ==========")

    for consulta in dados["consultas"]:
        if consulta["data"] == data:
            encontrou = True

            paciente = buscar_por_codigo(
                dados["pacientes"],
                consulta["paciente_codigo"]
            )

            profissional = buscar_por_codigo(
                dados["profissionais"],
                consulta["profissional_codigo"]
            )

            print(
                f'{consulta["horario"]} | '
                f'Paciente: {paciente["nome"]} | '
                f'Profissional: {profissional["nome"]} | '
                f'Status: {consulta["status"]}'
            )

    if not encontrou:
        print("Nenhuma consulta encontrada.")

    pausar()

def relatorio_faturamento(dados):
    inicio_texto = ler_data("\nData inicial (DD/MM/AAAA): ")
    fim_texto = ler_data("Data final (DD/MM/AAAA): ")

    inicio = datetime.strptime(inicio_texto, FORMATO_DATA)
    fim = datetime.strptime(fim_texto, FORMATO_DATA)

    if fim < inicio:
        print("A data final não pode ser anterior à inicial.")
        pausar()
        return

    quantidade = 0
    total = 0

    for consulta in dados["consultas"]:
        data_consulta = datetime.strptime(
            consulta["data"],
            FORMATO_DATA
        )

        if (
            consulta["status"] == "Concluída"
            and inicio <= data_consulta <= fim
        ):
            quantidade += 1
            total += consulta["valor_total"]

    print("\n========== FATURAMENTO ==========")
    print(f"Período: {inicio_texto} até {fim_texto}")
    print(f"Consultas concluídas: {quantidade}")
    print(f"Total faturado: R$ {total:.2f}")

    pausar()

def menu_relatorios(dados):
    while True:
        print("\n========== MENU DE RELATÓRIOS ==========")
        print("1. Consultas por data")
        print("2. Faturamento por período")
        print("0. Voltar")

        opcao = ler_inteiro("Escolha uma opção: ")

        if opcao == 1:
            relatorio_consultas_por_data(dados)

        elif opcao == 2:
            relatorio_faturamento(dados)

        elif opcao == 0:
            break

        else:
            print("Opção inexistente.")

