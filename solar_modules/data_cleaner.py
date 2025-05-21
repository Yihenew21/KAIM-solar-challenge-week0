import pandas as pd
import numpy as np
from scipy.stats import zscore

class DataCleaner:
    def __init__(self, df, columns):
        self.df = df.copy()
        self.columns = columns
        self.z_scores = None
        self.outliers = None

    def generate_missing_value_report(self):
        """
        Generate a missing value report showing count and percent.
        """
        missing = self.df.isnull().sum()
        percent = (missing / len(self.df)) * 100
        report = pd.DataFrame({'Missing Values': missing, 'Percent': percent})
        return report[report['Missing Values'] > 0].sort_values(by='Percent', ascending=False)

    def detect_outliers_zscore(self, threshold=3):
        """
        Detect outliers using Z-score.
        """
        self.z_scores = self.df[self.columns].apply(zscore)
        self.outliers = (self.z_scores.abs() > threshold)
        return self.outliers, self.z_scores

    def impute_outliers(self, threshold=3):
        """
        Replace outliers in specified columns using median imputation.
        """
        if self.z_scores is None:
            self.detect_outliers_zscore(threshold)
        df_outliers_mask = self.z_scores.abs() > threshold
        df_masked = self.df[self.columns].mask(df_outliers_mask)
        df_imputed = df_masked.fillna(self.df[self.columns].median())
        self.df[self.columns] = df_imputed
        self.df['was_outlier'] = df_outliers_mask.any(axis=1)
        return self.df

    def handle_outliers(self, threshold=3):
        self.detect_outliers_zscore(threshold)
        self.impute_outliers(threshold)

    def handle_missing(self):
        self.df = self.df.fillna(self.df.median(numeric_only=True))

    def get_cleaned_data(self):
        return self.df
