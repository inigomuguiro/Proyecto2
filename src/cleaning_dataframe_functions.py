import pandas as pd
import seaborn as sns
import numpy as np
import re
import os
import sys

def load_data(path):
    return pd.read_csv(path)

def drop_col(col, df):
    return df.drop(col, axis = 1, inplace=True)


def nan(df):
    """takes a data frame and removes all nan rows and columns"""
    df.dropna(axis=0, how = "all",inplace=True)
    df.dropna(axis=1, how = "all",inplace=True)
    return df


def drop(df):
    """asks for user autorization to drop columns with scarse data"""
    percent_missing = round(df.isnull().sum() * 100 / len(df), 2)
    if input("drop poor data colums? [y/n] ")=="y":
        t=int(input("Threshold [%] for data "))
        for c,n in zip(percent_missing.index,percent_missing.values):
            if n>t:
                df.drop([c], axis=1, inplace=True)
    return df


def filna(df):
    """takes a dataframe and replaces all NaN values depending on the type of the column
    if type is  string or object replaces with UNK 
    if type is int or float returns -1"""
    col_n = list(df.select_dtypes(include="object").columns) 
    for col in list(df.columns):
        if col in col_n:
            df.fillna("UNK",inplace=True)
        else:
            df.fillna(-1,inplace=True)
    return df