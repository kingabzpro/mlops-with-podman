# src/app.py

import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import os

# Load the trained model
model_path = os.path.join("model", "model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

app = FastAPI()


class InputData(BaseModel):
    data: list  # List of dictionaries representing feature values


@app.post("/predict")
def predict(input_data: InputData):
    # Convert input data to DataFrame
    X_new = pd.DataFrame(input_data.data)
    # Ensure the columns match the training data
    prediction = model.predict(X_new)
    # Return predictions
    return {"prediction": prediction.tolist()}
