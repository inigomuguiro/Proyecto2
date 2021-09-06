import src.cleaning_dataframe_functions as cl 

df = cl.load_data("summer.csv")

df2 = cl.drop_col("Event", df)


def nan(df):
    df.dropna(axis=0, how = "all",inplace=True)
    df.dropna(axis=1, how = "all",inplace=True)
    return df

def filna(df):
    col_n = list(df.select_dtypes(include="object").columns) 
    for col in list(df.columns):
        if col in col_n:
            df.fillna("UNK",inplace=True)
        else:
            df.fillna(-1,inplace=True)
    return df

















df.to_csv("bew.csv")