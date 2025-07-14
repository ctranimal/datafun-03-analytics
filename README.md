#Project Name: datafun-03-analytics

##Description:
This project demonstrates how to fetch and process various types of data (Excel, JSON, text, and CSV) using Python.

##The repository includes:

### Sample / Starting code:
_ Four example fetchers: Scripts to retrieve data from the web. With filenames: example_get_*.py
_ Four example processors: Scripts to analyze and process the fetched data. With filesnames: example_process_*.py

### My implementation for credit:
_ Four files with filenames: tran_process_*.py

Commands to Manage Virtual Environment (On MacOS terminal)
cd ~/Repos/datafun-03-analytics
python3 -m venv .venv
./.venv/bin/activate

Note: requirements.txt is where the list of required packages are listed 
Use following commands to ensure the .venv environment folder has all required packages installed
py -m pip install --upgrade pip setuptools wheel
py -m pip install --upgrade -r requirements.txt

Commands to Run Python Scripts
Remember to activate your .venv (and install packages if they haven't been installed yet) before running files. Verify that all required packages are included in requirements.txt (and have NOT been commented out).

Firstly, run the example_get_*.py to obtain the required data files for processing by issuing these commands

python3 example_get_csv.py
python3 example_get_excel.py
python3 example_get_json.py
python3 example_get_text.py

Then, the sample data files will be created at ~/Repos/datafun-03-analytics/example_data folder

Run the following commands for files example_process_*.py to get a taste of what the example_process*.py should accomplish
python3 example_process_csv.py
python3 example_process_excel.py
python3 example_process_json.py
python3 example_process_text.py

Then, the sample processed files will be created at ~/Repos/datafun-03-analytics/example_processed folder

Now, to run my implementation of the *_process_*.py files, run the following commands

python3 tran_process_csv.py
python3 tran_process_excelpy
python3 tran_process_json.py
python3 tran_process_text.py

Then, the processed files will be created at ~/Repos/datafun-03-analytics/tran_processed folder

### Files descriptions for example fetchers:
example_get_csv.py  : This file fetches a sample csv file from the internet and make a copy locally to example_data folder.
example_get_excel.py  : This file fetches a sample excel file from the internet and make a copy locally to example_data folder.
example_get_json.py  : This file fetches a sample JASON file from the internet and make a copy locally to example_data folder.
example_get_text.py  : This file fetches a sample TEXT file (about Romeo play) from the internet and make a copy locally to example_data folder.


tran_process_csv.py   : This file process a sample CSV file from example_data folder, providing some descriptive statistics data such as: Min/Max/Mean/Standard Deviation and info on the richest/poorest countries with associated GDP data. The output file is located at the local tran_processed folder

tran_process_excel.py   : This file process a sample EXCEL file from example_data folder, The output file is located at the local tran_processed folder. The output file contain data such as: how many times all software tools (GitHub, Microsoft Word, Cannvas ...) were mentioned in the Excel cells

tran_process_json.py   : This file process a sample JASON file from example_data folder, The output file is located at the local tran_processed folder. The output file contain data such as: how many astronauts (and their names) associated with ISS and Tiangong teams. It then list all 27 teams of two members with one from each of ISS and Tiangong.

tran_process_text.py   : This file process a sample TEXT file from example_data folder, The output file is located at the local tran_processed folder. The output file contain data such as: how many time Speaking Actors lines are there. Usually, such lines would contain ALL CAPS. Thus, the script tran_process_test.py would analyze and summarize how many such Speaking Actors occurred.
