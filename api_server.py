import os
import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(title="Enterprise Iris Prediction Service")

MODEL_PATH = "model.pkl"
if not os.path.exists(MODEL_PATH):
    raise RuntimeError(f"❌ Missing model asset at {MODEL_PATH}")

model = joblib.load(MODEL_PATH)

class IrisFeatures(BaseModel):
    features: List[float] = Field(..., min_items=4, max_items=4)

class PredictionResponse(BaseModel):
    prediction: int
    class_name: str
    probability_distribution: List[float]

CLASS_MAP = {0: "setosa", 1: "versicolor", 2: "virginica"}

@app.post("/predict", response_model=PredictionResponse)
async def predict_features(request: IrisFeatures):
    try:
        input_data = np.array(request.features).reshape(1, -1)
        pred_class = int(model.predict(input_data)[0])
        prob_dist = model.predict_proba(input_data)[0].tolist()
        return PredictionResponse(
            prediction=pred_class,
            class_name=CLASS_MAP[pred_class],
            probability_distribution=[round(p, 4) for p in prob_dist]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
