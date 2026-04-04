# System Threat Forecaster

System Threat Forecaster is a machine learning project that uses 60,000+ telemetry records to predict whether a system has a possibility of malware infection. The trained model currently targets about 75% accuracy and is exposed through a small full-stack application:

- `frontend/system_threat`: React + Vite user interface
- `backend`: Node.js + Express API for auth, prediction requests, and MySQL persistence
- `src`: Python + FastAPI machine learning service that loads the trained pipeline

## Project Flow

1. A user registers or logs in from the React frontend.
2. The frontend sends device and security telemetry to the Node backend.
3. The backend validates the JWT token and forwards the telemetry to the FastAPI ML service.
4. The ML service loads the trained pipeline from `src/model_pipeline.pkl` and returns:
   - `prediction`
   - `probability_0`
   - `probability_1`
5. The backend stores the submitted system data and prediction result in MySQL.

## Tech Stack

- Frontend: React 19, Vite, React Router
- Backend: Node.js, Express, bcrypt, JWT, MySQL
- ML Service: Python, FastAPI, pandas, scikit-learn, joblib
- Database: MySQL

## Folder Structure

```text
.
├── backend/
│   ├── package.json
│   └── src/
├── frontend/
│   └── system_threat/
├── src/
│   ├── ml_server.py
│   ├── model_pipeline.pkl
│   ├── requirements.txt
│   └── *.ipynb
├── data/
└── README.md
```

## Prerequisites

Install these before starting:

- Node.js 18+ and npm
- Python 3.10+ recommended
- MySQL 8+

## 1. Clone The Project

```bash
git clone <your-repo-url>
cd "System threat forecaster"
```

## 2. Install Dependencies

### Frontend

```bash
cd frontend/system_threat
npm install
cd ../..
```

### Backend

```bash
cd backend
npm install
cd ..
```

### Python ML Service

Create and activate a virtual environment, then install Python packages:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r src/requirements.txt
```

## 3. Create The MySQL Database

The backend connects to a MySQL database named `systemthreat`.

Open MySQL and run:

```sql
CREATE DATABASE systemthreat;
USE systemthreat;

CREATE TABLE USERS (
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  user_name VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL
);

CREATE TABLE system_threat_features (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_name VARCHAR(255) NOT NULL,
  pc_name VARCHAR(255) NOT NULL,
  ProcessorCoreCount INT NULL,
  Processor VARCHAR(50) NULL,
  SKUEditionName VARCHAR(100) NULL,
  OSEdition VARCHAR(100) NULL,
  OSBuildNumber INT NULL,
  ChassisType VARCHAR(100) NULL,
  AppVersion VARCHAR(100) NULL,
  IsSystemProtected BOOLEAN NULL,
  IsPassiveModeEnabled BOOLEAN NULL,
  AntivirusConfigID VARCHAR(100) NULL,
  FirewallEnabled BOOLEAN NULL,
  OSBranch VARCHAR(100) NULL,
  AV_Imbalance BOOLEAN NULL,
  SignatureAgeDays INT NULL,
  OSUpdateAgeDays INT NULL,
  FirewallWithoutProtection BOOLEAN NULL,
  prediction INT NULL,
  infection_probability FLOAT NULL
);
```

Notes:

- The table names above match the names used in the source code.
- If you want stricter SQL types or foreign keys, you can extend the schema, but this structure matches the current app behavior.

## 4. Create Environment Files

This project needs two separate `.env` files.

### Backend `.env`

Create this file at [backend/.env](/home/kavin/projects/System threat forecaster/backend/.env):

```env
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
JWT_SECRET=replace_with_a_long_random_secret
ML_SECRET_KEY=replace_with_the_same_value_used_in_src_env
```

### ML Service `.env`

Create this file at [src/.env](/home/kavin/projects/System threat forecaster/src/.env):

```env
API_KEY=replace_with_the_same_value_as_ML_SECRET_KEY
```

Important:

- `ML_SECRET_KEY` in the backend and `API_KEY` in the ML service must be exactly the same.
- The backend expects MySQL to be available on `localhost`.
- The backend uses the fixed database name `systemthreat`.

## 5. Start The Services

You need three terminals.

### Terminal 1: Start the ML Service

From the project root:

```bash
source .venv/bin/activate
cd src
uvicorn ml_server:app --reload --host 0.0.0.0 --port 8000
```

The ML API will run on `http://localhost:8000`.

### Terminal 2: Start the Backend API

```bash
cd backend
node src/index.js
```

The backend API will run on `http://localhost:3000`.

### Terminal 3: Start the Frontend

```bash
cd frontend/system_threat
npm run dev
```

The frontend will run on `http://localhost:5173`.

## 6. Use The Application

1. Open `http://localhost:5173`
2. Register a new account
3. Log in
4. Open the dashboard
5. Fill in the telemetry fields
6. Submit the form to receive a malware risk prediction

## Example Prediction Payload

The backend and ML service are built around the following shape:

```json
{
  "ProcessorCoreCount": 4,
  "Processor": "x64",
  "SKUEditionName": "Pro",
  "OSEdition": "Core",
  "OSBuildNumber": 17134,
  "ChassisType": "Notebook",
  "AppVersion": "4.18.1807.18075",
  "IsSystemProtected": true,
  "IsPassiveModeEnabled": false,
  "AntivirusConfigID": "53447.0",
  "FirewallEnabled": true,
  "OSBranch": "rs4_release",
  "AV_Imbalance": false,
  "SignatureAgeDays": 25,
  "OSUpdateAgeDays": 100,
  "FirewallWithoutProtection": false
}
```

## API Summary

### Backend

- `POST /register/`: create user
- `POST /login/`: authenticate user and return JWT
- `GET /tokenAuth/`: validate JWT and return username
- `POST /predict`: send telemetry for prediction
- `GET /pcs`: fetch saved systems for the authenticated user

### ML Service

- `GET /`: health endpoint
- `POST /health`: prediction endpoint

## Common Issues

### MySQL connection error

Check:

- MySQL is running
- `DB_USER` and `DB_PASSWORD` are correct
- The `systemthreat` database exists

### `401` or `Invalid API key` from the ML server

Check:

- `backend/.env` contains `ML_SECRET_KEY`
- `src/.env` contains `API_KEY`
- Both values are identical

### Model loading error

Check:

- `src/model_pipeline.pkl` exists
- Your Python environment has all packages from `src/requirements.txt`

### Frontend starts but some flows feel broken

There are currently a few implementation issues in the codebase unrelated to setup, especially around the dashboard auth flow. The build succeeds, but linting still reports frontend issues that should be cleaned up next.

## Current Model Statement

- Dataset size: 60,000+ telemetry records
- Goal: estimate the possibility of malware infection
- Reported accuracy: approximately 75%

## Future Improvements

- Add backend npm scripts for development and production
- Add a database migration or SQL bootstrap file
- Add unit and integration tests
- Add model versioning and metrics reporting
- Improve dashboard and authenticated user flow
