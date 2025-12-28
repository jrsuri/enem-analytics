import msvcrt

try:
    import pickle
    import os
    import pandas as pd

    # Directory settings
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)
    models_dir = os.path.join(base_dir, 'models')
    input_path = os.path.join(models_dir, 'model.pkl')

    # Loads the saved model
    with open(input_path, 'rb') as f:
        model = pickle.load(f)

    # Option mappings for the values used in the model
    age_range_options = [
        'Under 17 years old', '17 years old', '18 years old', '19 years old', '20 years old',
        '21 years old', '22 years old', '23 years old', '24 years old', '25 years old',
        'Between 26 and 30 years old', 'Between 31 and 35 years old', 'Between 36 and 40 years old',
        'Between 41 and 45 years old', 'Between 46 and 50 years old', 'Between 51 and 55 years old',
        'Between 56 and 60 years old', 'Between 61 and 65 years old', 'Between 66 and 70 years old', 'Over 70 years old'
    ]

    mother_education_options = [
        'Never studied.', 'Did not complete 4th grade/5th year of Elementary School.',
        'Completed 4th grade/5th year, but did not complete 8th grade/9th year of Elementary School.',
        'Completed 8th grade/9th year of Elementary School, but did not complete High School.',
        'Completed High School, but did not complete College.',
        'Completed College, but did not complete Graduate studies.',
        'Completed Graduate studies.'
    ]

    family_income_options = [
        'No Income', 'Up to R$ 1,212.00', 'From R$ 1,212.01 to R$ 1,818.00.',
        'From R$ 1,818.01 to R$ 2,424.00.', 'From R$ 2,424.01 to R$ 3,030.00.',
        'From R$ 3,030.01 to R$ 3,636.00.', 'From R$ 3,636.01 to R$ 4,848.00.',
        'From R$ 4,848.01 to R$ 6,060.00.', 'From R$ 6,060.01 to R$ 7,272.00.',
        'From R$ 7,272.01 to R$ 8,484.00.', 'From R$ 8,484.01 to R$ 9,696.00.',
        'From R$ 9,696.01 to R$ 10,908.00.', 'From R$ 10,908.01 to R$ 12,120.00.',
        'From R$ 12,120.01 to R$ 14,544.00.', 'From R$ 14,544.01 to R$ 18,180.00.',
        'From R$ 18,180.01 to R$ 24,240.00.', 'Above R$ 24,240.00.'
    ]

    # Function to display options and capture user choice
    def select_option(options_list, message):
        print(message)
        for i, option in enumerate(options_list):
            print(f'[{i}] {option}')
        choice = int(input('Choose a number: '))
        return choice

    # Collects user inputs
    age_range = select_option(age_range_options, '\nSelect age range:')
    mother_education = select_option(mother_education_options, '\nSelect mother\'s education:')
    family_size = int(input('\nEnter family size (number of people): '))
    family_income = select_option(family_income_options, '\nSelect family income:')
    female_gender = int(input('\nGender (0 - Male, 1 - Female): '))
    private_school = int(input('\nDid you attend private school? (0 - No, 1 - Yes): '))
    trainee = int(input('\nAre you a trainee? (0 - No, 1 - Yes): '))

    # Race selection
    print('\nSelect race/color:')
    print('[0] White')
    print('[1] Asian')
    print('[2] Black')
    print('[3] Pardo (Mixed-race)')
    print('[4] Indigenous')
    race = int(input('Choose a number: '))

    # Defines binary race variables
    white_asian = 1 if race in [0, 1] else 0
    black_pardo_indigenous = 1 if race in [2, 3, 4] else 0

    # Computer at home
    has_computer = int(input('\nDo you have a computer at home? (0 - No, 1 - Yes): '))

    # Creates a DataFrame with the entered values
    columns = [
        'age_range', 'mother_education', 'family_size', 'family_income',
        'female_gender', 'private_school', 'trainee', 'white_asian',
        'black_pardo_indigenous', 'has_computer'
    ]

    input_data = pd.DataFrame([[age_range, mother_education, family_size, family_income,
                                female_gender, private_school, trainee, white_asian,
                                black_pardo_indigenous, has_computer]], columns=columns)

    # Makes the prediction
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    # Displays the result
    print('\n*** RESULT ***')
    if prediction == 1:
        print(f'The model predicts that the candidate will have a HIGH score, with a probability of {round(probability * 100, 2)}%')
    else:
        print(f'The model predicts that the candidate will NOT have a high score, with a probability of {round((1 - probability) * 100, 2)}%')

    print('\nPress any key to close.')
    msvcrt.getch()

except Exception as e:
    print(e)
    print('\nPress any key to close.')
    msvcrt.getch()