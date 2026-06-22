import logging
# Logging = diary of the project
# Stores information such as:
# "Data Ingestion Started"
# "Model Training Completed"
# "Error Occurred"

import os
# os = File and Folder Manager
# Helps Python create folders and work with file paths

from datetime import datetime
# Used to get current date and time


# STEP 1
# Create a UNIQUE log file name using current date and time
# Example:
# 06_17_2026_15_30_45.log
#
# IMPORTANT:
# At this point NO file is created.
# Only the NAME is stored in a variable.
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"


# STEP 2
# Get current project folder
#
# Example:
# C:\Users\User\Ml_project
#
# Then add:
# logs
#
# Result:
# C:\Users\User\Ml_project\logs
#
# This is the FOLDER where log files will be stored.
logs_path = os.path.join(os.getcwd(), "logs")


# STEP 3
# Create the logs folder if it doesn't exist.
#
# Before:
#
# Ml_project
# ├── src
# └── notebook
#
# After:
#
# Ml_project
# ├── src
# ├── notebook
# └── logs
#
os.makedirs(logs_path, exist_ok=True)


# STEP 4
# Combine:
# Folder path + File name
#
# Folder:
# C:\Users\User\Ml_project\logs
#
# File:
# 06_17_2026_15_30_45.log
#
# Result:
# C:\Users\User\Ml_project\logs\06_17_2026_15_30_45.log
#
# This is the COMPLETE ADDRESS of the log file.
#
# IMPORTANT:
# The file still does NOT exist yet.
# Python only knows where it should be created.
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
#basic setup 
logging.basicConfig(
    filename=LOG_FILE_PATH,
    #format means how our logging message inside log file should appears.
    #%()--means insert the value of each term 
    #s--> for string 
    #d--. for decimal number 
    format="[ %(asctime)s ] %(name)s -%(lineno)d  -%(levelname)s-%(message)s",
    level=logging.info()
)