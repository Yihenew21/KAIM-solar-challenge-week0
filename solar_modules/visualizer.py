import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np
import pandas as pd

class DataVisualizer:
    def __init__(self, df):
        self.df = df

    def plot_time_series(self, time_cols=None):
        if time_cols is None:
            time_cols = [col for col in self.df.columns if col not in ['Timestamp'] and np.issubdtype(self.df[col].dtype, np.number)]
        self.df.set_index('Timestamp')[time_cols].resample("D").mean().plot(figsize=(15, 6))
        plt.title("Daily Averages: Solar Irradiance and Temperature")
        plt.ylabel("Value")
        plt.grid(True)
        plt.show()

    def plot_cleaning_impact(self):
        df = self.df.copy()
        df['Cleaning'] = df['Cleaning'].fillna('Unknown')
        df.groupby('Cleaning')[['ModA', 'ModB']].mean().plot(kind='bar', figsize=(8, 5))
        plt.title("Average ModA and ModB by Cleaning Flag")
        plt.grid(True)
        plt.show()

    def plot_correlation_heatmap(self):
        plt.figure(figsize=(10, 8))
        cols = [col for col in ['GHI', 'DNI', 'DHI', 'TModA', 'TModB', 'Tamb', 'RH', 'WS'] if col in self.df.columns]
        sns.heatmap(self.df[cols].corr(), annot=True, cmap='coolwarm')
        plt.title("Correlation Heatmap")
        plt.show()

    def plot_pairwise_scatter(self):
        cols = [col for col in ['GHI', 'DNI', 'DHI', 'Tamb', 'WS', 'RH'] if col in self.df.columns]
        sns.pairplot(self.df, vars=cols, kind='scatter', plot_kws={'alpha': 0.3})
        plt.suptitle("Pairwise Scatter Plots", y=1.02)
        plt.show()

    def plot_wind_rose(self):
        if 'WS' in self.df.columns and 'WD' in self.df.columns:
            wind_data = self.df[['WS', 'WD']].dropna()
            wind_data['WD_bin'] = pd.cut(wind_data['WD'], bins=np.arange(0, 361, 30), labels=np.arange(0, 360, 30))
            wind_avg = wind_data.groupby('WD_bin')['WS'].mean().reset_index()
            fig = px.bar_polar(wind_avg, r='WS', theta='WD_bin', title='Wind Speed by Direction', template='plotly_dark')
            fig.show()

    def plot_histograms(self):
        cols = [col for col in ['GHI', 'WS'] if col in self.df.columns]
        self.df[cols].hist(bins=50, figsize=(12, 4), color='skyblue')
        plt.suptitle("Distribution of GHI and Wind Speed")
        plt.show()

    def plot_bubble_chart(self):
        if all(col in self.df.columns for col in ['Tamb', 'GHI', 'RH']):
            fig = px.scatter(self.df, x='Tamb', y='GHI', size='RH', color='RH', title='GHI vs Tamb vs RH', template='plotly_white')
            fig.show()
