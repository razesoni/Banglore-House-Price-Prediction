# Bengaluru House Price Prediction

A machine learning project demonstrating end-to-end predictive modeling, from data exploration and model training to deployment and client-facing inference.

## Overview

This project implements a regression model trained on Bengaluru housing data to predict residential property prices. It includes a complete pipeline: Jupyter notebook-based analysis, a Flask REST API server, and an interactive web-based client interface.

## Key Features

- **Data-Driven Modeling**: Trained model using scikit-learn on historical Bengaluru housing data
- **RESTful API**: Flask server providing real-time price predictions
- **Web Interface**: HTML/CSS/JavaScript client for user-friendly predictions
- **Reproducible Artifacts**: Serialized model and configuration for consistent inference

## Project Structure

```
├── notebooks/
│   └── Banglore_house_price_prediction.ipynb    # Model training & EDA
├── data/
│   ├── Bengaluru_House_Data.csv                 # Training dataset
│   ├── model.pickle                             # Trained model artifact
│   └── columns.json                             # Feature configuration
├── server/
│   ├── server.py                                # Flask API server
│   └── util.py                                  # Prediction utilities
├── client/
│   └── app.html                                 # Web interface
└── requirements.txt
```

## Tech Stack

- **Machine Learning**: scikit-learn, Pandas, NumPy
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript

## Getting Started

### Prerequisites
- Python 3.x
- Virtual environment (recommended)

### Installation & Setup

1. Clone the repository
2. Create and activate a Python virtual environment
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the Flask server:
   ```bash
   python server/server.py
   ```

The API server runs on `http://localhost:5000`. Open `client/app.html` in a browser and ensure the JavaScript API endpoint matches your running server.

## Limitations & Considerations

- **Historical Data**: Model predictions reflect historical market patterns, not current valuations
- **Model Maintenance**: Package dependency versions should be documented; verify model compatibility before inference
- **Input Validation**: Review appropriate input ranges for your use case
- **Testing**: Production deployment should include endpoint test coverage and model evaluation metrics

## Future Enhancements

- Automated unit tests for API endpoints
- Model performance tracking and logging
- Enhanced input validation and error handling
- Documentation of package versions and model evaluation results

---

*This project demonstrates full-stack machine learning development, from exploration to deployment.*
