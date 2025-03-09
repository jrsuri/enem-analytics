import msvcrt

try:
    import pickle
    import os
    import pandas as pd

    # Configurações dos diretórios
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)
    models_dir = os.path.join(base_dir, 'models')
    input_path = os.path.join(models_dir, 'model.pkl')

    # Carrega o modelo salvo
    with open(input_path, 'rb') as f:
        modelo = pickle.load(f)

    # Mapeamentos das opções para os valores usados no modelo
    faixa_etaria_opcoes = [
        'Menor de 17 anos', '17 anos', '18 anos', '19 anos', '20 anos',
        '21 anos', '22 anos', '23 anos', '24 anos', '25 anos',
        'Entre 26 e 30 anos', 'Entre 31 e 35 anos', 'Entre 36 e 40 anos',
        'Entre 41 e 45 anos', 'Entre 46 e 50 anos', 'Entre 51 e 55 anos',
        'Entre 56 e 60 anos', 'Entre 61 e 65 anos', 'Entre 66 e 70 anos', 'Maior de 70 anos'
    ]

    escolaridade_mae_opcoes = [
        'Nunca estudou.', 'Não completou a 4ª série/5º ano do Ensino Fundamental.',
        'Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental.',
        'Completou a 8ª série/9º ano do Ensino Fundamental, mas não completou o Ensino Médio.',
        'Completou o Ensino Médio, mas não completou a Faculdade.',
        'Completou a Faculdade, mas não completou a Pós-graduação.',
        'Completou a Pós-graduação.'
    ]

    renda_familiar_opcoes = [
        'Nenhuma Renda', 'Até R$ 1.212,00', 'De R$ 1.212,01 até R$ 1.818,00.',
        'De R$ 1.818,01 até R$ 2.424,00.', 'De R$ 2.424,01 até R$ 3.030,00.',
        'De R$ 3.030,01 até R$ 3.636,00.', 'De R$ 3.636,01 até R$ 4.848,00.',
        'De R$ 4.848,01 até R$ 6.060,00.', 'De R$ 6.060,01 até R$ 7.272,00.',
        'De R$ 7.272,01 até R$ 8.484,00.', 'De R$ 8.484,01 até R$ 9.696,00.',
        'De R$ 9.696,01 até R$ 10.908,00.', 'De R$ 10.908,01 até R$ 12.120,00.',
        'De R$ 12.120,01 até R$ 14.544,00.', 'De R$ 14.544,01 até R$ 18.180,00.',
        'De R$ 18.180,01 até R$ 24.240,00.', 'Acima de R$ 24.240,00.'
    ]

    # Função para exibir opções e capturar a escolha do usuário
    def selecionar_opcao(lista_opcoes, mensagem):
        print(mensagem)
        for i, opcao in enumerate(lista_opcoes):
            print(f'[{i}] {opcao}')
        escolha = int(input('Escolha um número: '))
        return escolha

    # Coleta os inputs do usuário
    faixa_etaria = selecionar_opcao(faixa_etaria_opcoes, '\nSelecione a faixa etária:')
    escolaridade_mae = selecionar_opcao(escolaridade_mae_opcoes, '\nSelecione a escolaridade da mãe:')
    tamanho_familia = int(input('\nDigite o tamanho da família (número de pessoas): '))
    renda_familiar = selecionar_opcao(renda_familiar_opcoes, '\nSelecione a renda familiar:')
    sexo_feminino = int(input('\nSexo (0 - Masculino, 1 - Feminino): '))
    escola_privada = int(input('\nEstudou em escola privada? (0 - Não, 1 - Sim): '))
    treineiro = int(input('\nÉ treineiro? (0 - Não, 1 - Sim): '))

    # Seleção de raça
    print('\nSelecione a raça/cor:')
    print('[0] Branco')
    print('[1] Amarelo')
    print('[2] Preto')
    print('[3] Pardo')
    print('[4] Indígena')
    raca = int(input('Escolha um número: '))

    # Define as variáveis binárias de raça
    branco_amarelo = 1 if raca in [0, 1] else 0
    preto_pardo_indigena = 1 if raca in [2, 3, 4] else 0

    # Computador em casa
    possui_computador = int(input('\nPossui computador em casa? (0 - Não, 1 - Sim): '))

    # Cria um DataFrame com os valores inseridos
    colunas = [
        'faixa_etaria', 'escolaridade_mae', 'tamanho_familia', 'renda_familiar',
        'sexo_feminino', 'escola_privada', 'treineiro', 'branco_amarelo',
        'preto_pardo_indigena', 'possui_computador'
    ]

    dados_entrada = pd.DataFrame([[faixa_etaria, escolaridade_mae, tamanho_familia, renda_familiar,
                                   sexo_feminino, escola_privada, treineiro, branco_amarelo,
                                   preto_pardo_indigena, possui_computador]], columns=colunas)

    # Exibe os dados coletados
    # print('\nDados inseridos:')
    # print(dados_entrada.to_string(index=False))

    # Faz a previsão
    previsao = modelo.predict(dados_entrada)[0]
    probabilidade = modelo.predict_proba(dados_entrada)[0][1]

    # Exibe o resultado
    print('\n*** RESULTADO ***')
    if previsao == 1:
        print(f'O modelo prevê que o candidato terá uma nota ALTA, com probabilidade de {round(probabilidade * 100, 2)}%')
    else:
        print(f'O modelo prevê que o candidato NÃO terá uma nota alta, com probabilidade de {round((1 - probabilidade) * 100, 2)}%')

    print('\nPressione qualquer tecla para fechar.')
    msvcrt.getch()

except Exception as e:
    print(e)
    print('\nPressione qualquer tecla para fechar.')
    msvcrt.getch()