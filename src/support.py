import os
import pandas as pd

def read_data(path):
    
    df_dict = {}
    count = 1
    for data in os.listdir(path):
        df = pd.read_csv(f'{path}/{data}')
        df_dict[f'df{count}'] = df
        count +=1
    
    return df_dict