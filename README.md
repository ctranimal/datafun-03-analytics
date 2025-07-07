# the process for this project:

# next command, clone a github Repos (on the cloud) into local directory on my commputer
git clone https://github.com/ctranimal/datafun-03-analytics

# Create venv environment into ~/Repos/datafun-03-analytics
python3 -m venv .venv

# activate and install (repeat as necessary if adding additional dependency)
source .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install -r requirements.txt

# next editing files in VS Code, test regularly
python3 demo-script.py

# when code are working OK, regularly commit/push local code into remote (on the cloud) GitHub repository
git add .
git commit -m "Some descriptive comments about code changes go here"
git push -u origin main