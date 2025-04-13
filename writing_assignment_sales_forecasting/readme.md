# 📈 Sales Forecasting with Python and SQL  
### A Function Approximation Approach Using Holt-Winters Method

This project demonstrates how to build a **sales forecasting model** using Python and SQLite on real-world retail data. The model leverages **Holt-Winters (Triple Exponential Smoothing)** to predict future sales patterns based on historical data, following a function approximation methodology.

---

##  Dataset

**Online Retail II (UCI)**  
 Source: [Kaggle - Online Retail II UCI](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci)  
 Duration: December 1, 2009 – December 9, 2011  
 Focus: A UK-based online retailer primarily selling gifts to wholesalers.

The dataset contains transaction records with the following key attributes:
- InvoiceDate: Date and time of the transaction
- Quantity: Quantity of products sold (can be negative for cancellations)
- Price: Unit price per product
- Country, CustomerID, StockCode (not used in this model)

---

##  Methodology

This project is built entirely using **Python** and is focused on **time series forecasting** using a **function approximation approach**. Here's what we've done:

### 1. **Data Ingestion and Transformation**
- CSV data is loaded and stored in a local SQLite database.
- Negative quantities (returns/cancellations) are removed.
- Sales = Quantity * Price is calculated for each record.
- Data is **resampled monthly** to get total sales per month.

### 2. **Forecasting Model**
- We use the **Holt-Winters Exponential Smoothing** method, which captures:
  - **Trend** (rising/falling patterns)
  - **Seasonality** (repeating cycles, e.g., holiday spikes)
- The model is trained on the **entire dataset** (no test set due to limited duration).
- We forecast sales for the **next 36 months (3 years)**.

### 3. **Visualization**
- A clear and intuitive **matplotlib** plot shows:
  - Historical sales (blue line)
  - Forecasted future sales (red line)

---

##  Project Structure

SalesForecas_winter/
├── data/
│   ├── online_retail_II.csv      # Source CSV dataset
│   └── sales_data.db             # SQLite database (created automatically)
├── src/
│   ├── data_processing.py        # Data ingestion & transformation
│   ├── forecasting.py            # Holt-Winters forecasting logic
│   ├── visualization.py          # Plotting function
│   └── main.py                   # Main pipeline entry point
└── README.md                     # You're here!


---

## ▶ How to Run

### 1.Create and Activate Virtual Environment (Recommended)
Set up a Python virtual environment:

```bash
python -m venv .venv
```

Activate it:

- **Windows**  
  ```bash
  .venv\Scripts\activate
  ```

- **macOS/Linux**  
  ```bash
  source .venv/bin/activate


### 2. Install Dependencies

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

>  *If `requirements.txt` is missing, generate it with:*  
> `pip freeze > requirements.txt`

### 3. Add Data

- Download the dataset from [Kaggle](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci)  
- Save the `online_retail_II.csv` file into the `data/` directory

### 4. Run the Project

Navigate to the `src/` directory and run the main script:

```bash
cd src
python main.py
```

### 5. Output

- A graph displaying:  
  -  Historical monthly sales (blue line)  
  -  3-year future forecast (red line)
---

##  Why Holt-Winters?

We chose Holt-Winters (Triple Exponential Smoothing) because:
- It models both **trend** and **seasonality** in retail sales.
- It's effective for short-term forecasting with small datasets.
- It avoids overfitting and is more stable than ARIMA/SARIMA on this dataset size.

---

##  Notes

- This dataset ends in late 2011. There's **no future "test set"** available for validation.
- All available historical data is used for **training**.
- For production use, consider integrating **backtesting** or **cross-validation**.

---

##  Future Improvements

- Add SARIMA or Prophet for comparison
- Introduce model evaluation metrics (e.g., MAPE, RMSE)
- Extend with SQL views and scheduled forecasts
- Deploy as a Flask web app

---
##  Requirements

Here’s a minimal `requirements.txt` based on the actual code:

```
pandas
matplotlib
statsmodels
```

>  No need to install `sqlite3` separately — it's built into Python's standard library.

---

##  License

This project is released under the **MIT License**.

---

##  Acknowledgments

- Dataset: [UCI / Kaggle - Online Retail II](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci)  
- Forecasting: [Statsmodels Documentation](https://www.statsmodels.org/)
