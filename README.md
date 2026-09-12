# Bengaluru House Price Prediction

A learning project with a scikit-learn housing model, a Flask prediction server, and an HTML/CSS/JavaScript client.

## Repository

- `notebooks/Banglore_house_price_prediction.ipynb`: training notebook
- `data/Bengaluru_House_Data.csv`: training data
- `data/model.pickle` and `data/columns.json`: existing inference artifacts
- `server/server.py`, `server/util.py`: Flask endpoints and artifact loading
- `client/`: browser interface

## Run locally

From the repository root in a separate Python environment:

```bash
python -m pip install -r requirements.txt
python server/server.py
```

The development server runs on port 5000. Open `client/app.html` and check its JavaScript API URL matches the running server. Retrain the model if its pickle is incompatible with your installed scikit-learn version.

## Limitations

Historical listing data is not a current market valuation. The saved model's package versions and a fresh evaluation are not recorded here. Verify input ranges, add endpoint tests and export the training environment before deployment. The repository slug is retained to preserve existing links.
