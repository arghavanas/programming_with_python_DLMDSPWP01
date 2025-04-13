import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.palettes import Category10
from bokeh.models import Legend


class Visualizer:
    """Visualizes test point assignments and ideal function curves."""

    def plot_test_assignments(self, mapped_points, ideal_ds, best_fits):
        p = figure(title="Test Data Assignments", x_axis_label="x", y_axis_label="y", width=600, height=400)
        colors = Category10[10]
        chosen_funcs = list({info["ideal_func"] for info in best_fits.values()})

        for i, func in enumerate(chosen_funcs):
            p.line(ideal_ds.df["x"], ideal_ds.df[func], color=colors[i % len(colors)], line_width=2, legend_label=f"Ideal {func}")

        df_mapped = pd.DataFrame(mapped_points)
        for i, func in enumerate(chosen_funcs):
            subset = df_mapped[df_mapped["ideal_func"] == func]
            p.scatter(subset["x"], subset["y"], color=colors[i % len(colors)], size=6, legend_label=f"Test -> {func}")

        legend = p.legend[0]
        p.add_layout(legend, 'right')  

        return p
