import pandas as pd

def read_data(filepath):
    """
    Reads in CSV from filepath and returns dataframe for analysis

    Inputs:
    filepath -> str: path to csv

    Outputs:
    df -> Dataframe: Dataframe for analsyis
    """
    df = pd.read_csv(filepath)
    return df

def ingress(df):
    # TODO write docstring
    # TODO convert birthdates to datatime
    # TODO convert string to number
    # TODO add drop duplicates function
    df['SEX'] = df['SEX'].map(
        {1:'Male',
         2:'Female'}
    )

    return df

def gender_count(df):
    #TODO write docstring
    #TODO write test
    male = len(df[df['SEX'] == 'Male'])
    female = len(df[df['SEX'] == 'Female'])

    return male, female

def child_count(df):
    #TODO write docstring
    #TODO write test
    return len(df['CHILD'].unique())