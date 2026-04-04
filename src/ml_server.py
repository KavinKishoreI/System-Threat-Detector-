
from typing import Any, Dict, Optional

import pandas as pd
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import joblib
import os
from dotenv import load_dotenv
# Features selected for the model (excluding the training label 'target')
USEFUL_COLUMNS = [
  "ProcessorCoreCount",
  "Processor",
  "SKUEditionName",
  "OSEdition",
  "OSBuildNumber",
  "ChassisType",
  "AppVersion",
  "IsSystemProtected",
  "IsPassiveModeEnabled",
  "AntivirusConfigID",
  "FirewallEnabled",
  "OSBranch",
  "AV_Imbalance",
  "SignatureAgeDays",
  "OSUpdateAgeDays",
  "FirewallWithoutProtection"
]


class ThreatFeatures(BaseModel):
  ProcessorCoreCount: Optional[int]
  Processor: Optional[str]
  SKUEditionName: Optional[str]
  OSEdition: Optional[str]
  OSBuildNumber: Optional[int]
  ChassisType: Optional[str]
  AppVersion: Optional[str]
  IsSystemProtected: Optional[bool]
  IsPassiveModeEnabled: Optional[bool]
  AntivirusConfigID: Optional[str]
  FirewallEnabled: Optional[bool]
  OSBranch: Optional[str]
  AV_Imbalance: Optional[bool]
  SignatureAgeDays: Optional[int]
  OSUpdateAgeDays: Optional[int]
  FirewallWithoutProtection: Optional[bool]  

def features_to_dataframe(payload: ThreatFeatures) -> pd.DataFrame:
  """Convert the pydantic payload to a single-row DataFrame in the
  expected column order, preserving boolean fields as True/False.
  """
  # Support Pydantic v1 and v2
  data: Dict[str, Any] = (
    payload.model_dump() if hasattr(payload, "model_dump") else payload.dict()
  )

  # Ensure DataFrame has all expected columns in order
  ordered = {col: data.get(col) for col in USEFUL_COLUMNS}
  
  df= pd.DataFrame([ordered])
  return df


app = FastAPI(title="System Threat Forecaster API")

# Enable CORS for local frontend (localhost:3000)
app.add_middleware(
  CORSMiddleware,
  allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)


@app.on_event("startup")
def load_model() -> None:
  """Load the trained pipeline into app state on startup."""
  # Load environment variables from .env
  try:
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))
  except Exception:
    pass
  app.state.api_key = os.getenv("API_KEY")

  model_path = os.path.join(os.path.dirname(__file__), "model_pipeline.pkl")
  try:
    app.state.model = joblib.load(model_path)
  except:
    print("Pipeline loading error")
 

@app.middleware("http")
async def require_authorization(request, call_next):
  """Require Authorization: Bearer <API_KEY> for all routes."""
  expected = getattr(app.state, "api_key", None) or os.getenv("API_KEY")
  auth = request.headers.get("authorization")
  if not expected:
    return JSONResponse({"detail": "API key not configured"}, status_code=503)
  if not auth or not auth.lower().startswith("bearer "):
    return JSONResponse({"detail": "Missing or invalid Authorization header"}, status_code=401)
  token = auth.split(" ", 1)[1].strip()
  if token != expected:
    print(token)
    print(expected)
    return JSONResponse({"detail": "Invalid API key"}, status_code=401)
  return await call_next(request)


@app.get("/")
def health() -> Dict[str, str]:
  return {"status": "ok"}


@app.post("/health")
def predict(features: ThreatFeatures) -> Dict[str, Any]:
  try :
    X = features_to_dataframe(features)
    model = app.state.model
    bool_cols = X.select_dtypes(include=["bool"]).columns
    X[bool_cols] = X[bool_cols].astype(int)

    cat_cols = X.select_dtypes(include=["string"]).columns
    X[cat_cols] = X[cat_cols].astype(object)

    y_pred = model.predict(X)

    result: Dict[str, Any] = {"prediction": int(y_pred[0])}

    # Return probability if available
    probs = model.predict_proba(X)

  # Probability of "threat" class (class = 1)
    result["probability_0"] = float(probs[0][0])
    result['probability_1'] = float(probs[0][1])
    return result
  except:
    print('Prediction error')
    return ({
      "message": "Invalid request"
    })

