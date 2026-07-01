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
            cat_columns=[
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch", 
                "test_preprartion_score"
            ]
            num_pipeline=Pipeline( 
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler())

                ]
        
            )
            cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("onehotencoder",OneHotEncoder()),
                    ("scaler",StandardScaler())
                ]
            )
            logging.info("numerical columns cleaning done "),
            logging.info("categorical columns encoding done ")

            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,num_columns),
                    ("cat_pipeline",cat_pipeline,cat_columns)
                                        

                ]
            )
            return preprocessor 
        
        except Exception as e:
            raise CustomException(e,sys)
        

