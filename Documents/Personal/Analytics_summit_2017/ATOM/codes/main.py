# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 19:51:44 2017

@author: anigoyal
"""
import pandas as pd
from input_parameters import *
from functions import *

    ##Input_dataset
    ##################

data_name = input_file_path + "//" + input_file_name
data = pd.read_csv(data_name)
print("The input data contains "+ str(data.shape[0])+" rows"+" and "+str(data.shape[1])+" columns")

    ##Dataset_statistics
    #######################

if require_variable_types==1:
    variable_types = variable_types_generator(data)
    
if require_missing_percentages==1:
    missing_percentages = missing_percentage_generator(data)
    
if require_parameter_statistics ==1:
    parameter_statistics = parameter_statistics_generator(data,statistics_required_for)
    
    ##Missing_value_imputation
    #######################

if impute_missing_values==1:
    if require_missing_percentages==1:
        imputed_data = missing_value_imputer(data,variables_to_impute,impute_by,require_missing_percentages,missing_percentages)
    else:
        imputed_data = missing_value_imputer(data,variables_to_impute,impute_by,require_missing_percentages,"")
    
if impute_missing_values==0:
    imputed_data = data.dropna(axis=0)            ## removing the rows that contain missing values
    
    ##Data_exploration
    #########################

if require_correlation_matrix==1:
    correlation_matrix = correlation_matrix_generator(imputed_data,Target_variable)
    
if require_bivariate_analysis ==1:
    bivaraite_analysis = bivariate_analysis()
 
