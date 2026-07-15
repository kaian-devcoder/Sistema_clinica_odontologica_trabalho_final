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