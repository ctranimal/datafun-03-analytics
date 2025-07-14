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
Github_word_count_for_entire_excel: int = 0
MS_Word_word_count_for_entire_excel: int = 0
Jupyter_word_count_for_entire_excel: int = 0
VScode_word_count_for_entire_excel: int = 0
Canvas_word_count_for_entire_excel: int = 0
Google_word_count_for_entire_excel: int = 0
AllTools_word_count_for_entire_excel: int = 0

#####################################
# Define Functions
#####################################

def count_word_in_column(file_path: pathlib.Path, column_letter: str, word: str) -> int:
    """Count the occurrences of a specific word in a given column of an Excel file."""
    logger.info(f"count_word_in_column() is called, filepath={file_path}, column_letter={column_letter}, word={word}\n")
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
    
def count_word_in_entire_Excel_file(file_path: pathlib.Path, column_letter: str, word: str) -> int:
    """Count the occurrences of a specific word in a given column of an Excel file."""
    global Github_word_count_for_entire_excel
    global MS_Word_word_count_for_entire_excel
    global Jupyter_word_count_for_entire_excel
    global VScode_word_count_for_entire_excel
    global Canvas_word_count_for_entire_excel
    global Google_word_count_for_entire_excel
    global AllTools_word_count_for_entire_excel

    try:
        word_count = count_word_in_column(file_path, column_letter, word)
        logger.info(f"count_word_in_entire_Excel_file(): word_count is: {word_count}\n")
        #match_found: bool = false
        match word:
            case "GitHub":
                Github_word_count_for_entire_excel += word_count
            case "Microsoft Word":
                MS_Word_word_count_for_entire_excel += word_count
            case "Jupyter":
                Jupyter_word_count_for_entire_excel += word_count
            case "VS code":
                VScode_word_count_for_entire_excel += word_count
            case "Canvas":
                Canvas_word_count_for_entire_excel += word_count
            case "Google":
                Google_word_count_for_entire_excel += word_count

        if(word_count > 0):
            # update AllTools count if word_count > 0
            AllTools_word_count_for_entire_excel += word_count
        return word_count           
    except Exception as e:
        logger.error(f"Error in function count_word_in_entire_Excel_file(). Exception: {e}")
        return 0    
    
def process_excel_file():
    """Read an Excel file, count occurrences of 'GitHub' in a specific column, and save the result."""
    input_file = pathlib.Path(utils_project03.FETCHED_DATA_DIR, "Feedback.xlsx")
    output_file = pathlib.Path(utils_project03.PROCESSED_DIR, "excel_feedback_github_count.txt")
    
    # Write the results to the output file    
    output_file.parent.mkdir(parents=True, exist_ok=True)
    percent: float = 0.0

    # Open the output file in write mode and write the results
    with output_file.open('w') as file:
        # Update the output to describe your results
        for software_tool in {"GitHub", "Microsoft Word", "Jupyter", "VS code", "Canvas", "Google"}:
            for column_name in {"A", "B", "C", "D", "E", "F"}:
                # Call the function to count occurrences of the word in the specified column
                word_count = count_word_in_entire_Excel_file(input_file, column_name, software_tool)
                file.write(f"Occurrences of '{software_tool}' in column {column_name}: {word_count}\n")
            file.write(f"\n")
            
        file.write(f"***********************************\n  *** SUMMARY: *** \n")
        file.write(f"  Entire Excel file: Occurrences of ALL tools: {AllTools_word_count_for_entire_excel}\n\n") 

        percent = Github_word_count_for_entire_excel / AllTools_word_count_for_entire_excel
        file.write(f"  Entire Excel file: Occurrences of 'GitHub': {Github_word_count_for_entire_excel}. PERCENT: {percent:.2%}\n")

        percent = MS_Word_word_count_for_entire_excel / AllTools_word_count_for_entire_excel        
        file.write(f"  Entire Excel file: Occurrences of 'Microsoft Word': {MS_Word_word_count_for_entire_excel}. PERCENT: {percent:.2%}\n")

        percent = Jupyter_word_count_for_entire_excel / AllTools_word_count_for_entire_excel        
        file.write(f"  Entire Excel file: Occurrences of 'Jupyter': {Jupyter_word_count_for_entire_excel}. PERCENT: {percent:.2%}\n")

        percent = VScode_word_count_for_entire_excel / AllTools_word_count_for_entire_excel        
        file.write(f"  Entire Excel file: Occurrences of 'VS code': {VScode_word_count_for_entire_excel}. PERCENT: {percent:.2%}\n")

        percent = Canvas_word_count_for_entire_excel / AllTools_word_count_for_entire_excel        
        file.write(f"  Entire Excel file: Occurrences of 'Canvas': {Canvas_word_count_for_entire_excel}. PERCENT: {percent:.2%}\n")

        percent = Google_word_count_for_entire_excel / AllTools_word_count_for_entire_excel        
        file.write(f"  Entire Excel file: Occurrences of 'Google': {Google_word_count_for_entire_excel}. PERCENT: {percent:.2%}\n")

    # Log the processing of the Excel file    
    logger.info(f"Processed Excel file: {input_file}, Word count saved to: {output_file}")    


#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting Excel processing...")
    utils_project03.set_globalvars_for_data_folders_empty() # call this function to SET global vars FETCHED_DATA_DIR, PROCESSED_DIR
    logger.info(f"Global vars FETCHED_DATA_DIR: {utils_project03.FETCHED_DATA_DIR}")
    logger.info(f"Global vars PROCESSED_DIR: {utils_project03.PROCESSED_DIR}")     
    process_excel_file()
    logger.info("Excel processing complete.")