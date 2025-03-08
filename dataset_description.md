# Descrição do Dataset - Microdados do ENEM 2022

## Origem do dataset
Os microdados do ENEM 2022 são disponibilizados pelo Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP) e contêm informações detalhadas sobre os candidatos, suas escolas, desempenho nas provas e dados socioeconômicos coletados por meio de um questionário.

O dataset pode ser acessado diretamente no site oficial do INEP:  
[https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem)

## Estrutura do dataset
A seguir são apresentadas as principais variáveis disponíveis. O dataset está dividido em quatro partes principais:

### 1. Dados do aluno, escola e prova

| Nome da Variável     | Descrição                                           |
|----------------------|-----------------------------------------------------|
| NU_ANO              | Ano de realização do ENEM                           |
| TP_FAIXA_ETARIA     | Faixa etária do candidato                           |
| TP_SEXO             | Sexo do candidato (M ou F)                          |
| TP_COR_RACA         | Cor ou raça autodeclarada                           |
| TP_ESCOLA           | Tipo de escola frequentada                          |
| TP_ENSINO           | Tipo de escola do ensino médio                      |
| CO_MUNICIPIO_PROVA  | Código do município onde o participante fez a prova |
| SG_UF_PROVA         | Sigla da UF onde o participante fez a prova         |
| TP_PRESENCA_CN      | Presença na prova de Ciências da Natureza           |
| TP_PRESENCA_CH      | Presença na prova de Ciências Humanas               |
| TP_PRESENCA_LC      | Presença na prova de Linguagens e Códigos           |
| TP_PRESENCA_MT      | Presença na prova de Matemática                     |
| NU_NOTA_CN          | Nota em Ciências da Natureza                        |
| NU_NOTA_CH          | Nota em Ciências Humanas                            |
| NU_NOTA_LC          | Nota em Linguagens e Códigos                        |
| NU_NOTA_MT          | Nota em Matemática                                  |
| TP_LINGUA           | Língua estrangeira escolhida                        |
| TP_STATUS_REDACAO   | Status da redação                                   |
| NU_NOTA_COMP1       | Nota da competência 1 na redação                    |
| NU_NOTA_COMP2       | Nota da competência 2 na redação                    |
| NU_NOTA_COMP3       | Nota da competência 3 na redação                    |
| NU_NOTA_COMP4       | Nota da competência 4 na redação                    |
| NU_NOTA_COMP5       | Nota da competência 5 na redação                    |
| NU_NOTA_REDACAO     | Nota final da redação                               |

### 2. Itens da prova

| Nome da Variável  | Descrição |
|------------------|-----------|
| CO_POSICAO      | Posição do item na prova |
| SG_AREA         | Área de conhecimento do item |
| CO_ITEM        | Código do item |
| TX_GABARITO    | Gabarito do item |
| CO_HABILIDADE  | Habilidade avaliada pelo item |
| IN_ITEM_ABAN   | Indicador de item abandonado |
| TX_MOTIVO_ABAN | Motivo para o abandono do item |
| NU_PARAM_A     | Parâmetro de discriminação do item |
| NU_PARAM_B     | Parâmetro de dificuldade do item |
| NU_PARAM_C     | Parâmetro de acerto ao acaso |
| TX_COR         | Cor da prova |
| CO_PROVA       | Identificador da prova |
| TP_LINGUA      | Língua estrangeira |
| IN_ITEM_ADAPTADO | Item pertencente à prova adaptada |

### 3. Dados do questionário socioeconômico

| Código da pergunta | Descrição |
|------------------|-----------|
| Q001 | Escolaridade do pai/homem responsável |
| Q002 | Escolaridade da mãe/mulher responsável |
| Q003 | Ocupação do pai/homem responsável |
| Q004 | Ocupação da mãe/mulher responsável |
| Q006 | Faixa de renda familiar |
| Q008 | Possui banheiro em casa? |
| Q010 | Possui carro na residência? |
| Q012 | Possui geladeira na residência? |
| Q014 | Possui máquina de lavar roupa? |
| Q016 | Possui forno micro-ondas? |
| Q019 | Possui televisão em casa? |
| Q021 | Possui TV por assinatura? |
| Q024 | Possui computador em casa? |
| Q025 | Possui acesso à internet? |

### 4. Dados do questionário de hábitos de estudo durante a pandemia

| Código da pergunta | Descrição |
|------------------|-----------|
| Q001 | Vínculo escolar durante a pandemia |
| Q004 | Percepção sobre o processo de aprendizagem na pandemia |
| Q006 | Ajuste do tempo de estudo conforme a dificuldade das matérias |
| Q009 | Leitura de textos antes das aulas ou videoaulas |
| Q013 | Realização de atividades avaliativas e simulados |
| Q018 | Estruturação das principais ideias para redações |
| Q020 | Participação em fóruns de discussão para tirar dúvidas |
| Q022 | Frequência nas aulas online nas datas programadas |
| Q025 | Meio mais utilizado para estudar ou se informar |
| Q027 | Dificuldades na rotina de estudos durante a pandemia |
| Q029 | Dificuldades de infraestrutura para estudar em 2021 |
| Q033 | Tipo de ajuda recebida para estudar em 2021 |
| Q034 | Nível de preparo para conduzir o próprio aprendizado |

## Possíveis análises e insights
Este dataset permite diversas análises, como:

- Impacto do nível socioeconômico no desempenho dos alunos
- Diferenças de desempenho entre alunos de escolas públicas e privadas
- Padrões de notas por faixa etária, sexo e cor/raça
- Correlação entre infraestrutura familiar e pontuação no exame
- Diferenças regionais nos resultados do ENEM
- Modelagem preditiva para identificar padrões de sucesso no exame

## Considerações finais
Os microdados do ENEM 2022 são uma fonte valiosa para análise educacional no Brasil, permitindo investigações detalhadas sobre fatores que influenciam o desempenho dos estudantes.