"""
Process a text file to count occurrences of the word "Romeo" and save the result.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import sys

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
from utils_logger import logger
import utils_project03

#####################################
# Declare Global Variables
#####################################

#Note: these 2 global vars are moved to utils_project_03.py
#FETCHED_DATA_DIR
#PROCESSED_DIR

#####################################
# Define Functions
#####################################

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting text processing...")
    utils_project03.set_globalvars_for_data_folders_empty() # call this function to SET global vars FETCHED_DATA_DIR, PROCESSED_DIR
    logger.info(f"Global vars FETCHED_DATA_DIR: {utils_project03.FETCHED_DATA_DIR}")
    logger.info(f"Global vars PROCESSED_DIR: {utils_project03.PROCESSED_DIR}")   
    #process_text_file()
    logger.info("Text processing complete.")