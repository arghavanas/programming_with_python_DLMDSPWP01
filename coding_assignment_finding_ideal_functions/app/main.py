from config import ENGINE, TRAIN_FILE, IDEAL_FILE, TEST_FILE, OUTPUT_PATH
from datasets import TrainingDataSet, IdealDataSet, TestDataSet
from visualizer import Visualizer
from bokeh.plotting import show, output_file

def main():
    # Initialize datasets
    train_ds = TrainingDataSet(name="Training Data", engine=ENGINE, table_name="training_data")
    ideal_ds = IdealDataSet(name="Ideal Functions", engine=ENGINE, table_name="ideal_functions")
    test_ds = TestDataSet(name="Test Data", engine=ENGINE, table_name="test_data")

    # Load CSV data into SQLite
    train_ds.load_csv_into_db(TRAIN_FILE)
    ideal_ds.load_csv_into_db(IDEAL_FILE)
    test_ds.load_csv_into_db(TEST_FILE)

    # Read datasets from DB
    train_ds.read_db_into_df()
    ideal_ds.read_db_into_df()
    test_ds.read_db_into_df()

    # Find best-fitting ideal functions
    best_fits = train_ds.find_best_fits(ideal_ds)

    # Map test points
    mapped_points = test_ds.map_test_points(best_fits, ideal_ds)

    # Visualization
    viz = Visualizer()
    test_plot = viz.plot_test_assignments(mapped_points, ideal_ds, best_fits)

    # Save output visualization
    output_file_path = f"{OUTPUT_PATH}/bokeh_visualization.html"
    output_file(output_file_path)
    show(test_plot)

    print(f"[INFO] Visualization saved at {output_file_path}")

if __name__ == "__main__":
    main()
