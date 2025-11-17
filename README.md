# 🔋 Forecasting EV Charging Load: A Machine Learning Approach to Smart Energy Management

## Overview

This project implements a machine learning and optimization solution for managing **Electric Vehicle (EV) charging** powered by **Solar Photovoltaic (PV) energy** within a microgrid. The primary goal is to leverage predictive analytics to create optimal charging schedules, thereby **maximizing renewable energy utilization** and **reducing overall grid costs** and strain.

### Project Context

Our solution utilizes time-series forecasting and classification models to predict key metrics and inform a sophisticated optimization framework for smart energy dispatch.

-----

## 💡 Core Features

| Feature | Description |
| :--- | :--- |
| **Primary Analysis Tool** | All data exploration, model training, and evaluation (using **XGBoost Regressor**) are executed and documented within the **`MLProject.ipynb` Jupyter Notebook**. |
| **Energy Forecasting** | Implements predictive models for essential metrics, including **Solar Power Generation** and **EV Charging Demand**. |
| **Charging Optimization** | The model outputs inform the **`Optimal_Charging_Decision`**, allowing the system to intelligently regulate demand based on energy costs and grid constraints. |
| **Interactive Web Application** | A **Flask API** (`app.py`) serves a user-friendly **HTML/CSS frontend** (`index.html`), enabling real-time input of parameters and visualization of the forecasted EV load. |

-----

## 💻 Technical Stack

| Category | Tools & Libraries |
| :--- | :--- |
| **Language** | Python 3.7+ |
| **Data Science** | pandas, numpy, scikit-learn |
| **Machine Learning** | **XGBoost** (Primary Model) |
| **Deployment** | **Flask** (for the web API), joblib (for model serialization) |
| **Environment** | **Jupyter Notebook** |

-----

## 🛠️ Getting Started

Follow these steps to clone the repository and run the project on your local machine.

### 1\. Prerequisites

Ensure you have **Git**, **Python 3.7+**, and **Jupyter Notebook** installed.

### 2\. Cloning the Repository

Open your terminal or command prompt and clone the project:

```bash
git clone https://github.com/kaviyavarshini08/AI-and-ML
cd AI-and-ML
```

### 3\. Installation

Install all required packages using pip:

```bash
pip install pandas matplotlib scikit-learn xgboost joblib flask
```

-----

## 🚀 Usage Instructions

The project runs in two main phases: reviewing the analysis and demonstrating the application.

### Phase 1: Running the Analysis Notebook (`MLProject.ipynb`)

1.  **Launch Jupyter Notebook:** Ensure you are in the project directory.
    ```bash
    jupyter notebook
    ```
2.  **Open the File:** Click on **`MLProject.ipynb`** in the browser window.
3.  **Execute Cells:** Run all cells to see the data processing, model training, and generate the saved model file (**`xgb_best_model.pkl`**).

### Phase 2: Running the Web Application Frontend

1.  **Start the Flask Server:** (After stopping the Jupyter process using **Ctrl + C**):
    ```bash
    python app.py
    ```
2.  **Access the Application:** Open your web browser and navigate to the address shown in the terminal (e.g., `http://127.0.0.1:5000/`).
3.  **Test Prediction:** Interact with the form to see the real-time forecasted EV load.

-----

## 📁 Repository Contents

| File Name | Description |
| :--- | :--- |
| **`MLProject.ipynb`** | **The core analysis and training file (Jupyter Notebook).** |
| **`PV_EV_CHARGING PPT.pptx`** | The official project presentation slide deck. |
| `app.py` | The Flask API file that handles prediction logic and serves the frontend. |
| `index.html` | The Frontend user interface for the interactive prediction tool. |
| `xgb_best_model.pkl` | The trained XGBoost model saved and used by `app.py`. |
| `PV_EV_Charging_Dataset.csv` | The raw, detailed dataset used for the project. |

-----

## 🤝 Contributing

Contributions are welcome\! Please open issues or submit pull requests.

