from solar_modules.data_loader import DataLoader
from solar_modules.data_cleaner import DataCleaner
from solar_modules.visualizer import DataVisualizer
import pandas as pd

class SolarAnalyzer:
    """
    Master class to run full data analysis pipeline on solar datasets.
    """

    def __init__(self, filepath, target_columns):
        """
        Initializes the analyzer with the dataset path and target columns.
        """
        self.filepath = filepath
        self.target_columns = target_columns
        self.df = None

    def run_pipeline(self):
        """
        Executes the full pipeline: load → clean → visualize → export.
        """

        # Step 1: Load data
        loader = DataLoader(self.filepath)
        self.df = loader.load_data()
        print("✅ Data loaded:", self.df.shape)

        # Step 2: Clean data (handle outliers & missing)
        cleaner = DataCleaner(self.df, self.target_columns)
        cleaner.handle_outliers()
        cleaner.handle_missing()
        self.df = cleaner.get_cleaned_data()
        print("✅ Data cleaned.")

        # Step 3: Visualize data
        viz = DataVisualizer(self.df)
        viz.plot_time_series()
        viz.plot_correlation_heatmap()
        viz.plot_pairwise_scatter()
        viz.plot_wind_rose()
        viz.plot_histograms()
        viz.plot_bubble_chart()

        # Step 4: Save cleaned data
        filename = self.filepath.replace(".csv", "_clean.csv")
        self.df.to_csv(filename, index=False)
        print(f"✅ Cleaned data exported to {filename}")
