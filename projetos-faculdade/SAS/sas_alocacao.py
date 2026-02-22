
# Disciplina: Lógica de Programação e Algoritmo I.
# Projeto: Sistema de Alocação de Salas (SAS).
# Desenvolvido por: Éveny Oliveira.

salas = []  # listas para armazenar as salas e as turmas.
turmas = []

qtd_salas = int(input("Digite a quantidade de salas a serem cadastradas: "))  # Aqui são solicitadas a quantidade de turmas e salas que serão cadastradas.
qtd_turmas = int(input("Digite a quantidade de turmas a serem cadastradas: "))

print("\n----------------------- CADASTRO DE SALAS ----------------------\n")

for i in range (qtd_salas): # laço de repetição p/ cadastrar cada sala.
    numero = int(input("Digite o número da sala: "))
    andar = int(input("Digite o andar onde fica a sala: "))
    capacidade = int(input("Digite a capacidade máxima da sala: "))
    print()

    if capacidade <= 0:  # a capacidade deve ser maior e diferente de 0.
        print("Erro: valores inválidos. Tente novamente.\n")
        continue

    # aqui um dicionário é criado para armazenas os atributos da sala
    sala = {"numero": numero, "andar": andar, "capacidade": capacidade, "ocupada": False} # ocupada: true é indisponivel e ocupada: false é disponivel.
    salas.append(sala) # essa linha adiciona o dicionário "sala" a lista de salas.

print("\n----------------------- CADASTRO DE TURMAS ----------------------\n")

for i in range(qtd_turmas): # aqui é o cadastro de turmas.
    curso = str(input("Digite o nome do curso: "))
    periodo = int(input("Digite o período (1 à 10): "))
    disciplina = str(input("Digite o nome da disciplina: "))
    qtd_alunos = int(input("Digite a quantidade de alunos da turma: "))
    print()

    if qtd_alunos <= 0 or periodo <= 0:  # a quantidade de alunos e período também devem ser maior que 0.
        print("Erro: valores inválidos. Tente novamente.\n")
        continue # pula pra próxima iteração

    turma = {"curso": curso, "periodo": periodo, "disciplina": disciplina, "qtd_alunos": qtd_alunos, "alocada": False, "sala_alocada": None}
    turmas.append(turma) # essa linha adiciona a turma a lista de turmas
    # sala_alocada: none significa que a turma ainda não tem uma sala.
    # e alocada: false, que ainda não foi alocada.

print("\n---------------------------- ALOCAÇÃO ---------------------------\n")

for turma in turmas: # isso aqui faz com que percorra cada turma; laço externo.
    turma_alocada = False
    sala_compativel = False # e essa se existe sala compatível e desocupada.

    for sala in salas: # esse percorre cada sala para uma compatível.
        if turma['qtd_alunos'] <= sala["capacidade"]: # se a quantidade de alunos for menor ou igual a capacidade da sala ela é compatível.
           sala_compativel = True

           if not sala["ocupada"]: # a sala: não pode estar ocupada e sua capacidade deve ser o suficiente para acomodar a turma.
               sala["ocupada"] = True # se a alocação for bem sucessida, os dados são atualizados.
               turma["alocada"] = True
               turma["sala_alocada"] = sala["numero"]
               diferenca = sala["capacidade"] - turma["qtd_alunos"] # diferença de lugares livres.
               print("\n-----------------------------------------------------------------\n")
               print("Turma alocada com sucesso!")
               print(f"Curso: {turma['curso']}.")
               print(f"Período: {turma['periodo']}.")
               print(f"Disciplina: {turma['disciplina']}.")
               print(f"Sala: {sala['numero']} ({sala['andar']}º andar).")
               print(f"Restam {diferenca} lugares livres.")
               print("\n-----------------------------------------------------------------\n")
               turma_alocada = True
               break

    if not turma_alocada:  # caso a turma não tenha sido alocada.
        print("\n-----------------------------------------------------------------\n")
        print("Não foi possível alocar a turma.")
        print(f"Curso: {turma['curso']}.")
        print(f"Período: {turma['periodo']}.")
        print(f"Disciplina: {turma['disciplina']}.")

        if sala_compativel: # se sala_comaptivel é True, então significa que a turma cabe em alguma sala, mas ela está ocupada.
            print("Salas compatíveis já ocupadas.")
            print("\n-----------------------------------------------------------------\n")
        else: # se não tiver uma compativel, é porque faltam lugares.
            print("Faltam alguns lugares para acomodar todos os alunos.")
            print("\n-----------------------------------------------------------------\n")

print("Alocação finalizada.")

# aqui sairia o relatório final

print("\n------------------ Relatório final de Alocação ------------------\n")

# essa linha abaixo faz com que o sistema percorra todas as turmas e mostre a situação final de cada uma delas.
for t in turmas:
    if t["alocada"]:
        print(f"Turma '{t['disciplina']}' - Curso: {t['curso']} -> Sala {t['sala_alocada']}.")
    else:
        print(f"Turma '{t['disciplina']}' - Curso: {t['curso']} -> Não alocada.")
print("\n-----------------------------------------------------------------\n")