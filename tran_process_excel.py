"""
Process an Excel file to count occurrences of a specific word in a column.

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import sys

# Import from external packages
import openpyxl

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

def count_word_in_column(file_path: pathlib.Path, column_letter: str, word: str) -> int:
    """Count the occurrences of a specific word in a given column of an Excel file."""
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        count = 0
        for cell in sheet[column_letter]:
            if cell.value and isinstance(cell.value, str):
                count += cell.value.lower().count(word.lower())
        return count
    except Exception as e:
        logger.error(f"Error reading Excel file: {e}")
        return 0
    

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting Excel processing...")
    utils_project03.set_globalvars_for_data_folders_empty() # call this function to SET global vars FETCHED_DATA_DIR, PROCESSED_DIR
    logger.info(f"Global vars FETCHED_DATA_DIR: {utils_project03.FETCHED_DATA_DIR}")
    logger.info(f"Global vars PROCESSED_DIR: {utils_project03.PROCESSED_DIR}")     
    #process_excel_file()
    logger.info("Excel processing complete.")