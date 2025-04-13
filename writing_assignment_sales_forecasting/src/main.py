import os
import pandas as pd
from data_processing import DataProcessor
from forecasting import HoltWintersForecaster
from visualization import Visualizer

def main():
    # Set up paths (adjust as needed)
    base_path = os.path.dirname(os.path.abspath(__file__))
    # Assuming 'data' folder is one level above 'src'
    data_folder = os.path.join(base_path, '..', 'data')
    db_path = os.path.join(data_folder, 'sales_data.db')
    csv_path = os.path.join(data_folder, 'online_retail_II.csv')
    
    # Instantiate DataProcessor with both DB and CSV paths.
    processor = DataProcessor(db_path=db_path, csv_path=csv_path)
    
    # Load and transform data from database
    raw_df = processor.load_data()
    monthly_sales = processor.transform_data(raw_df)
    
    # Print some info about the aggregated data
    print("Data loaded. Sales from", monthly_sales.index.min().date(), "to", monthly_sales.index.max().date())
    
    # Use the full dataset for training since there's no test set
    train_data = monthly_sales

    # Fit Holt-Winters model on the full dataset
    forecaster = HoltWintersForecaster(trend='add', seasonal='add', seasonal_periods=12)
    forecaster.fit(train_data)
    
    # Forecast for an additional 3 years (36 months) beyond the last available date
    forecast_steps = 36
    future_forecast_values = forecaster.forecast(steps=forecast_steps)
    future_forecast_index = pd.date_range(start=train_data.index[-1] + pd.offsets.MonthBegin(1),
                                          periods=forecast_steps, freq='MS')
    future_forecast_series = pd.Series(future_forecast_values.values, index=future_forecast_index)
    
    # Plot historical data and future forecast
    Visualizer.plot_forecast(train=train_data, forecast=future_forecast_series,
                             title="Holt-Winters Forecast (Next 3 Years)")
    
if __name__ == "__main__":
    main()
# This script serves as the entry point for the forecasting application.
# It orchestrates the data loading, processing, forecasting, and visualization.