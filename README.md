
# 🏥 Hospital Patient Data – End-to-End Analytics Pipeline

## 📌 Project Overview
This project demonstrates an **end-to-end healthcare data analytics pipeline** built using Python.  
It covers the complete lifecycle of a data analytics project — from **data generation** to **data cleaning**, **exploratory data analysis (EDA)**, and **automated pipeline execution** with logging and configuration management.

The goal is to simulate how hospital patient data can be analyzed to derive **actionable insights** that help improve **patient care, operational efficiency, and cost management**.

---

## 🎯 Business Objectives
- Analyze patient demographics and admission patterns  
- Understand disease distribution across departments  
- Evaluate length of hospital stay and treatment costs  
- Identify trends in patient outcomes  
- Build a reproducible, scalable analytics pipeline  

---

## 🧱 Project Architecture
Data Generation → Data Cleaning → Feature Engineering → EDA → Reports & Visuals

yaml
Copy code

The entire workflow is executed using **one master pipeline script**.

---

## 📂 Project Structure
hospital-patient-eda/
│
├── config/
│ └── config.yaml # Central configuration
│
├── data/
│ ├── raw/ # Generated raw datasets
│ └── processed/ # Cleaned & merged dataset
│
├── outputs/
│ ├── figures/ # EDA visualizations
│ └── reports/ # Analytical summary tables
│
├── scripts/
│ ├── generate_hospital_data.py
│ ├── data_cleaning.py
│ └── eda.py
│
├── src/
│ ├── init.py
│ ├── logger.py # Central logging
│ └── config_loader.py # YAML config loader
│
├── logs/
│ └── pipeline.log # Execution logs
│
├── run_pipeline.py # One-click pipeline runner
├── requirements.txt
└── README.md

yaml
Copy code

---

## 🧪 Datasets Generated
The project generates **synthetic hospital data** (1000+ records) across multiple tables:

- Patients  
- Admissions  
- Diagnosis  
- Treatments  
- Outcomes  

These datasets are joined and transformed into a **single analysis-ready table**.

---

## ⚙️ Technologies Used
- Python  
- Pandas & NumPy – data manipulation  
- Matplotlib & Seaborn – visualization  
- Faker – synthetic data generation  
- PyYAML – configuration management  
- Logging – pipeline monitoring  

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone <your-github-repo-url>
cd hospital-patient-eda
2️⃣ Create & Activate Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run Full Pipeline (One Command)
bash
Copy code
python run_pipeline.py
📊 Outputs
🔹 Data
data/raw/ → generated datasets

data/processed/hospital_patient_cleaned.csv

🔹 Visualizations
Saved in:

bash
Copy code
outputs/figures/
Includes:

Age distribution

Gender distribution

Disease frequency

Length of stay by department

Treatment cost by outcome

Correlation heatmap

🔹 Analytical Reports
Saved in:

bash
Copy code
outputs/reports/
Includes:

Department summary

Admission type vs outcome

Correlation matrix

📈 Key Insights

Emergency admissions show higher severity outcomes

Cardiology and Neurology departments have longer average stays

Treatment cost increases with length of stay

Certain departments consistently generate higher costs

Patient demographics influence hospital utilization patterns


🧠 Key Learnings

Built a config-driven analytics pipeline

Implemented centralized logging

Solved real-world issues like Python path resolution and virtual environment subprocess execution

Designed an enterprise-style folder structure

Automated EDA outputs for reuse in dashboards

🔮 Future Enhancements

Power BI / Tableau dashboard

Predictive modeling (length of stay, cost prediction)

Database integration (PostgreSQL)

CI/CD pipeline for automation

Data quality validation rules

👤 Author
Prasanta Kumar Deb
Data Analyst


⭐ If You Like This Project
Give it a ⭐ on GitHub — it helps visibility and motivation!