# Solar Cross-Country Comparison Dashboard

## Usage

1. Place cleaned CSVs in the `data/` directory:
   - `benin_clean.csv`
   - `sierraleone_clean.csv`
   - `togo_clean.csv`
2. Run the dashboard:
   ```
   streamlit run app/main.py
   ```
3. Use the sidebar to select countries and metrics for comparison.

## Features

- Boxplots for GHI, DNI, DHI by country
- Summary statistics table
- Bar chart of average GHI
- Download filtered data
- Statistical test results
- (Optional) Top regions table and histogram
