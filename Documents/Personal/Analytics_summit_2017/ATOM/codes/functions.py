# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 20:18:46 2017

@author: anigoyal
"""
from collections import OrderedDict

    #Dataset_statistics
    ###################

    ##Variable_type_generator
    ##########################

def variable_types_generator(data_set):
    numeric_columns = list(data_set._get_numeric_data().columns)
    nominal_columns = set(data_set.columns)-set(numeric_columns)
    types = ["nominal" if x in nominal_columns else "numeric" for x in data_set.columns]
    variable_type_pair = dict(zip(list(data_set.columns),types))
    return(variable_type_pair)
    
    ##Missing_percentage_generator
    ###############################

def missing_percentage_generator(data_set):
    missing_values_count = data_set.isnull().sum()
    missing_percentage = ((missing_values_count/data_set.shape[0])*100).round()
    variable_type_missing_percent_pair = dict(zip(list(missing_percentage.index),list(missing_percentage)))
    contains_missing = [(keys,values) for keys,values in variable_type_missing_percent_pair.items() if values>0]
    if (len(contains_missing)!=0):
       variable_type_missing_percent_pair = dict(contains_missing)
    else:
        variable_type_missing_percent_pair = "Data doesnot contain missing values"
    return(variable_type_missing_percent_pair)
    
    ##Parameter_statistics_generator
    ##################################
    
def parameter_statistics_generator(data_set,variables_to_consider):
    if variables_to_consider ==["All"]:
        numeric_columns = list(data_set._get_numeric_data().columns)
        nominal_columns = set(data_set.columns)-set(numeric_columns)
        parameter_statistics = dict()
        if (len(numeric_columns)!=0):
            numeric_stats = data_set.describe()
            for i in numeric_stats.columns:
                column_name = i
                parameter_statistics.update({i:dict(zip(list(numeric_stats[i].index),list(numeric_stats[i].round(2))))})
        if (len(nominal_columns)!=0):
            nominal_stats = data_set.describe(include=["O"])
            for i in nominal_stats.columns:
                column_name=i
                temp = data_set[i].value_counts()
                if (len(temp)<=20):    
                    parameter_statistics.update({column_name:dict(zip(list(temp.index),list(temp)))})
    else:
        data_set = data_set[variables_to_consider]
        numeric_columns = list(data_set._get_numeric_data().columns)
        nominal_columns = set(data_set.columns)-set(numeric_columns)
        parameter_statistics = dict()
        if (len(numeric_columns)!=0):
            numeric_stats = data_set.describe()
            for i in numeric_stats.columns:
                column_name = i
                parameter_statistics.update({i:dict(zip(list(numeric_stats[i].index),list(numeric_stats[i].round(2))))})
        if (len(nominal_columns)!=0):
            nominal_stats = data_set.describe(include=["O"])
            for i in nominal_stats.columns:
                column_name=i
                temp = data_set[i].value_counts()
                if (len(temp)<=20):    
                    parameter_statistics.update({column_name:dict(zip(list(temp.index),list(temp)))})
    return(parameter_statistics)
    
    ##Missing_value_imputer
    ###########################
    
def missing_value_imputer(data_set,variables_to_impute,impute_by,require_missing_percentages,missing_percentages):
    imputed_new_dataset = data_set.copy(deep=True)    
    if (variables_to_impute==["All"]):
        if(require_missing_percentages==1):
            missing_percentages = missing_percentages
        else:
            missing_percentages = missing_percentage_generator(data_set)
        if (missing_percentages == "Data doesnot contain missing values"):
            print("Data doesnot contain missing values")
        else:
            contains_missing_vals = missing_percentages.keys()
            numeric_columns = list(data_set._get_numeric_data().columns)
            nominal_columns = set(data_set.columns)-set(numeric_columns)
            missing_numeric_columns = [x for x in contains_missing_vals if x in numeric_columns]
            missing_nominal_columns = [x for x in contains_missing_vals if x in nominal_columns]
            if (len(missing_nominal_columns)!=0):
                print("Nominal features can only be imputed by Mode. Hence Imputing nominal features by Mode")
                for i in missing_nominal_columns:
                    imputed_new_dataset[i] = imputed_new_dataset[i].fillna(imputed_new_dataset[i].value_counts().index[0])
            if (impute_by==["Mean"]):
                imputed_new_dataset=imputed_new_dataset.fillna(imputed_new_dataset.mean())
            if(impute_by==["Median"]):
                imputed_new_dataset=imputed_new_dataset.fillna(imputed_new_dataset.median())
    else:
        for i in range(len(variables_to_impute)):
            if (impute_by[i] == "Mean"):
                imputed_new_dataset[variables_to_impute[i]]=imputed_new_dataset[variables_to_impute[i]].fillna(imputed_new_dataset[variables_to_impute[i]].mean())
            if (impute_by[i] == "Median"):
                imputed_new_dataset[variables_to_impute[i]]=imputed_new_dataset[variables_to_impute[i]].fillna(imputed_new_dataset[variables_to_impute[i]].median())
            if (impute_by[i] == "Mode"):
                imputed_new_dataset[variables_to_impute[i]] = imputed_new_dataset[variables_to_impute[i]].fillna(imputed_new_dataset[variables_to_impute[i]].value_counts().index[0])
    return(imputed_new_dataset)

    ##Data_exploration           
    ##########################

def correlation_matrix_generator(data_set,dependent_variable):
    independent_features = data_set.drop(dependent_variable,axis=1)
    correlation_matrix = independent_features.corr()
    if(correlation_matrix.shape[0]==0):
        print("No Numeric features in the dataset")
    else:
        return(correlation_matrix)
    
    
    
            
                
                
            
                
        
        
        
    
    
