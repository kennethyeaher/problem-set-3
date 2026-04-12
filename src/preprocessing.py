'''
PART 1: PRE-PROCESSING
- Tailor the code scaffolding below to load and process the data
- Write the functions below
    - Further info and hints are provided in the docstrings
    - These should return values when called by the main.py
'''

import pandas as pd
import ast

def load_data():
    '''
    Load data from CSV files
    
    Returns:
        model_pred_df (pd.DataFrame): DataFrame containing model predictions
        genres_df (pd.DataFrame): DataFrame containing genre information
    '''
    model_pred_df = pd.read_csv('data/prediction_model_03.csv')
    genres_df = pd.read_csv('data/genres.csv')
    return model_pred_df, genres_df



def process_data(model_pred_df, genres_df):
    '''
    Process data to get genre lists and count dictionaries
    
    Returns:
        genre_list (list): List of unique genres
        genre_true_counts (dict): Dictionary of true genre counts
        genre_tp_counts (dict): Dictionary of true positive genre counts
        genre_fp_counts (dict): Dictionary of false positive genre counts
    '''
    genre_list = genres_df['genre'].tolist()

    # pasrese string lists into python lists 
    model_pred_df['actual_parsed'] = model_pred_df['actual genre'].apply(ast.literal_eval)

    # explode actual genres into one row per genre
    all_actuals = model_pred_df['actual_parsed'].explode()
    genre_true_counts = {g: 0 for g in genre_list} | all_actuals.value_counts().to_dict()

    # tp, predicted genre is in actual list; fp, it's not
    correct = model_pred_df[model_pred_df['correct?'] == 1]['predicted'].value_counts().to_dict()
    incorrect = model_pred_df[model_pred_df['correct?'] == 0]['predicted'].value_counts().to_dict()

    genre_tp_counts = {g: correct.get(g, 0) for g in genre_list}
    genre_fp_counts = {g: incorrect.get(g, 0) for g in genre_list}

    return genre_list, genre_true_counts, genre_tp_counts, genre_fp_counts




