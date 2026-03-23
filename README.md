# 📈 SPY Stock Price Predictor — MLOps Final Project

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20App-lightgrey?logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-D24939?logo=jenkins&logoColor=white)
![Airflow](https://img.shields.io/badge/Apache%20Airflow-Orchestration-017CEE?logo=apache-airflow&logoColor=white)
![CI](https://img.shields.io/github/actions/workflow/status/Minhal-Zafar/MLOPS_Final_Project/main.yml?label=GitHub%20Actions&logo=github-actions)

A fully production-grade **end-to-end MLOps pipeline** that trains a deep **LSTM neural network** to predict the closing price of the **SPY ETF (S&P 500)**, serves real-time predictions through a **Flask web dashboard**, and orchestrates the entire lifecycle through **Jenkins**, **Apache Airflow**, **Docker**, and **GitHub Actions CI/CD** — built as a collaborative team project.

---

## 🧠 What It Does

1. **Fetches live market data** from Yahoo Finance for the SPY ETF (Jan 2021 → today)
2. **Trains a 3-layer LSTM model** on 60-day lookback windows of MinMax-scaled closing prices
3. **Predicts** the next trading day's SPY closing price
4. **Serves a live interactive dashboard** displaying:
   - 📊 Actual vs. Predicted SPY price chart (13-month test window)
   - 📉 Training metrics per epoch — MSE, MAE, Cosine Proximity
   - 🔮 Next-day price prediction
5. **Orchestrates** the full pipeline via Apache Airflow DAGs on an hourly schedule
6. **Automates build & deployment** through a Jenkins pipeline and GitHub Actions

---

## 🏗️ Project Structure

```
MLOPS_Final_Project/
├── app.py                              # Flask app + LSTM training & inference
├── testdag.py                          # Apache Airflow DAG definition
├── templates/
│   └── chart.html                      # Chart.js dashboard (prices + training metrics)
├── requirements.txt                    # Python dependencies
├── Dockerfile                          # Docker image (python:3.9-slim-buster)
├── Jenkinsfile                         # Jenkins pipeline: build → run → teardown
├── makefile                            # Shorthand commands: install, format, lint
├── commands.txt                        # Airflow setup & Docker reference commands
└── .github/
    └── workflows/
        └── main.yml                    # GitHub Actions CI across all team branches
```

---

## 🤖 Model Architecture

The LSTM model is built with **TensorFlow / Keras** and trained from scratch on every startup:

| Layer          | Units | Dropout |
|----------------|-------|---------|
| LSTM (1)       | 50    | 20%     |
| LSTM (2)       | 50    | 20%     |
| LSTM (3)       | 50    | 20%     |
| Dense (Output) | 1     | —       |

**Training configuration:**

| Hyperparameter   | Value              |
|------------------|--------------------|
| Optimizer        | Adam               |
| Loss Function    | Mean Squared Error |
| Epochs           | 25                 |
| Batch Size       | 32                 |
| Lookback Window  | 60 trading days    |
| Feature Scaling  | MinMaxScaler [0,1] |

---

## ⚙️ Full MLOps Stack

| Layer               | Tool / Technology                              |
|---------------------|------------------------------------------------|
| ML / Deep Learning  | TensorFlow 2.x, Keras (LSTM), scikit-learn    |
| Data Ingestion      | yfinance, pandas-datareader, pandas, numpy     |
| Model Serving       | Flask, Jinja2, Chart.js                        |
| Containerisation    | Docker (python:3.9-slim-buster)               |
| Pipeline Orchestration | Apache Airflow 2.5.1 (hourly DAG)          |
| CI/CD Automation    | Jenkins (build + deploy pipeline)             |
| Source Control CI   | GitHub Actions (multi-branch)                 |
| Build Tooling       | Makefile (install, format, lint)              |
| Code Quality        | Flake8 (linting), Bandit (security scanning)  |

---

## 🔁 CI/CD Architecture

This project implements **three layers of automation**:

### 1. GitHub Actions — Source Control CI
Triggered on every push to `main` and every **merged** pull request across all team branches:

```
Push / Merged PR  →  main | minhal | hammas | abeeha
              │
              ▼
    ┌─────────────────────────┐
    │    Python Test Job       │
    │  ───────────────────    │
    │  ✅ Checkout code        │
    │  ✅ Set up Python 3.8    │
    └─────────────────────────┘
```

### 2. Jenkins Pipeline — Build & Deploy Automation
A full **Docker build → run → cleanup** pipeline automated via `Jenkinsfile`:

```
┌──────────────────────┐     ┌──────────────────────┐     ┌──────────────────────┐
│  Stage 1             │ ──▶ │  Stage 2             │ ──▶ │  Post: Cleanup       │
│  Build Docker Image  │     │  Run Container        │     │  Stop & remove       │
│  docker build ...    │     │  docker run -p 5000   │     │  all containers      │
└──────────────────────┘     └──────────────────────┘     └──────────────────────┘
```

### 3. Apache Airflow — Pipeline Orchestration
An Airflow DAG (`testdag.py`) runs on an **hourly schedule**, providing the scaffolding to orchestrate data ingestion, retraining, and serving as separate tasks:

```python
# DAG: dag_testing | Schedule: 0 * * * * (every hour)
dag_test_task  →  PythonOperator (extendable to full ML pipeline)
```

---

## 🚀 Getting Started

### Option 1 — Run with Docker (Recommended)

```bash
# 1. Clone the repo
git clone https://github.com/Minhal-Zafar/MLOPS_Final_Project.git
cd MLOPS_Final_Project

# 2. Build the Docker image
docker build -t spy-predictor .

# 3. Run the container
docker run -p 5000:5000 spy-predictor
```

Open your browser at **http://localhost:5000**

---

### Option 2 — Run via Makefile

```bash
# Install dependencies
make install

# Run the app
python app.py
```

---

### Option 3 — Run Locally (Manual)

```bash
# 1. Clone the repo
git clone https://github.com/Minhal-Zafar/MLOPS_Final_Project.git
cd MLOPS_Final_Project

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the Flask app
python app.py
```

Open your browser at **http://localhost:5000**

> ⚠️ **Note:** The LSTM model trains from scratch on every startup — allow a few minutes for training to complete before the dashboard loads. A GPU is recommended for faster training.

---

### Option 4 — Run via Jenkins

Ensure Docker and Jenkins are installed, then point a Jenkins pipeline job at this repository. The `Jenkinsfile` will automatically:
1. Build the Docker image `my-flask-app`
2. Run the container on port `5000`
3. Tear down and clean up containers after the run

---

## 🌀 Apache Airflow Setup

To run the Airflow orchestration layer:

```bash
# 1. Start a Python 3.8 Docker container
docker run -it --rm -p 8888:8080 python:3.8-slim /bin/bash

# 2. Set Airflow home and install dependencies
export AIRFLOW_HOME=/opt/airflow
apt-get update -y && apt-get install -y wget curl git gcc build-essential zip unzip

# 3. Create airflow user and virtual environment
useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow
su - airflow && cd /opt/airflow
python -m venv .airflowvirtualenv && source .airflowvirtualenv/bin/activate

# 4. Install Apache Airflow 2.5.1 with constraints
wget https://raw.githubusercontent.com/apache/airflow/constraints-2.5.1/constraints-3.8.txt
pip install "apache-airflow[crypto,celery,postgres,cncf.kubernetes,docker]"==2.5.1 \
    --constraint ./constraints-3.8.txt

# 5. Initialise the database and create an admin user
airflow db init
airflow users create -u admin -p admin -r Admin -e admin@example.com -f admin -l admin

# 6. Start the scheduler
airflow scheduler &

# 7. Copy the DAG into the Airflow dags folder
docker cp testdag.py <container_id>:/opt/airflow/.sandbox/lib/python3.8/site-packages/airflow/example_dags/testdag.py

# 8. Verify the DAG is registered
airflow dags list
```

---

## 📊 Dashboard Preview

The web dashboard (rendered via `Chart.js`) displays:

- **SPY Price Chart** — overlays actual closing prices against LSTM-predicted prices over a 13-month test window
- **Training Metrics Chart** — tracks MSE, MAE, and Cosine Proximity across all 25 training epochs
- **Next Day Prediction** — single scalar output for the next trading session's expected close price

---

## 📦 Dependencies

```
tensorflow        # LSTM model training & inference
scikit-learn      # MinMaxScaler preprocessing
pandas            # Data manipulation
pandas_datareader # Yahoo Finance data fetching
yfinance          # yfinance override for pandas_datareader
numpy             # Numerical operations
flask             # Web server & dashboard
flake8            # Code linting
bandit            # Security vulnerability scanning
```

---

## 📌 Key MLOps Concepts Demonstrated

| Concept                    | Implementation                                          |
|----------------------------|---------------------------------------------------------|
| ✅ Containerisation         | Docker (python:3.9-slim), port 5000 exposed            |
| ✅ Pipeline Orchestration   | Apache Airflow DAG with hourly schedule                |
| ✅ CI/CD Automation         | Jenkins: build → run → teardown pipeline               |
| ✅ Source Control CI        | GitHub Actions across 4 branches (team workflow)       |
| ✅ Live Data Ingestion      | Real-time Yahoo Finance API via yfinance               |
| ✅ Model Serving            | Flask REST interface with Chart.js visualisation       |
| ✅ Training Metric Tracking | MSE, MAE, Cosine Proximity tracked per epoch           |
| ✅ Build Tooling            | Makefile for install, format, lint automation          |
| ✅ Security Scanning        | Bandit integrated in CI pipeline                       |
| ✅ Team Collaboration       | Multi-branch PR workflow (minhal, hammas, abeeha)      |

---

## 👥 Team

| Student ID | Branch  |
|------------|---------|
| i190510    | minhal  |
| i192026    | hammas  |
| i190742    | abeeha  |

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> Final project for MLOps coursework — demonstrating a full production ML pipeline with LSTM model training, Flask serving, Docker containerisation, Jenkins CI/CD, Apache Airflow orchestration, and GitHub Actions across a collaborative multi-branch team workflow.
