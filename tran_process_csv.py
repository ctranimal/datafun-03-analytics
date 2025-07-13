"""
Process a CSV file on 2020 Happiness ratings by country to analyze the `Ladder score` column and save statistics.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import csv
import statistics
import sys

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

FETCHED_DATA_DIR: str = "ctran_data"
PROCESSED_DIR: str = "ctran_processed"
PROJECT_PREFIX: str = "** PRJ-03 **"


#####################################
# Define Functions
#####################################

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info(PROJECT_PREFIX+"Starting CSV processing...")
    #process_csv_file()
    logger.info(PROJECT_PREFIX+"CSV processing complete.")
