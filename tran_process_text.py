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
SPEAKING_ACTOR_DICT: dict = {}

#####################################
# Define Functions
#####################################

def count_word_occurrences(file_path: pathlib.Path, word: str) -> int:
    """Count the occurrences of a specific word in a text file (case-insensitive)."""
    try:
        with file_path.open('r') as file:
            content: str = file.read()
            return content.lower().count(word.lower())
    except Exception as e:
        logger.error(f"Error reading text file: {e}")
        return 1
    

def obtain_Speaking_Actors_list(file_path: pathlib.Path):
     """Obtain a list of Speaking Actors (characterizeed by a line with ALL CAPS words)."""
     logger.info("obtain_Speaking_Actors_list() is called\n")
     try:
        with file_path.open('r') as file:
            for line in file:
                # process the line variable
                content: str = line.strip()
                if(content.isupper()):
                    # In the next line, make sure to ignore sing-lines that have words "ACT" or "PROLOGUE"
                    if(("ACT" not in content) and ("PROLOGUE" not in content)):
                        SPEAKING_ACTOR_DICT[content] = SPEAKING_ACTOR_DICT.get(content, 0) + 1
     except Exception as e:
        logger.error(f"Error reading text file: {e}")


def process_text_file():
    """Read a text file, count occurrences of 'Romeo', and save the result."""
 
    input_file = pathlib.Path(utils_project03.FETCHED_DATA_DIR, "romeo.txt")
    output_file = pathlib.Path(utils_project03.PROCESSED_DIR, "text_romeo_word_count.txt")

    word_to_count: str = "Romeo"
    word_count: int = count_word_occurrences(input_file, word_to_count)
    obtain_Speaking_Actors_list(input_file)

    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Write the results to the output file
    total_count: int = 0
    with output_file.open('w') as file:
        file.write(f"Occurrences of '{word_to_count}': {word_count}\n")
        file.write(f"Below are the names of Speaking Actors (and how many times they occurred)\n")
        for names, count in SPEAKING_ACTOR_DICT.items():
            total_count = total_count + count
            file.write(f"{names}: {count}\n")
        file.write(f"The total number of speaking-lines for all actors are: {total_count}\n")
    
    # Log the processing of the TEXT file
    logger.info(f"Processed text file: {input_file}, Word count saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting text processing...")
    utils_project03.set_globalvars_for_data_folders_empty() # call this function to SET global vars FETCHED_DATA_DIR, PROCESSED_DIR
    logger.info(f"Global vars FETCHED_DATA_DIR: {utils_project03.FETCHED_DATA_DIR}")
    logger.info(f"Global vars PROCESSED_DIR: {utils_project03.PROCESSED_DIR}")   
    process_text_file()
    logger.info("Text processing complete.")