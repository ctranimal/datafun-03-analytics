datafun-03-analytics
This project demonstrates how to fetch and process various types of data (Excel, JSON, text, and CSV) using Python.

The repository includes:

Four example fetchers: Scripts to retrieve data from the web.
Four example processors: Scripts to analyze and process the fetched data.
Start by running the examples to understand their functionality, and then build your own scripts to fetch and process data of your choice (using each of these example types).

Project Requirements
VS Code
Git
Python
Professional Python Workflow
See pro-analytics-01

Commands to Manage Virtual Environment

py -m venv .venv
.\.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel
py -m pip install --upgrade -r requirements.txt
Commands to Run Python Scripts
Remember to activate your .venv (and install packages if they haven't been installed yet) before running files. Verify that all required packages are included in requirements.txt (and have NOT been commented out).

py example_get_csv.py
py example_get_excel.py
py example_get_json.py
py example_get_text.py

py example_process_csv.py
py example_process_excel.py
py example_process_json.py
py example_process_text.py

py yourname_get_csv.py
py yourname_get_excel.py
py yourname_get_json.py
py yourname_get_text.py

py yourname_process_csv.py
py yourname_process_excel.py
py yourname_process_json.py
py yourname_process_text.py

Commands to Git add-commit-push
git add .
git commit -m "custom message"
git push -u origin main
Create and Run Your Data Fetchers
Find data files on the web for each type (CSV, Excel, JSON, and text).
Create your own Python script to fetch each type of data and save it in a folder named data.
Name your scripts:
yourname_get_csv.py
yourname_get_excel.py
yourname_get_json.py
yourname_get_text.py
Implement your data-processing logic in small steps:
Fetch data for one file type.
Test, verify, and Git add-commit-push.
Create and Run Your Data Processors
Determine a simple metric from each of your data files.
Create your own Python script to read the data, process it, and save it in a folder named data_processed.
Name your scripts:
yourname_process_csv.py
yourname_process_excel.py
yourname_process_json.py
yourname_process_text.py
Work incrementally, using git add-commit-push after each bit of progress.
Update README.md to Describe Your Work
In your README.md, list each of your fetchers with a short description.
In your README.md, list each of your processors with a short description of what it does.
Include the execution commands to run your fetchers and processors.
Helpful Documentation
If you're unsure about any of the setup steps or tools, consult these resources:

requests library documentation
Tips
Use descriptive filenames for the data you fetch - and proper file extensions.
Work incrementally—verify each small step works before moving to the next.
The examples are required reading - use them to learn and understand first.
Test each script carefully before proceeding.
Use meaningful commit messages when pushing to GitHub to document your progress.
Review Commit History
Once your project is complete, review your commit history in GitHub under the Commits tab. Ensure your commit messages are clear and professional.