# Dataset Description - ENEM 2022 Microdata

## Dataset Origin
The ENEM 2022 microdata are provided by the National Institute for Educational Studies and Research Anísio Teixeira (INEP) and contain detailed information about candidates, their schools, exam performance, and socioeconomic data collected through a questionnaire.

The dataset can be accessed directly on the official INEP website:
https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem

## Dataset Structure
The main available variables are presented below. The dataset is divided into four main parts:

### 1. Student, School, and Exam Data

| Variable Name         | Description                                         |
|----------------------|-----------------------------------------------------|
| NU_ANO               | Year of the ENEM exam                               |
| TP_FAIXA_ETARIA      | Candidate's age range                               |
| TP_SEXO              | Candidate's gender (M or F)                         |
| TP_COR_RACA          | Self-declared color or race                         |
| TP_ESCOLA            | Type of school attended                             |
| TP_ENSINO            | Type of high school                                 |
| CO_MUNICIPIO_PROVA   | City code where the participant took the exam       |
| SG_UF_PROVA          | State abbreviation where the exam was taken         |
| TP_PRESENCA_CN       | Presence in Natural Sciences exam                   |
| TP_PRESENCA_CH       | Presence in Human Sciences exam                     |
| TP_PRESENCA_LC       | Presence in Languages and Codes exam                |
| TP_PRESENCA_MT       | Presence in Mathematics exam                        |
| NU_NOTA_CN           | Natural Sciences score                              |
| NU_NOTA_CH           | Human Sciences score                                |
| NU_NOTA_LC           | Languages and Codes score                           |
| NU_NOTA_MT           | Mathematics score                                   |
| TP_LINGUA            | Chosen foreign language                             |
| TP_STATUS_REDACAO    | Essay status                                        |
| NU_NOTA_COMP1        | Essay competency 1 score                            |
| NU_NOTA_COMP2        | Essay competency 2 score                            |
| NU_NOTA_COMP3        | Essay competency 3 score                            |
| NU_NOTA_COMP4        | Essay competency 4 score                            |
| NU_NOTA_COMP5        | Essay competency 5 score                            |
| NU_NOTA_REDACAO      | Final essay score                                   |

### 2. Exam Items

| Variable Name    | Description                                   |
|------------------|-----------------------------------------------|
| CO_POSICAO       | Position of the item in the exam             |
| SG_AREA          | Knowledge area of the item                   |
| CO_ITEM          | Item code                                    |
| TX_GABARITO      | Item answer key                              |
| CO_HABILIDADE    | Skill evaluated by the item                  |
| IN_ITEM_ABAN     | Abandoned item indicator                     |
| TX_MOTIVO_ABAN   | Reason for item abandonment                  |
| NU_PARAM_A       | Item discrimination parameter                |
| NU_PARAM_B       | Item difficulty parameter                    |
| NU_PARAM_C       | Guessing parameter                           |
| TX_COR           | Exam color                                   |
| CO_PROVA         | Exam identifier                              |
| TP_LINGUA        | Foreign language                             |
| IN_ITEM_ADAPTADO | Item belonging to an adapted exam            |

### 3. Socioeconomic Questionnaire Data

| Question Code | Description                                      |
|---------------|--------------------------------------------------|
| Q001          | Father/male guardian's education level           |
| Q002          | Mother/female guardian's education level         |
| Q003          | Father/male guardian's occupation                |
| Q004          | Mother/female guardian's occupation              |
| Q006          | Family income bracket                            |
| Q008          | Does the house have a bathroom?                  |
| Q010          | Does the residence have a car?                   |
| Q012          | Does the residence have a refrigerator?          |
| Q014          | Does the residence have a washing machine?       |
| Q016          | Does it have a microwave?                        |
| Q019          | Does the house have a television?                |
| Q021          | Does it have cable/satellite TV?                 |
| Q024          | Does the house have a computer?                  |
| Q025          | Does it have internet access?                    |

### 4. Pandemic Study Habits Questionnaire

| Question Code | Description                                                |
|---------------|------------------------------------------------------------|
| Q001          | School enrollment status during the pandemic               |
| Q004          | Perception of the learning process during the pandemic     |
| Q006          | Adjustment of study time based on subject difficulty       |
| Q009          | Reading texts before classes or video lessons              |
| Q013          | Performance of evaluative activities and mock exams        |
| Q018          | Structuring main ideas for essays                          |
| Q020          | Participation in discussion forums to clear doubts         |
| Q022          | Attendance in online classes at scheduled times            |
| Q025          | Main method used to study or get informed                  |
| Q027          | Difficulties in study routine during the pandemic          |
| Q029          | Infrastructure difficulties for studying in 2021           |
| Q033          | Type of help received for studying in 2021                |
| Q034          | Level of preparedness to lead own learning                 |

## Potential Analyses and Insights
This dataset allows for various analyses, such as:

- Impact of socioeconomic status on student performance
- Performance differences between public and private school students
- Score patterns by age group, gender, and color/race
- Correlation between family infrastructure and exam scores
- Regional differences in ENEM results
- Predictive modeling to identify success patterns in the exam

## Final Considerations
The ENEM 2022 microdata are a valuable source for educational analysis in Brazil, enabling detailed investigations into factors that influence student performance.