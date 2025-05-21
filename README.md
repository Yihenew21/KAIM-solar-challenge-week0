# ☀️ KAIM Solar Challenge – Week 0

Welcome to the **KAIM Solar Challenge – Week 0** repository!  
This project provides a robust, modular pipeline for solar data analysis across West African countries, featuring reproducible code, cross-country comparison, and an interactive dashboard.

---

## 📊 Project Overview

This repository enables:

- **Modular data pipeline** for loading, cleaning, and visualizing solar datasets (Benin, Sierra Leone, Togo)
- **Exploratory Data Analysis (EDA)** for each country
- **Cross-country comparison** with statistical testing and visual summaries
- **Interactive Streamlit dashboard** for dynamic exploration
- **Comprehensive reporting** in both notebook and markdown/PDF formats

---

## 📁 Project Structure

```
KAIM-solar-challenge-week0/
├── app/                    # Streamlit dashboard (main.py, utils.py)
├── data/                   # Raw and cleaned CSVs (not included in repo)
├── notebooks/              # Jupyter notebooks (EDA, comparison)
├── solar_modules/          # Modular pipeline (data_loader, data_cleaner, visualizer, analyzer)
├── tests/                  # Unit tests
├── scripts/                # Utility scripts and documentation
├── final_report.md         # Medium-style final report (PDF exportable)
├── requirements.txt        # Python dependencies
└── README.md               # Project overview and instructions
```

---

## ��️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Yihenew21/KAIM-solar-challenge-week0.git
cd KAIM-solar-challenge-week0
```

### 2. Set Up a Virtual Environment

**Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📒 Notebooks & Analysis

- **notebooks/benin_eda.ipynb** – EDA and cleaning for Benin
- **notebooks/sierraleone_eda.ipynb** – EDA and cleaning for Sierra Leone
- **notebooks/togo_eda.ipynb** – EDA and cleaning for Togo
- **notebooks/compare_countries.ipynb** – Cross-country comparison: boxplots, summary tables, ANOVA/Kruskal–Wallis, and insights

Each notebook uses the modular pipeline for reproducibility and easy extension.

---

## 🧩 Modular Pipeline

- **solar_modules/data_loader.py** – Loads and parses solar datasets
- **solar_modules/data_cleaner.py** – Handles missing values and outliers
- **solar_modules/visualizer.py** – Generates plots and visual summaries
- **solar_modules/analyzer.py** – Orchestrates the full pipeline

---

## 📊 Cross-Country Comparison

- Loads cleaned data for Benin, Sierra Leone, and Togo
- Produces side-by-side boxplots for GHI, DNI, DHI
- Summary table of mean, median, std for each metric
- Statistical testing (ANOVA, Kruskal–Wallis) with p-values
- Bar chart ranking countries by average GHI
- Key findings and actionable insights

---

## 🖥️ Interactive Dashboard

- **app/main.py** – Streamlit app for dynamic exploration
  - Select countries and metrics
  - View boxplots, summary tables, and bar charts
  - Clean, intuitive UI
- To launch:
  ```bash
  streamlit run app/main.py
  ```

---

## 🧪 Testing & Quality

- All modules and scripts are tested via the `tests/` directory
- Continuous Integration (CI) with GitHub Actions for automated testing

---

## 📝 Reporting

- **final_report.md** – Medium-style final report (exportable to PDF)
- All code, notebooks, and dashboard are documented for clarity and reproducibility

---

## 🚀 Next Steps

- Add new countries or metrics by updating the data and reusing the pipeline
- Extend the dashboard with more interactive features
- Deploy the dashboard to Streamlit Community Cloud

---

## 🤝 Contributing

Contributions are welcome!  
Please fork the repo, create a feature branch, and submit a pull request.  
See the guidelines in this README for details.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📫 Contact

For questions or suggestions, reach out via:

- GitHub: [@Yihenew21](https://github.com/Yihenew21)

---
