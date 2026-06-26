 # ==========================================================
# Import Required Libraries
# ==========================================================

import os
# os (Operating System module)
# Used to work with folders and file paths.
# Example:
# os.path.join("artifacts","train.csv")
# creates the path: artifacts/train.csv

import sys
# sys (System module)
# Used to interact with Python's runtime environment.
# Here it is passed to CustomException so we can get detailed
# information like the line number where an error occurred.

from src.exception import CustomException
# Import our custom exception class.
# Instead of showing a normal Python error,
# this class gives a more readable error message.

from src.logger import logging
# Import the logger.
# Logger records every important step of the program
# in a log file for debugging and monitoring.

import pandas as pd
# Pandas library is used for working with datasets.
# It reads CSV files into a DataFrame (table).

from sklearn.model_selection import train_test_split
# train_test_split()
# Used to divide the dataset into:
# 1. Training Data
# 2. Testing Data

from dataclasses import dataclass
# @dataclass automatically creates the constructor (__init__)
# and stores configuration variables easily.


# ==========================================================
# Configuration Class
# ==========================================================

@dataclass
# @dataclass automatically creates an __init__() method.
# We don't need to write a constructor manually.

class DataIngestionConfig:

    # Path where training data will be saved.
    # os.path.join() joins folder name and file name
    # according to the operating system.
    train_data_path: str = os.path.join("artifacts", "train.csv")

    # Path where testing data will be saved.
    test_data_path: str = os.path.join("artifacts", "test.csv")

    # Path where the original dataset copy will be saved.
    raw_data_path: str = os.path.join("artifacts", "data.csv")


# ==========================================================
# Data Ingestion Class
# ==========================================================

class DataIngestion:

    # Constructor
    # This method runs automatically whenever
    # an object of this class is created.
    def __init__(self):

        # Create an object of DataIngestionConfig.
        # Now all file paths become available through
        # self.ingestion_config.
        self.ingestion_config = DataIngestionConfig()


    # ======================================================
    # Main Data Ingestion Method
    # ======================================================

    def initiate_data_ingestion(self):

        # Write a message into the log file.
        # This helps us know that the Data Ingestion
        # process has started.
        logging.info("Entered the data ingestion method or component")

        try:

            # Read the CSV file.
            # pd.read_csv() loads the CSV file into a DataFrame.
            # DataFrame is like an Excel sheet inside Python.
            df = pd.read_csv('notebook/data/stud.csv')

            # Log that the dataset has been successfully read.
            logging.info('Read the dataset as dataframe')


            # ==================================================
            # Create Folder
            # ==================================================

            # self.ingestion_config.train_data_path
            # contains:
            # artifacts/train.csv

            # os.path.dirname()
            # extracts only the folder name.
            #
            # Example:
            # artifacts/train.csv
            # becomes
            # artifacts

            # os.makedirs()
            # creates the folder.

            # exist_ok=True means:
            # If the folder already exists,
            # do NOT give an error.

            os.makedirs(
                os.path.dirname(self.ingestion_config.train_data_path),
                exist_ok=True
            )


            # ==================================================
            # Save Original Dataset
            # ==================================================

            # Save the DataFrame into a CSV file.

            # self.ingestion_config.raw_data_path
            # contains:
            # artifacts/data.csv

            # index=False
            # Do not save row numbers (0,1,2...)

            # header=True
            # Save column names.

            df.to_csv(
                self.ingestion_config.raw_data_path,
                index=False,
                header=True
            )


            # Log that train-test splitting is starting.
            logging.info("Train test split initiated")


            # ==================================================
            # Split Dataset
            # ==================================================

            # train_test_split() divides the dataset into two parts.

            # df
            # Original DataFrame.

            # test_size=0.2
            # 20% data goes to the testing set.

            # Remaining 80%
            # goes to the training set.

            # random_state=42
            # Keeps the split the same every time
            # we run the program.
            # This makes experiments reproducible.

            train_set, test_set = train_test_split(
                df,
                test_size=0.2,
                random_state=42
            )


            # ==================================================
            # Save Training Dataset
            # ==================================================

            # Save train_set as train.csv

            # index=False
            # Do not save row numbers.

            # header=True
            # Save column names.

            train_set.to_csv(
                self.ingestion_config.train_data_path,
                index=False,
                header=True
            )


            # ==================================================
            # Save Testing Dataset
            # ==================================================

            # Save test_set as test.csv

            test_set.to_csv(
                self.ingestion_config.test_data_path,
                index=False,
                header=True
            )


            # Log that Data Ingestion is completed successfully.
            logging.info("Ingestion of the data is completed")


            # ==================================================
            # Return Paths
            # ==================================================

            # Return the locations of the generated files.
            # These paths will be used in the next component
            # (Data Transformation).

            return (

                self.ingestion_config.train_data_path,

                self.ingestion_config.test_data_path

            )


        # ======================================================
        # Exception Handling
        # ======================================================

        except Exception as e:

            # If any error occurs,
            # send the original error and system information
            # to our CustomException class.

            raise CustomException(e, sys)


# ==========================================================
# Driver Code
# ==========================================================

# This block executes only when this file is run directly.

if __name__ == "__main__":

    # Create an object of DataIngestion.
    obj = DataIngestion()

    # Start the complete Data Ingestion process.
    obj.initiate_data_ingestion()