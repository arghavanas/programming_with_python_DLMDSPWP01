import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

class HoltWintersForecaster:
    """
    Holt-Winters forecaster for seasonal time series data.
    """

    def __init__(self, trend='add', seasonal='add', seasonal_periods=12):
        """
        :param trend: 'add' or 'mul' for trend component.
        :param seasonal: 'add' or 'mul' for seasonal component.
        :param seasonal_periods: Number of periods in a seasonal cycle (12 for monthly data).
        """
        self.trend = trend
        self.seasonal = seasonal
        self.seasonal_periods = seasonal_periods
        self.model = None
        self.results = None

    def fit(self, train_series):
        """
        Fit the Holt-Winters model on the training series.
        :param train_series: Pandas Series of sales data (indexed by date).
        """
        self.model = ExponentialSmoothing(
            train_series,
            trend=self.trend,
            seasonal=self.seasonal,
            seasonal_periods=self.seasonal_periods
        )
        self.results = self.model.fit()
        print("Holt-Winters model fitted.")

    def forecast(self, steps):
        """
        Forecasts for a specified number of periods (months).
        :param steps: Number of months to forecast.
        :return: Forecasted values as a Pandas Series.
        """
        forecast_values = self.results.forecast(steps=steps)
        return forecast_values
