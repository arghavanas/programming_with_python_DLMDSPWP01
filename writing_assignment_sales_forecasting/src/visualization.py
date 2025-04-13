import matplotlib.pyplot as plt

class Visualizer:
    """
    Handles plotting of training and forecast data.
    """

    @staticmethod
    def plot_forecast(train, forecast, title="Sales Forecast"):
        """
        Plots training data and forecast data.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(train.index, train, label='Historical Data', color='blue')
        plt.plot(forecast.index, forecast, label='Forecast', color='red')
        plt.title(title)
        plt.xlabel('Date')
        plt.ylabel('Sales')
        plt.legend()
        plt.show()
