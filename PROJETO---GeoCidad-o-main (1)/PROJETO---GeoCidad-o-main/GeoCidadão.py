# Sistema de Coleta Seletiva - GeoCidadão + GeoData

# Dados de pontos de coleta por região (GeoData)
pontos_coleta = {
    "Centro": ["Praça Central", "Rua Verde", "Mercado Municipal"],
    "Zona Norte": ["Escola Municipal", "Parque Norte"],
    "Zona Sul": ["Shopping Sul", "Avenida Principal"],
    "Zona Leste": ["Terminal Leste", "Praça das Flores"]
}

# Lista de registros
registros = []


# VALIDAÇÃO DE IDADE

def validar_idade(idade):
    return idade >= 18


# CADASTRO

def cadastro():
    print("\n--- Cadastro ---")

    nome = input("Nome: ")
    email = input("E-mail: ")
    cpf = input("CPF: ")

    while True:
        try:
            idade = int(input("Idade: "))
            if idade <= 0:
                print("Idade inválida!")
            else:
                break
        except:
            print("Digite um número válido!")

    if not validar_idade(idade):
        print("\n Apenas maiores de idade podem acessar.")
        return None

    print("\n Cadastro realizado!")

    return {
        "nome": nome,
        "email": email,
        "cpf": cpf
    }


# ESCOLHER REGIÃO

def escolher_regiao():
    print("\n--- Escolha sua região ---")

    regioes = list(pontos_coleta.keys())

    for i, r in enumerate(regioes, start=1):
        print(f"{i} - {r}")

    while True:
        try:
            escolha = int(input("Digite o número da região: "))
            if 1 <= escolha <= len(regioes):
                return regioes[escolha - 1]
            else:
                print("Opção inválida!")
        except:
            print("Digite um número válido!")


# MOSTRAR PONTOS DE COLETA

def mostrar_pontos(regiao):
    print(f"\n Pontos de coleta na região {regiao}:")

    for ponto in pontos_coleta[regiao]:
        print(f"- {ponto}")


# REGISTRAR DESCARTE

def registrar_descarte(usuario, regiao):
    print("\n--- Registrar Descarte ---")

    tipo = input("Tipo de material (plástico/papel/vidro/metal): ")
    ponto = input("Escolha um ponto de coleta: ")

    registro = {
        "usuario": usuario["nome"],
        "regiao": regiao,
        "tipo": tipo,
        "ponto": ponto
    }

    registros.append(registro)

    print("\n Descarte registrado com sucesso!")


# LISTAR REGISTROS

def listar_registros():
    print("\n--- Registros ---")

    if not registros:
        print("Nenhum registro encontrado.")
        return

    for r in registros:
        print(f"\nUsuário: {r['usuario']}")
        print(f"Região: {r['regiao']}")
        print(f"Material: {r['tipo']}")
        print(f"Ponto: {r['ponto']}")


# MENU

def menu():
    usuario = cadastro()

    if usuario is None:
        return

    regiao = escolher_regiao()
    mostrar_pontos(regiao)

    while True:
        print("\n--- Menu ---")
        print("1 - Registrar descarte")
        print("2 - Ver registros")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            registrar_descarte(usuario, regiao)

        elif opcao == "2":
            listar_registros()

        elif opcao == "3":
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")

# EXECUÇÃO
menu()