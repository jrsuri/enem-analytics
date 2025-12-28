# ENEM 2022 Microdata Analysis

## Project Objective
This repository is dedicated to analyzing the ENEM 2022 microdata. The project includes data organization, exploratory analysis, machine learning modeling, and deployment considerations.

## What is ENEM?
The ENEM (Exame Nacional do Ensino Médio) is the primary standardized high school exam in Brazil. For an international context, it is the Brazilian equivalent of the SAT or ACT in the United States.

### Key points:
* College Entrance: It is the main gateway to higher education in Brazil, used for admission into nearly all public universities.
* Massive Scale: It is one of the largest exams in the world, taken by millions of candidates simultaneously across the country.
* Subjects: Covers Natural Sciences, Human Sciences, Languages, Mathematics, and a mandatory essay.
* Scoring (IRT): It uses Item Response Theory, where questions are weighted based on difficulty and consistency rather than just raw correct answers.
* Social Impact: It is a crucial tool for social mobility, providing access to scholarships and student loans.

## Repository Structure
- /data/ – Dataset (samples and reference files) and output files
- /models/ – Trained models
- /notebooks/ – Analysis and modeling notebooks (ordered and numbered for execution)
- /scripts/ – Data download and inference scripts
- dataset_description.md – Dataset description
- LICENSE – Repository license
- README.md – Repository explanation and general guidelines
- requirements.txt – Project dependency list

## Reproducibility & Environment
This project was developed in Python 3.10+. All required libraries are listed in `requirements.txt`.

The notebooks are numbered and should be executed **in the order they appear**, reflecting the analytical workflow of the project (data understanding → exploration → modeling → results).

The modeling decisions, comparison between approaches, and evaluation metrics are documented in notebooks 3 and 4.

## How to Reproduce the Project
1. Clone this repository
   git clone https://github.com/jrsuri/enem-analytics.git
   cd enem-analytics

2. Install dependencies
   pip install -r requirements.txt

3. Run the script to download the microdata
   python scripts/download_microdados_2022.py

4. Run the notebooks in the order they appear

## Modeling Overview
This project frames the task as a binary classification problem, where the model predicts whether a candidate is likely to achieve a high score or not.

Two machine learning approaches were tested during the project:
- Random Forest
- XGBoost (final selected model)

The XGBoost model was chosen based on its performance and is implemented and documented in **notebook 04 – Modeling**.

The notebook contains:
- model training and comparison
- evaluation workflow
- metrics and interpretation context

## Evaluation & Results
The evaluation process and performance metrics are presented in notebook 4, including the comparison between Random Forest and XGBoost and the rationale for selecting the final model.

The final XGBoost model achieved a **ROC AUC of 0.7456** and a **Matthews Correlation Coefficient (MCC) of 0.3838** on the evaluation dataset.

## To Run Predictions Only
1. Run the following script
   python scripts/inference.py

The script receives user inputs directly in the terminal and returns a probability-based prediction from the trained XGBoost model.

The output format is:

*** RESULT ***
The model predicts that the candidate will have a HIGH score, with a probability of XX%

or

*** RESULT ***
The model predicts that the candidate will NOT have a high score, with a probability of XX%

## About the ENEM 2022 Microdata
The ENEM microdata are provided by INEP and contain detailed information about participants, their answers, and exam results. In this project, the dataset is used for statistical analysis and predictive modeling in an educational and research-oriented context.

## Requirements
- Python 3.10+
- Libraries listed in requirements.txt

## License
This repository follows the MIT license.