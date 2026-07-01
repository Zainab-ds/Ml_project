import os
import sys
from dataclasses import dataclass
import numpy as np 
import pandas as pd 
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from src.exception import CustomException
from src.logger import logging
@dataclass 
class datatransformerconfig:
    preprocessor_obj_file_path=os.path.join("artifacts","preprocessor.pkl")
class Datatransformation:
    def __init__(self):
        self.data_transformation_config=datatransformerconfig()
    def get_data_transformer_object(self):
        try:
            num_columns=["writing_score","reading_score"]
            categorical_columns=[
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preprartion_score"
            ]
            num_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median"))
                    ("scaler",StandardScaler())

                ]
            )
        except:
