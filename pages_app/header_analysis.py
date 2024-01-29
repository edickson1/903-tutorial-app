import pandas as pd
import streamlit as st
import numpy as np
import json
import plotly.express as px

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


st.title("903 Header Analysis App")

upload = st.file_uploader("Upload 903 Header file")

if upload:
    df = pd.read_csv(upload)

    with st.sidebar:
        ethnicities = st.sidebar.multiselect(
            'Select ethnicities for analysis',
            df["ETHNIC"].unique(),
            df["ETHNIC"].unique()
        )

    df = df[df["ETHNIC"].isin(ethnicities)]   
    df = ingress(df)
    now = pd.Timestamp('now')
    df["DOB"] = pd.to_datetime(df["DOB"], format='%d/%m/%Y', errors = "coerce")
    df['AGE'] = pd.to_datetime('today').normalize() - df['DOB']
    df['AGE'] = (df['AGE'] / np.timedelta64(1, 'Y')).astype('int')

    child_pop = child_count(df)
    male, female = gender_count(df)
    average_age = round(df['AGE'].mean())
    

    st.write(f"The total population of children is: {child_pop}")
    st.write(f"The total number of males is: {male}")
    st.write(f"The total number of females is: {female}")
    st.write(f"The average age is: {average_age}")

    gender_bar = px.bar(df,
                        x = "ETHNIC",
                        title = "Number of children in each ethnicity in 903 data",
                        labels = {"ETHNIC": "Ethnicity",
                                  "count": "Number of children"})
    st.plotly_chart(gender_bar)

    age_hist = px.histogram(df["AGE"],
                        title = "Number of children in each ethnicity in 903 data",
                        labels = {"value": "Age",
                                  "histnorm": "Number of children"}
                                  )
    age_hist.update_layout(
        xaxis_title_text = 'Age', 
        yaxis_title_text = 'Number of children'
        )    
    st.plotly_chart(age_hist)

    

    st.dataframe(df)