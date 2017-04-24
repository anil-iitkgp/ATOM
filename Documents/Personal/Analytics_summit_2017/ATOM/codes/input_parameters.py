# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 19:37:58 2017

@author: anigoyal
"""

    ##Input file parameters
    ########################

input_file_path = "C://Users//anigoyal//Documents//Data science competition//data//data"
input_file_name = "train.csv"

    ##Dataset_statistics
    #########################

require_variable_types = 1
require_missing_percentages = 0
require_parameter_statistics = 1
statistics_required_for = ["Smoker","Medical","POEP"]            ## add variable names ##Type variable names or type All

    ##Missing_value_imputation
    ############################

impute_missing_values = 1
variables_to_impute = ["All"]                                        ## add variable name or add All 
impute_by = ["Mean"]                                       ## Mean or Median or Mode ## add in the order to impute or if impute by a single metric add that

    ##Data_exploration
    ############################
Target_variable = "risk_class_num"
require_correlation_matrix = 1
require_bivariate_analysis = 1 