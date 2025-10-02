# Navigate to your project directory (you are already there)
cd C:\Users\ronys\Documents\FistAPI\1stPro

# Create the virtual environment (you already did this)
# python -m venv ./venv

# Activate the virtual environment (Crucial Step!)
.\venv\Scripts\activate

# (Optional) Upgrade pip within the active venv
pip install --upgrade pip

# Install FastAPI and Uvicorn (Corrected package name)
pip install fastapi uvicorn[standard] joblib pydantic pandas typing numpy

# Start API: Kill the server (Ctrl+C), then 
uvicorn main:app --reload

# Now you can start developing your FastAPI application!

# To check installed packages within the venv:
pip list

# When you are finished working, deactivate the environment:
deactivate