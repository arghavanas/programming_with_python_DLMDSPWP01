import numpy as np
import math
from database import DataSet

class TrainingDataSet(DataSet):
    """Handles training data and finds best-fitting ideal functions."""

    def find_best_fits(self, ideal_ds):
        if self.df.empty or ideal_ds.df.empty:
            raise ValueError("Training or ideal dataset is empty. Load data first.")

        best_fits = {}
        for train_col in [col for col in self.df.columns if col != "x"]:
            min_sse, best_func, best_diff = float("inf"), None, None
            for ideal_col in [col for col in ideal_ds.df.columns if col != "x"]:
                diff = self.df[train_col] - ideal_ds.df[ideal_col]
                sse = np.sum(diff**2)
                if sse < min_sse:
                    min_sse, best_func, best_diff = sse, ideal_col, diff

            max_dev = float(np.max(np.abs(best_diff))) if best_diff is not None else 0.0
            best_fits[train_col] = {"ideal_func": best_func, "max_dev": max_dev}
            print(f"[INFO] Best fit for {train_col} is {best_func}, SSE={min_sse:.2f}, max_dev={max_dev:.2f}")

        return best_fits

class IdealDataSet(DataSet):
    """Handles the ideal functions dataset."""
    pass

class TestDataSet(DataSet):
    """Maps test points to best-fitting ideal functions within a threshold."""

    def map_test_points(self, best_fits, ideal_ds):
        if self.df.empty or ideal_ds.df.empty:
            raise ValueError("Test or ideal dataset is empty. Load data first.")

        thresholds = {info["ideal_func"]: math.sqrt(2) * info["max_dev"] for info in best_fits.values()}
        ideal_lookup = ideal_ds.df.set_index("x").to_dict(orient="index")

        mapped_points = []
        for _, row in self.df.iterrows():
            x_val, y_val = row["x"], row["y"]
            assigned_func, smallest_dev = None, None

            for _, info in best_fits.items():
                ideal_func = info["ideal_func"]
                if ideal_func not in thresholds:
                    continue

                try:
                    ideal_y = ideal_lookup[x_val][ideal_func]
                except KeyError:
                    continue

                deviation = y_val - ideal_y
                if abs(deviation) <= thresholds[ideal_func]:
                    if assigned_func is None or abs(deviation) < abs(smallest_dev):
                        assigned_func, smallest_dev = ideal_func, deviation

            if assigned_func:
                mapped_points.append({"x": x_val, "y": y_val, "ideal_func": assigned_func, "deviation": float(smallest_dev)})

        print(f"[INFO] Mapped {len(mapped_points)} out of {len(self.df)} test points.")
        return mapped_points
