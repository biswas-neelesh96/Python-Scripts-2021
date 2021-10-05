# a function to clean data frame with pandas and numpy with different methods 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def clear_data(path, percentage=15, type='drop', method='mean', cat_list=[]):
    data = pd.read_csv(path)

    def return_missing_columns(data, percentage):
        columns_per = data.isnull().mean()*100
        return columns_per[columns_per > percentage].keys()

    missing_columns = return_missing_columns(data, percentage)
    columns_droped_data = data.drop(columns=missing_columns, axis=1)
    droped_final_data = columns_droped_data.copy()
    num_data = columns_droped_data.select_dtypes(['int64', 'float64'])
    
    if type == 'drop':
        final_data = columns_droped_data.dropna()
    elif type == 'num':
        if method == 'mean':
            droped_final_data.update(num_data.fillna(num_data.mean()))
        elif method == 'median':
            droped_final_data.update(num_data.fillna(num_data.median()))
        final_data = droped_final_data
    elif type == 'num_category':
        num_missing_columns = return_missing_columns(num_data, 0)
        if cat_list == []:
            raise ValueError(
                f'category list must be given for {num_missing_columns}')
        else:
            for cat_var, num_var in zip(cat_list, num_missing_columns):
                for i in droped_final_data[cat_var].unique():
                    if method == 'mean':
                        droped_final_data.update(droped_final_data[droped_final_data.loc[:, cat_var] == i][num_var].replace(
                            np.nan, droped_final_data[droped_final_data.loc[:, cat_var] == i][num_var].mean()))
                    if method == 'median':
                        droped_final_data.update(droped_final_data[droped_final_data.loc[:, cat_var] == i][num_var].replace(
                            np.nan, droped_final_data[droped_final_data.loc[:, cat_var] == i][num_var].median()))
            final_data = droped_final_data
           
    elif type == 'cat':
        cat_vars = columns_droped_data.select_dtypes(include='object')
        missing_cat_vars = return_missing_columns(cat_vars, 0)
        for i in missing_cat_vars:
           cat_vars.fillna({i: cat_vars[i].mode()[0]},inplace=True)
        final_data = cat_vars

        
    return final_data
