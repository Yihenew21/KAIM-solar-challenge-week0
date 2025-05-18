# ☀️ KAIM Solar Challenge – Week 0

Welcome to the **KAIM Solar Challenge – Week 0** repository!  
This project provides the foundation for the KAIM Solar Challenge, focusing on environment setup, project organization, and preparing for the exciting weeks ahead.

---

## 📊 About the Project

This repository is structured to support a robust data science workflow for solar energy analysis. It includes:

- **Jupyter notebooks** for exploratory data analysis (EDA) of solar datasets from different regions (e.g., Benin, Sierra Leone).
- **Python scripts** for data processing and utility functions.
- **Unit tests** to ensure code reliability.
- **CI/CD workflows** for automated testing and quality assurance.

The project is designed for easy collaboration, reproducibility, and scalability as the challenge progresses.

---

## 📁 Project Structure

```
KAIM-solar-challenge-week0/
├── .github/workflows/      # GitHub Actions for CI/CD
├── notebooks/              # Jupyter notebooks for data exploration (e.g., benin_eda.ipynb, sierraleone_eda.ipynb, togo_eda.ipynb)
├── scripts/                # Python scripts for data processing/utilities
├── tests/                  # Unit tests for code reliability
├── .gitignore              # Ignore rules for version control
├── README.md               # Project overview and setup instructions
└── requirements.txt        # Python dependencies
```

---

## 🛠️ Getting Started

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/Yihenew21/KAIM-solar-challenge-week0.git
cd KAIM-solar-challenge-week0
```

### 2. Create and Activate a Virtual Environment

**For Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

**For macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Unit Tests

```bash
python -m unittest discover tests
```

---

## 📒 Notebooks Overview

- **notebooks/benin_eda.ipynb**  
  Exploratory data analysis and cleaning for Benin solar dataset, including outlier detection, imputation, and visualization.

- **notebooks/sierraleone_eda.ipynb**  
  EDA and cleaning for Sierra Leone solar dataset, with advanced visualizations (e.g., wind rose, bubble charts) and time series analysis.

- **notebooks/togo_eda.ipynb**  
  EDA and cleaning for Togo solar dataset, including summary statistics, outlier handling, and visual analytics.

Each notebook is self-contained and demonstrates best practices for data cleaning, visualization, and reporting.

---

## 🧪 Testing & Quality

- All scripts and notebooks are designed to be tested using the `tests/` directory.
- Continuous Integration (CI) is set up via GitHub Actions to automatically run tests on each push or pull request.

---

## 🚀 What's Next?

This Week 0 setup lays the groundwork for the upcoming phases of the KAIM Solar Challenge.  
Future weeks will involve:

- 📥 Data collection and preprocessing
- 📊 Exploratory data analysis
- 🤖 Model development and evaluation
- 🚀 Deployment strategies

Stay tuned for updates and new contributions!

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. **Fork** the repository
2. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit your changes**
   ```bash
   git commit -m "Add your feature"
   ```
4. **Push to your branch**
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a pull request**

Please ensure your code follows the project's coding standards and includes relevant tests.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📫 Contact

For questions or suggestions, feel free to reach out:

- GitHub: [@Yihenew21](https://github.com/Yihenew21)

---
