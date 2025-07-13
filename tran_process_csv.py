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
import util_project03

#####################################
# Declare Global Variables
#####################################

#Note: these 2 global vars are moved to utils_project_03.py
#FETCHED_DATA_DIR
#PROCESSED_DIR

#####################################
# Define Functions
#####################################

def analyze_ladder_score(file_path: pathlib.Path) -> dict:
    """Analyze the Ladder score column to calculate min, max, mean, and stdev."""
    northAmerica_countries_total: int = 0
    westernEurope_countries_total: int = 0
    countries_total: int = 0
    richest_country_name: str = ""
    richest_country_gdp: float = 0.0
    poorest_country_name: str = ""
    poorest_country_gdp: float = 100.0 # initially, set this to very high

    try:
        # initialize an empty list to store the scores
        score_list = []
        with file_path.open('r') as file:
            # csv.DictReader() methods to read into a DictReader so we can access named columns in the csv file
            dict_reader = csv.DictReader(file)  
            for row in dict_reader:
                try:
                    score = float(row["Ladder score"])  # Extract and convert to float
                    # append the score to the list
                    score_list.append(score)

                    if(str(row["Regional indicator"]) == "North America and ANZ"):
                        northAmerica_countries_total += 1
                    elif(str(row["Regional indicator"]) == "Western Europe"):
                        westernEurope_countries_total += 1

                    # increment the counter of countries processed
                    countries_total += 1

                    if(float(row["Logged GDP per capita"]) >= richest_country_gdp):
                        richest_country_gdp = float(row["Logged GDP per capita"])
                        richest_country_name = str(row["Country name"])
                    elif (float(row["Logged GDP per capita"]) < poorest_country_gdp):
                        poorest_country_gdp = float(row["Logged GDP per capita"])                        
                        poorest_country_name = str(row["Country name"])                        

                except ValueError as e:
                    logger.warning(f"Skipping invalid row: {row} ({e})")
        
        # Calculate statistics
        stats = {
            "min": min(score_list),
            "max": max(score_list),
            "mean": statistics.mean(score_list),
            "stdev": statistics.stdev(score_list) if len(score_list) > 1 else 0,
            "totalWesternEurope": westernEurope_countries_total, 
            "totalNorthernAmerica": northAmerica_countries_total,     
            "totalCountries": countries_total, 
            "richestCountry": richest_country_name,
            "richestGDP": richest_country_gdp, 
            "poorestCountry": poorest_country_name,
            "poorestGDP": poorest_country_gdp,                                                             
        }
        return stats
    except Exception as e:
        logger.error(f"Error processing CSV file, Exception Error is: {e}")
        return {}

def process_csv_file():
    """Read a CSV file, analyze Ladder score, and save the results."""
    
    input_file = pathlib.Path(util_project03.FETCHED_DATA_DIR, "2020_happiness.csv")
    output_file = pathlib.Path(util_project03.PROCESSED_DIR, "happiness_ladder_score_stats.txt")
    
    stats = analyze_ladder_score(input_file)

    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_file.open('w') as file:
        file.write("Ladder Score Statistics:\n")
        file.write(f"Minimum: {stats['min']:.2f}\n")
        file.write(f"Maximum: {stats['max']:.2f}\n")
        file.write(f"Mean: {stats['mean']:.2f}\n")
        file.write(f"Standard Deviation: {stats['stdev']:.2f}\n")
        file.write(f"# Western Europe countries: {stats['totalWesternEurope']}\n")   
        file.write(f"# Northern American countries: {stats['totalNorthernAmerica']}\n")  
        file.write(f"# Total countries: {stats['totalCountries']}\n")          
        file.write(f"# Richest country: {stats['richestCountry']} with GDP: {stats['richestGDP']}\n")      
        file.write(f"# Poorest country: {stats['poorestCountry']} with GDP: {stats['poorestGDP']}\n")                 
    # Log the processing of the CSV file
    logger.info(f"Processed CSV file: {input_file}, Statistics saved to: {output_file}")


#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    util_project03.set_globalvars_for_data_folders_empty() # call this function to SET global vars FETCHED_DATA_DIR, PROCESSED_DIR
    logger.info(f"Global vars FETCHED_DATA_DIR: {util_project03.FETCHED_DATA_DIR}")
    logger.info(f"Global vars PROCESSED_DIR: {util_project03.PROCESSED_DIR}")   
    process_csv_file()
    logger.info("CSV processing complete.")
