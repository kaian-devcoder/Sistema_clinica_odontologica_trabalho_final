from persistencia import carregar_dados, salvar_dados
from pacientes import menu_pacientes
from especialidades import menu_especialidades
from profissionais import menu_profissionais
from consultas import menu_consultas
from relatorios import menu_relatorios
from utilitarios import ler_inteiro


def main():
    dados = carregar_dados()

    while True:
        print("\n==============================================")
        print("   SISTEMA DE CLÍNICA MÉDICA/ODONTOLÓGICA")
        print("==============================================")
        print("1. Pacientes")
        print("2. Especialidades")
        print("3. Profissionais")
        print("4. Consultas")
        print("5. Relatórios")
        print("0. Sair")

        opcao = ler_inteiro("Escolha uma opção: ")

        if opcao == 1:
            menu_pacientes(dados)

        elif opcao == 2:
            menu_especialidades(dados)

        elif opcao == 3:
            menu_profissionais(dados)

        elif opcao == 4:
            menu_consultas(dados)

        elif opcao == 5:
            menu_relatorios(dados)

        elif opcao == 0:
            salvar_dados(dados)
            print("\nDados salvos. Programa encerrado.")
            break

        else:
            print("Opção inexistente.")


if __name__ == "__main__":
    main()