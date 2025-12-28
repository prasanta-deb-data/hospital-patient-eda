# 🏥 Hospital Patient Data Analysis | End-to-End Data Analytics Pipeline (Python)

## 📌 Project Summary
This project is an **end-to-end healthcare data analytics pipeline** built using **Python**, designed to demonstrate **real-world data analyst skills** including **data generation, data cleaning, feature engineering, exploratory data analysis (EDA), automation, logging, and configuration management**.

The project simulates **hospital patient data** and analyzes patient demographics, admission patterns, disease distribution, length of stay, treatment cost, and patient outcomes.  
It follows **industry-standard project structure** and is fully **GitHub and ATS optimized**.

---

## 🎯 Business Problem
Hospitals generate large volumes of patient data but often lack structured analytics to:
- Understand patient demographics
- Optimize hospital operations
- Reduce treatment costs
- Improve patient outcomes
- Identify high-risk admissions

This project addresses these challenges using **data analytics and visualization techniques**.

---

## 🧠 Key Skills Demonstrated (ATS Keywords)
- Data Analysis  
- Exploratory Data Analysis (EDA)  
- Data Cleaning & Data Wrangling  
- Feature Engineering  
- Python Programming  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Healthcare Analytics  
- Data Visualization  
- ETL Pipeline  
- Config-driven Architecture  
- Logging & Monitoring  
- Git & GitHub  
- Virtual Environments (venv)  
- Modular Python Project Structure  

---

## 🧱 Architecture Overview

Synthetic Data Generation
↓
Data Cleaning & Feature Engineering
↓
Exploratory Data Analysis (EDA)
↓
Reports & Visualizations


The entire workflow is executed via a **single pipeline script**, making it reproducible and scalable.

---

## 📂 Project Structure

hospital-patient-eda/
│
├── config/
│ └── config.yaml # Central configuration management
│
├── data/
│ ├── raw/ # Raw generated datasets
│ └── processed/ # Cleaned and merged dataset
│
├── outputs/
│ ├── figures/ # EDA visualizations (PNG)
│ └── reports/ # Summary analytics (CSV)
│
├── scripts/
│ ├── generate_hospital_data.py # Data generation
│ ├── data_cleaning.py # Data cleaning & feature engineering
│ └── eda.py # Exploratory data analysis
│
├── src/
│ ├── init.py
│ ├── logger.py # Centralized logging
│ └── config_loader.py # YAML configuration loader
│
├── logs/
│ └── pipeline.log # Pipeline execution logs
│
├── run_pipeline.py # End-to-end pipeline runner
├── requirements.txt
└── README.md


---

## 🧪 Dataset Description
Synthetic healthcare datasets with **1000+ records** are generated using Python:

- Patients (demographics)
- Admissions (department, admission type, dates)
- Diagnosis (disease, severity)
- Treatments (cost, treatment type)
- Outcomes (recovered, referred, deceased)

These datasets are joined into a **single analytical dataset** for EDA.

---

## ⚙️ Tools & Technologies
- **Python**
- **Pandas, NumPy** – data manipulation & analysis
- **Matplotlib, Seaborn** – data visualization
- **Faker** – synthetic data generation
- **PyYAML** – configuration management
- **Logging module** – pipeline monitoring
- **Git & GitHub** – version control

---

## 🚀 How to Run the Project

### Step 1: Clone Repository
```bash
