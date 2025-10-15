# Navigate to project directory

# Create the virtual environment
    python -m venv ./venv

# Activate the virtual environment
    .\venv\Scripts\activate

# Install FastAPI and Uvicorn, ETC.
    pip install fastapi uvicorn[standard] lightgbm joblib pandas scikit-learn

# Start API: Kill the server (Ctrl+C), then 
    uvicorn main:app --reload

# To check installed packages within the venv:
    pip list

# To finish working, deactivate the environment:
    deactivate
