"""
Process a JSON file to count astronauts by spacecraft and save the result.

JSON file is in the format where people is a list of dictionaries with keys "craft" and "name".

{
    "people": [
        {
            "craft": "ISS",
            "name": "Oleg Kononenko"
        },
        {
            "craft": "ISS",
            "name": "Nikolai Chub"
        }
    ],
    "number": 2,
    "message": "success"
}

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import json
import pathlib
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
    logger.info(PROJECT_PREFIX+"Starting JSON processing...")
    #process_json_file()
    logger.info(PROJECT_PREFIX+"JSON processing complete.")