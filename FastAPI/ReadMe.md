# Navigate to project directory

# Create the virtual environment
    python -m venv ./venv

# Activate the virtual environment
    .\venv\Scripts\activate

# Install FastAPI and Uvicorn, ETC.
    pip install fastapi uvicorn[standard] joblib pandas scikit-learn lightgbm pydantic numpy

# Start API: Kill the server (Ctrl+C), then 
    uvicorn main:app --reload

# To check installed packages within the venv:
    pip list

# To finish working, deactivate the environment:
    deactivate

pa website delete --domain heartdiseaseprediction.pythonanywhere.com
pa website create --domain heartdiseaseprediction.pythonanywhere.com --command 'cd /home/heartdiseaseprediction/cardio-api && /home/heartdiseaseprediction/.virtualenvs/cardio-api-venv/bin/uvicorn --app-dir /home/heartdiseaseprediction/cardio-api --uds ${DOMAIN_SOCKET} main:app --log-level info'

pa website create --domain heartdiseaseprediction.pythonanywhere.com --command '/home/heartdiseaseprediction/.virtualenvs/cardio-api-venv/bin/uvicorn --app-dir /home/heartdiseaseprediction/cardio-api --uds ${DOMAIN_SOCKET} main:app --log-level info'

cd /home/heartdiseaseprediction/cardio-api

pip install scikit-learn-1.7.1 pip install --no-cache-dir scikit-learn
2a36cb474f35ea722a6b6d1895f859c52ccab1a7

pa website reload --domain heartdiseaseprediction.pythonanywhere.com