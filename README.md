# 🚗 Trabalho Final — Sistemas de Gestão

**Instituto Federal de Educação, Ciência e Tecnologia do Piauí — IFPI / Campus Corrente**

**Disciplina:** Algoritmos e Lógica de Programação

**Curso:** Análise e Desenvolvimento de Sistemas (ADS)

---

## 🎯 Objetivo

Desenvolver um **sistema de gestão** completo, aplicando os conceitos estudados ao longo da disciplina: variáveis e tipos de dados, estruturas de decisão e repetição, listas e dicionários, funções, validação de dados e organização do código.

Cada equipe escolherá **um** dos temas disponíveis abaixo e deverá implementar o sistema atendendo aos requisitos descritos para aquele tema, além dos **requisitos mínimos comuns** a todos os projetos.

> 💡 Todos os temas têm o **mesmo grau de complexidade**. Não há tema "mais fácil" — a nota depende da qualidade da implementação, não do tema escolhido.

---

## 📋 Orientações Gerais

- **Equipes:** KAIAN e DEUS
- **Tema:** Clínica Médica Odontológica.
- **Linguagem:** Python 3.
- **Entrega:** repositório/pasta com o código-fonte + este README preenchido com os nomes da equipe.
- **Apresentação:** demonstração do sistema funcionando + explicação do código.
- **Prazo de entrega:** `15/07/2026`

---

## ✅ Requisitos Mínimos (comuns a todos os temas)

Independentemente do tema escolhido, o sistema **deve** conter:

1. **Menu principal** com navegação (laço de repetição até o usuário escolher sair).
2. **Cadastro completo (CRUD)** das principais entidades:
   - **C**riar (incluir novo registro)
   - **R**ecuperar (listar / consultar)
   - **U**pdate (alterar dados de um registro)
   - **D**elete (remover registro)
3. **Pelo menos 4 entidades** relacionadas entre si.
4. **Validação de dados de entrada** (não aceitar valores inválidos, campos vazios, opção inexistente no menu etc.).
5. **Regras de negócio** específicas do tema (cálculos, multas, descontos, verificação de disponibilidade etc.).
6. **Manipulação de datas/horas** quando o tema exigir (uso do módulo `datetime`).
7. **Pelo menos 2 relatórios/consultas** com filtro (ex.: listar todos os registros de um período, calcular um total etc.).
8. **Uso de funções** para organizar o código (evitar todo o programa em um único bloco).

### ⭐ Diferenciais (pontuação extra)
- Persistência de dados em arquivo (`.txt`).
- Tratamento de exceções (`try / except`).
- Interface organizada e amigável no terminal.
- Código comentado e bem identado.

---

## 🗂️ Tema

### 3. 🏥 Sistema de Clínica Médica/Odontológica

A clínica conta com diversos profissionais de saúde, de diferentes especialidades, que atuam em consultórios próprios. Eventualmente um profissional é afastado, desligado ou tem a agenda suspensa, e novos profissionais são contratados — sendo necessário manter o cadastro de profissionais, especialidades e horários sempre atualizado.

Os pacientes procuram a clínica para marcar consultas. Primeiro é necessário cadastrá-los, registrando se o atendimento será **particular** ou por **convênio**. Depois de identificado, o paciente escolhe a especialidade, o profissional e o horário disponível na agenda — **o valor da consulta varia conforme a especialidade, o tipo de atendimento e se é primeira consulta ou retorno**. O sistema deve **impedir conflito de horário** (dois pacientes no mesmo slot do mesmo profissional).

Realizada a consulta, define-se como concluída, registra-se data/hora e anotam-se no **prontuário** os procedimentos efetuados (cada procedimento extra tem valor próprio e soma ao total). **Retornos dentro do prazo** não são cobrados. Em caso de **falta sem aviso** ou remarcação fora do prazo, registra-se a ocorrência e aplicam-se as penalidades previstas.

---

## 📊 Critérios de Avaliação

| Critério | Descrição | Pontos |
|---|---|---|
| Funcionamento do menu e CRUD | Menu navegável e cadastro completo das entidades | 2,0 |
| Regras de negócio | Cálculos, multas, descontos e verificações corretas | 2,5 |
| Validação de dados | Tratamento de entradas inválidas | 1,5 |
| Relatórios/consultas | Consultas com filtro funcionando | 1,5 |
| Organização do código | Uso de funções, identação e clareza | 1,5 |
| Apresentação | Demonstração e domínio do código pela equipe | 1,0 |
| **Total** | | **10,0** |

> ⭐ Os diferenciais (persistência, tratamento de exceções, interface caprichada) podem render **pontuação extra** a critério do professor.

---

## 👥 Identificação da Equipe

| Nome | Sistema |
|---|---|
| Kaian Carvalho de Souza | 3 |

## 🚀 Como Executar

```bash
python main.py
```
---