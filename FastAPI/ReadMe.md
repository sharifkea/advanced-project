# How to set up the venv for API and run the server 

# Create the virtual environment 
    python -m venv ./venv

# Activate the virtual environment 
    .\venv\Scripts\activate

# Install FastAPI and Uvicorn 
    pip install fastapi uvicorn[standard] lightgbm scikit-learn pandas numpy pydantic joblib 

# Start API: We can kill the server with (Ctrl+C), then 
    uvicorn main:app --reload

# When finished working, deactivate the environment:
    deactivate
